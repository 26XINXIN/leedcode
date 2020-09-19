class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        return self._canTransform(start, end) or self._canTransform(end, start)

    def _canTransform(self, start: str, end: str) -> bool:
        if len(start) != len(end):
            return False
        
        i = j = 0
        while i < len(start) and j < len(end):
            while i < len(start) and start[i] == 'X':
                i += 1
            while j < len(end) and end[j] == 'X':
                j += 1
            
            if (i == len(start) and j < len(end)) or (i < len(start) and j == len(end)):
                return False
            if i < len(start) and j < len(end):
                if start[i] != end[j]:
                    return False
                if start[i] == 'L' and i < j:
                    return False
                if start[i] == 'R' and i > j:
                    return False
            
            i += 1
            j += 1
        
        if (i >= len(start) and j < len(end)) or (i < len(start) and j >= len(end)):
            return False
        return True