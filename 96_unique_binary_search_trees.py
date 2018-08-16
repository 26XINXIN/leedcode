class Solution:
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        tree_num = [0] * (n + 1)
        tree_num[1] = 1
        tree_num[2] = 2
        for i in range(3, n + 1):
            tree_num[i] += 2 * tree_num[i-1]
            for x in range(1, i):
                tree_num[i] += tree_num[x-1] * tree_num[i-x]
        return tree_num[n]