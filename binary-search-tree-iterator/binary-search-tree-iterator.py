# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = []
        self.partialTraversal(root)
        
    def partialTraversal(self, node):
        while node:
            self.stack.append(node)
            node=node.left
            
    def next(self):
        """
        :rtype: int
        """
        nxt = self.stack.pop()
        self.partialTraversal(nxt.right)
        return nxt.val
    
    def hasNext(self):
        """
        :rtype: bool
        """
        return True if self.stack else False


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()