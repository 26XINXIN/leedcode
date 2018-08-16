class Solution:
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        pre = dict()
        for course, prereq in prerequisites:
            pre[course] = prereq
        
        for course in pre.keys():
            if course not in pre:
                continue
            pre_chain = set()
            pre_chain.add(course)
            c = pre[course]
            while c in pre and c not in pre_chain:
                pre_chain.add(c)
                c = pre[c]
            if c in pre_chain:
                return False
        return True
                