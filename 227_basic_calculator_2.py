class Solution:
    def calculate(self, s: str) -> int:
        ops = list()
        nums = list()
        i = 0
        while i < len(s):
            # print('op',ops)
            # print('num', nums)
            c = s[i]
            if c == ' ':
                pass
            elif c in ['*', '/']:
                ops.append(c)
            elif c in ['+', '-']:
                while ops and ops[-1] in ['+', '-']:
                    num2 = nums.pop()
                    num1 = nums.pop()
                    op = ops.pop()
                    nums.append(self.basic_cal(num1, num2, op))
                ops.append(c)
            elif c == '(':
                ops.append(c)
            elif c == ')':
                ops.pop()
                while ops and ops[-1] != '(':
                    op = ops.pop()
                    num2 = nums.pop()
                    num1 = nums.pop()
                    num = self.basic_cal(num1, num2, op)
                    nums.append(num)
            else: # c is numbers
                start = i
                while i < len(s) and s[i] in '0123456789': 
                    i += 1
                num = int(s[start:i])
                if ops and ops[-1] in ['*', '/']:
                    op = ops.pop()
                    other = nums.pop()
                    num = self.basic_cal(other, num, op)
                nums.append(num)
                i -= 1
            i += 1
        while ops:
            op = ops.pop()
            num2 = nums.pop()
            num1 = nums.pop()
            nums.append(self.basic_cal(num1, num2, op))
        return nums[-1]
    
    def basic_cal(self, num1, num2, op):
        if op == '*':
            return num1 * num2
        elif op == '/':
            return num1 // num2
        elif op == '+':
            return num1 + num2
        elif op == '-':
            return num1 - num2
                