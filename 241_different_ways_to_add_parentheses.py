class Solution:
    def diffWaysToCompute(self, input: str) -> List[int]:
        start, end = 0, 0
        nums = list()
        ops = list()
        while start < len(input):
            while end < len(input) and input[end].isdigit(): end += 1
            nums.append(int(input[start:end]))
            if end < len(input): ops.append(input[end])
            start, end = end + 1, end + 1
        print(ops)
        print(nums)
        return self.calculate(ops, nums)
        
    def calculate(self, ops, nums):
        if len(nums) == 1:
            return nums
        elif len(ops) == 1 and len(nums) == 2:
            return [self.cal(ops[0], nums[0], nums[1])]
        else:
            res = list()
            for i in range(len(ops)):
                num1 = self.calculate(ops[:i], nums[:i+1])
                num2 = self.calculate(ops[i+1:], nums[i+1:])
                for _num1 in num1:
                    for _num2 in num2:
                        res.append(self.cal(ops[i], _num1, _num2))
            return res

    def cal(self, op, num1, num2):
        if op == '+':
            return num1 + num2
        elif op == '-':
            return num1 - num2
        elif op == '*':
            return num1 * num2