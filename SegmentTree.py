

class SegmentTreeNode:
    def __init__(self, l, r):
        self.l, self.r = l, r
        self.left, self.right = None, None
        self.sum = 0

class SegmentTree:
    def __init__(self, arr):
        self.root = self.construct(arr, 0, len(arr)-1)

    def inorder(self, root):
        if not root:
            return
        self.inorder(root.left)
        print(root.l, root.r, root.sum)
        self.inorder(root.right)

    def construct(self, arr, l, r):
        if l == r:
            node = SegmentTreeNode(l, r)
            node.sum = arr[l]
            return node

        mid = (l+r)//2
        node = SegmentTreeNode(l, r)
        node.left = self.construct(arr, l, mid)
        node.right = self.construct(arr, mid+1, r)

        node.sum = node.left.sum + node.right.sum
        return node

    def update(self, idx, val):
        return self._update(self.root, idx, val)

    def _update(self, node, idx, val):
        if node.l == node.r:
            node.val = val
            return node
        mid = (node.l+node.r)//2

        if idx <= mid:
            node.left = self.update(node.left, idx, val)
        else:
            node.right = self.update(node.right, idx, val)

        node.sum = node.left.sum + node.right.sum
        return node

    def getSum(self, l, r):
        return self._getSum(self.root, l, r)

    def _getSum(self, root, l, r):
        if l <= root.l and r >= root.r:
            return root.sum
        elif l < root.l or r > root.r:
            return 0
        else:
            return self._getSum(root.left, l, r) + 
            self._getSum(root.right, l, r)


s = SegmentTree([1, 2, 3, 4, 5])
# s.inorder(s.root)
print(s.getSum(0, 4))
