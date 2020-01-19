class Solution:
    def compress(self, chars: List[str]) -> int:
        cnt = 0
        length, i = len(chars), 0
        while i < length:
            if i == 0:
                cnt = 1
                i += 1
            elif chars[i] == chars[i-1]:
                cnt += 1
                chars.pop(i)
                length -= 1
            elif chars[i] != chars[i-1]:
                if cnt > 1:
                    for c in str(cnt):
                        chars.insert(i, c)
                        i += 1; length += 1
                cnt = 1
                i += 1
        if cnt > 1:
            for c in str(cnt):
                chars.append(c)
                length += 1
        return length