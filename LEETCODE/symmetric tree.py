'''Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

 

Example 1:


Input: root = [1,2,2,3,4,4,3]
Output: true'''

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return true
        return self.isSame(root.left, root.right)

    def isSame(self, leftroot, rightroot):

        if leftroot == None and rightroot == None:
            return True

        if leftroot == None or rightroot == None:
            return False

        if leftroot.val != rightroot.val:
            return False

        return self.isSame(leftroot.left, rightroot.right) and self.isSame(leftroot.right, rightroot.left)