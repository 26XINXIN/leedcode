class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        groups = dict()
        for s in strings:
            intervals = tuple((ord(s[i + 1]) - ord(s[i])) % 26 for i in range(len(s)-1))
            groups[intervals] = groups.get(intervals, list()) + [s]
        return list(groups.values())