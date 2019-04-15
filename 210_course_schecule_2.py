class Solution:
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        order = list()
        courses = set(range(numCourses))
        while courses:
            pre = set([p[1] for p in prerequisites])
            last = courses - pre
            if not last:
                return []
            order += list(last)
            courses = courses - last
            prerequisites = [p for p in filter(lambda x: x[0] not in last, prerequisites)]
        order += list(courses)
        return order[::-1]


numCourse = 7
prerequisites = [[1,0],[0,3],[0,2],[3,2],[2,5],[4,5],[5,6],[2,4]]

print(Solution().findOrder(numCourse, prerequisites))