from collections import Counter
class Solution:
    def maxRepOpt1(self, text: str) -> int:
        seq_info = list()
        i = j = 0
        while i < len(text):
            while j < len(text) and text[j] == text[i]:
                j += 1
            seq_info.append((text[i], j - i))
            i = j
        
        char_block_num = Counter([info[0] for info in seq_info])
        max_length = max([l + 1 if char_block_num[c] >= 2 else l for c, l in seq_info])
        
        for i in range(1, len(seq_info) - 1):
            if seq_info[i][1] == 1 and seq_info[i - 1][0] == seq_info[i + 1][0]:
                if char_block_num[seq_info[i - 1][0]] >= 3:
                    max_length = max(max_length, seq_info[i - 1][1] + seq_info[i + 1][1] + 1)
                else:
                    max_length = max(max_length, seq_info[i - 1][1] + seq_info[i + 1][1])
        return max_length