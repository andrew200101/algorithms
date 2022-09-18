class Node:
    def __init__(self, val, left=None, right=None, parent=None):
        self.val = val
        self.left = left
        self.right = right
        self.height = 0


class AVL:
    def __init__(self, root=None):
        pass

    def insert(self, root, val):
        if not root:
            return Node(val)
        elif val <= root.val:
            root.left = self.insert(root.left, val)
        else:
            root.right = self.insert(root.right, val)

        self.height = 1 + max(self.get_height(root.left),
                              self.get_height(root.right))

        balance = self.get_balance(root)

        if balance > 1 and self.get_balance(root.left) > 0:
            return self.rightRotate(root)

        elif balance > 1 and self.get_balance(root.left) < 0:
            self.leftRotate(root.left)
            return self.rightRotate(root)

        elif balance < -1 and self.get_balance(root.right) > 0:
            self.rightRotate(root.right)
            return self.leftRotate(root)

        elif balance < -1 and self.get_balance(root.right) < 0:
            return self.leftRotate(root)

        return root

    def leftRotate(self, root):

        pivot = root.right
        transfer_child = pivot.left

        # Perform rotation
        pivot.left = root
        root.right = transfer_child

        # Update heights
        root.height = 1 + max(self.getHeight(root.left),
                              self.getHeight(root.right))
        pivot.height = 1 + max(self.getHeight(pivot.left),
                               self.getHeight(pivot.right))

        return pivot

    def rightRotate(self, root):

        pivot = root.left
        transfer_child = pivot.right

        # Perform rotation
        pivot.right = root
        root.left = transfer_child

        # Update heights
        root.height = 1 + max(self.getHeight(root.left),
                              self.getHeight(root.right))
        pivot.height = 1 + max(self.getHeight(pivot.left),
                               self.getHeight(pivot.right))

        # Return the new root
        return pivot

    def get_height(self, root):
        if not root:
            return 0
        return root.height

    def get_balance(self, root):
        return self.get_height(root.left)-self.get_height(root.right)

    def preOrder(self, root):

        if not root:
            return

        print(root.val)
        self.preOrder(root.left)
        self.preOrder(root.right)


AVLTree = AVL()
root = Node(4)
AVLTree.insert(root, 5)
AVLTree.insert(root, 10)
AVLTree.insert(root, 11)
AVLTree.insert(root, 12)
AVLTree.insert(root, 13)


AVLTree.preOrder(root)
