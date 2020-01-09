# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def closestKValues(self, root: TreeNode, target: float, k: int) -> List[int]:
        node = root
        predecessor, successor = list(), list()
        while node:
            if node.val == target:
                predecessor = [node.val] + self.getPredecessor(node.left) + predecessor
                successor = self.getSuccessor(node.right) + successor
                break
            elif target < node.val:
                successor = [node.val] + self.getSuccessor(node.right) + successor
                node = node.left
            else:
                predecessor = [node.val] + self.getPredecessor(node.left) + predecessor
                node = node.right
        
        print(predecessor)
        print(successor)

        nearest = list()
        i, j = 0, 0
        while len(nearest) < k and i < len(predecessor) and j < len(successor):
            if target - predecessor[i] < successor[j] - target:
                nearest.append(predecessor[i])
                i += 1
            else:
                nearest.append(successor[j])
                j += 1
        if len(nearest) == k:
            return nearest
        while len(nearest) < k and i < len(predecessor):
            nearest.append(predecessor[i])
            i += 1
        while len(nearest) < k and j < len(successor):
            nearest.append(successor[j])
            j += 1
        return nearest
    
    def getPredecessor(self, node):
        if node is None:
            return []
        return self.getPredecessor(node.right) + [node.val] + self.getPredecessor(node.left)

    def getSuccessor(self, node):
        if node is None:
            return []
        return self.getSuccessor(node.left) + [node.val] + self.getSuccessor(node.right)
        
        