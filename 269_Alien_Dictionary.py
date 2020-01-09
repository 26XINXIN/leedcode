class Solution:
    def alienOrder(self, words) -> str:
        less = list()
        for i in range(len(words) - 1):
            for a, b in zip(words[i], words[i+1]):
                if a != b:
                    less.append(a + b)
                    break
        
        chars = set(''.join(words))
        order = ''
        while less:
            free = chars - set([l[1] for l in less])
            if not free:
                return ''
            order += ''.join(free)
            less = list(filter(free.isdisjoint, less))
            chars -= free
        return order + ''.join(chars)