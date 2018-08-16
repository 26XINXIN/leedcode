class Solution:
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        n = len(dungeon)
        if n == 0:
            return 0
        m = len(dungeon[0])
        hp = list()
        for _ in range(n):
            hp.append([0] * m)

        hp[n-1][m-1] = max(1 - dungeon[n-1][m-1], 1)

        for i in range(n-2, -1, -1):
            hp[i][m-1] = max(hp[i+1][m-1] - dungeon[i][m-1], 1)
        for j in range(m-2, -1, -1):
            hp[n-1][j] = max(hp[n-1][j+1] - dungeon[n-1][j], 1)
        
        for i in range(n-2, -1, -1):
            for j in range(m-2, -1, -1):
                hp[i][j] = max(min(hp[i+1][j], hp[i][j+1]) - dungeon[i][j], 1)
        return hp[0][0]
                