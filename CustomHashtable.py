
import unittest
from distutils.log import error


class LinkNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class Hashmap:
    def __init__(self, k):
        self.store = [False for _ in range(k)]
        self.k = k

    def get_hash(self, s):
        return hash(s) % self.k

    def put(self, k, v):
        h = self.get_hash(k)
        if not self.store[h]:
            self.store[h] = LinkNode((k, v))
        else:
            self.store[h] = self.search(self.store[h], k, v)

    def get(self, k):
        h = self.get_hash(k)
        if not self.store[h]:
            return "Can't find what you're looking for"

        head = self.store[h]
        while head:
            if head.val[0] == k:
                return head.val[1]
            head = head.next

        return "Can't find what you're looking for"

    def search(self, node, k, v):
        if not node:
            return LinkNode((k, v))
        if node.val[0] == k:
            return LinkNode((k, v), node.next)

        return LinkNode(node.val, self.search(node.next, k, v))

    def visualize(self):
        for i in range(len(self.store)):
            print(str(i) + ": " + str(self.print_linked_nodes(self.store[i])))

    def print_linked_nodes(self, n):
        res = []
        while n:
            res.append(n.val)
            n = n.next
        return res

    # def get(self, k):


H = Hashmap(3)
H.put("Andrew", "H: 173, W: 130")
H.put("Bianca", "H: 163, W: 120")
H.put("Andy", "H: 183, W: 151")
H.put("Alfred", "H: 190, W: 151")
H.put("Bee", "H: 171, W: 151")

assert H.get("Bianca") == "H: 163, W: 120", "Wrong Answer"
print("Put function works")
