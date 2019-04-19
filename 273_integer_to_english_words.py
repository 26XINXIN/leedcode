class Solution:
    def __init__(self):
        self.comma_to_word = {
            1: 'Thousand',
            2: 'Million',
            3: 'Billion'
        }
        self.digit_to_word = {
            '1': 'One',
            '2': 'Two',
            '3': 'Three',
            '4': 'Four',
            '5': 'Five',
            '6': 'Six',
            '7': 'Seven',
            '8': 'Eight',
            '9': 'Nine'
        }
        self.teens_to_word = {
            '10': 'Ten',
            '11': 'Eleven',
            '12': 'Twelve',
            '13': 'Thirteen',
            '14': 'Fourteen',
            '15': 'Fifteen',
            '16': 'Sixteen',
            '17': 'Seventeen',
            '18': 'Eighteen',
            '19': 'Nineteen'
        }
        self.ties_to_word = {
            '2': 'Twenty',
            '3': 'Thirty',
            '4': 'Forty',
            '5': 'Fifty',
            '6': 'Sixty',
            '7': 'Seventy',
            '8': 'Eighty',
            '9': 'Ninety',
        }


    def numberToWords(self, num: int) -> str:
        if num == 0:
            return 'Zero'
        num = str(num)
        comma = len(num) // 3
        position = len(num) % 3
        if position == 0:
            position += 3
            comma -= 1
        str_num = ''
        while comma >= 0:
            if position < 3:
                n = num[:position]
            else:
                n = num[position-3:position]
            str_n = self._num_to_words(n)
            if str_num and str_n:
                str_num += ' ' + str_n
            else:
                str_num += str_n
            if comma > 0 and str_n:
                str_num += ' ' + self.comma_to_word[comma]
            comma -= 1
            position += 3
        return str_num
        
    def _num_to_words(self, n):
        n = n.lstrip('0')
        l = len(n)
        n_str = ''
        while l > 0:
            d = n[len(n)-l]
            if l == 3:
                n_str += self.digit_to_word[d] + ' Hundred'
            elif l == 2:
                if d == '1':
                    if n_str:
                        n_str += ' '
                    n_str += self.teens_to_word[n[-2:]]
                    return n_str
                elif d == '0':
                    pass
                else:
                    if n_str:
                        n_str += ' '
                    n_str += self.ties_to_word[d]
            elif l == 1:
                if d == '0':
                    pass
                else:
                    if n_str:
                        n_str += ' '
                    n_str += self.digit_to_word[d]
            l -= 1
        return n_str