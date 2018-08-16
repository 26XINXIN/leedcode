class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        result = dict()
        for s in strs:
            inserted = False
            for k in result.keys:
                if self.equal(k, s):
                    result[k].append(s)
                    inserted = True
                    break
            if not inserted
                count = dict()
                for c in s:
                    if c not in count:
                        count[c] = 1
                    else:
                        count[c] += 1
                result[count] = [s]
        return result.values()
    
    def equal(self, k, s2):
        count2 = dict()
        for c in s2:
            if c not in count2:
                count2[c] = 1
            else:
                count2[c] += 1
        if k == count2:
            return True
        else:
            return False