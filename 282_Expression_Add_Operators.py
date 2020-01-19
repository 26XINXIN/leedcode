class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        self.result = list()
        self.num = num
        self.target = target
        if not num:
            return []

        self.search(0, 0, '*', 0, '')

        return self.result
    
    def search(self, a, b, op, s, pred):
        # print(a, op, b, s, pred)
        if s == len(self.num):
            if op == '*':
                res = a * b
            elif op == '+':
                res = a + b
            elif op == '-':
                res = a - b
            if res == self.target:
                self.result.append(pred)
            return
        if s == 0:
            valid_ops = ['+']
        else:
            valid_ops = ['+', '-', '*']
        if self.num[s] == '0':
            for op_next in valid_ops:
                if op_next == '*' and op != '*':
                    a_next = a
                    b_next = 0
                    self.search(a_next, b_next, op, s+1, pred + op_next + '0' if pred else '0')
                else:
                    if op == '*':
                        a_next = a * b
                    elif op == '+':
                        a_next = a + b
                    elif op == '-':
                        a_next = a - b
                    b_next = 0
                    self.search(a_next, b_next, op_next, s+1, pred + op_next + '0' if pred else '0')
        else:
            for j in range(s+1, len(self.num) + 1):
                c = int(self.num[s:j])
                for op_next in valid_ops:
                    if op_next == '*' and op != '*':
                        a_next = a
                        b_next = b * c
                        self.search(a_next, b_next, op, j, pred + op_next + self.num[s:j] if pred else self.num[s:j])
                    else:
                        if op == '*':
                            a_next = a * b
                        elif op == '+':
                            a_next = a + b
                        elif op == '-':
                            a_next = a - b
                        b_next = c
                        self.search(a_next, b_next, op_next, j, pred + op_next + self.num[s:j] if pred else self.num[s:j])