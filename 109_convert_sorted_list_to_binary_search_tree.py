# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if head == None:
            return None
        l = list()
        it = head
        while it:
            l.append(it.val)
            it = it.next
        return self.sortedArrayToBST(l)

    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if len(nums) == 0:
            return None

        l = len(nums)
        idx = l // 2
        root = TreeNode(nums[idx])
        if idx != 0:
            root.left = self.sortedArrayToBST(nums[:idx])
        if idx != l - 1:
            root.right = self.sortedArrayToBST(nums[idx+1:])
        return root
