class Solution:
    def decodeString(self, s: str) -> str:
        stack = list()
        decoded = ''
        k = ''
        for i in range(len(s)):
            # print(decoded, stack, k)
            if ord('a') <= ord(s[i]) <= ord('z') or ord('A') <= ord(s[i]) <= ord('Z'):
                decoded += s[i]
            elif ord('0') <= ord(s[i]) <= ord('9'):
                k += s[i]
            elif s[i] == '[':
                stack.append((len(decoded), int(k)))
                k = ''
            elif s[i] == ']':
                begin, _k = stack.pop()
                decoded += decoded[begin:] * (_k - 1)
        return decoded
