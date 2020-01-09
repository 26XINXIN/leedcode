from copy import deepcopy
from queue import Queue

class Solution:
    def isSolvable(self, words, result ):
        chars = set()
        for word in words:
            for c in word:
                chars.add(c)
        for c in result:
            chars.add(c)
        if len(chars) > 10:
            return False
        
        headings = [w[0] for w in words if len(w) > 1]
        domains = {c: set(range(10)) if c not in headings else set(range(1, 10)) for c in chars}
        self.var = list(chars)
        self.words = [word[::-1] + '0' * (len(result) - len(word)) for word in words]
        self.result = result[::-1]
        
        return self.canAssign({'0': 0}, domains, 0, 0, 0)
    
    def canAssign(self, assign, domains, i, w, addOne):
        # print(assign)
        if i == len(self.result):
            return True
        
        if w == len(self.words):
            thisSum = sum(assign[word[i]] for word in self.words) + addOne
            newAddOne = thisSum // 10
            res = thisSum % 10
            if self.result[i] in assign:
                if assign[self.result[i]] == res:
                    # newDomains = self.forwardChecking(domains, self.result[i], res)
                    return self.canAssign(assign, domains, i+1, 0, newAddOne)
                else:
                    return False
            if res in domains[self.result[i]]:
                newAssign = deepcopy(assign)
                newAssign[self.result[i]] = res
                newDomains = self.forwardChecking(domains, self.result[i], res)
                if newDomains:
                    return self.canAssign(newAssign, newDomains, i+1, 0, newAddOne)
                else:
                    assign.pop(domains[self.result[i]])
                    return False
            else:
                return False
        else:
            if self.words[w][i] == '0':
                return self.canAssign(assign, domains, i, w+1, addOne)
            elif self.words[w][i] in assign:
                return self.canAssign(assign, domains, i, w+1, addOne)
            else:
                for val in domains[self.words[w][i]]:
                    newAssign = deepcopy(assign)
                    newAssign[self.words[w][i]] = val
                    newDomains = self.forwardChecking(domains, self.words[w][i], val)
                    if newDomains:
                        res = self.canAssign(newAssign, newDomains, i, w+1, addOne)
                        if res:
                            return True
                # assign.pop(self.words[w][i])
                return False
            return False
        return False
    
    def forwardChecking(self, domains, char, num):
        newDomains = deepcopy(domains)
        newDomains[char] = set([num])
        changed = True
        while changed:
            for c in newDomains:
                if c == char:
                    continue
                try:
                    newDomains[c].remove(num)
                    if len(newDomains[c]) == 1:
                        char = c
                        num = list(newDomains[c])[0]
                        changed = True
                except:
                    changed = False
                if len(newDomains[c]) == 0:
                    return None
        return newDomains

    
print(Solution().isSolvable(["SEIS","CATORCE","SETENTA"], "NOVENTA"))