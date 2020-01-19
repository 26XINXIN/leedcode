class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        dest = {}
        # self.cities = set()
        for from_, to in tickets:
            # self.cities.add(from_)
            # self.cities.add(to)
            if from_ not in dest:
                dest[from_] = [to]
            else:
                dest[from_].append(to)
        
        for from_ in dest:
            dest[from_].sort()
        
        res = ['JFK']
        self.search(res, dest)
        return res
    
    def search(self, res, dest):
        # print(res)
        # print(dest)
        if all(not tic for tic in dest.values()):
            return True
        from_ = res[-1]
        if from_ not in dest or not dest[from_]:
            return False
        for i in range(len(dest[from_])):
            to = dest[from_].pop(i)
            res.append(to)
            if self.search(res, dest):
                return True
            dest[from_].insert(i, to)
            res.pop()
        return False
        
            
        
