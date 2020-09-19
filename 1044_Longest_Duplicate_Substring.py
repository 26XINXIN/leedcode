class Solution:
    def longestDupSubstring(self, S: str) -> str:
        duplicates = dict()
        max_length = 0
        max_seq = ''
        occurrence = dict()
        for i in range(len(S)):
            new_duplicates = dict()
            if S[i] in occurrence:
                for j in occurrence[S[i]]:
                    if j - 1 in duplicates:
                        l = duplicates.pop(j - 1)
                        new_duplicates[j] = l + 1
                    else:
                        new_duplicates[j] = 1
            for j, l in duplicates.items():
                if l > max_length:
                    max_length = l
                    max_seq = S[j - l + 1 : j + 1]
        
            if S[i] in occurrence:
                occurrence[S[i]].append(i)
            else:
                occurrence[S[i]] = [i]
            duplicates = new_duplicates
        
        for j, l in duplicates.items():
            if l > max_length:
                max_length = l
                max_seq = S[j - l + 1 : j + 1]
        return max_seq
            