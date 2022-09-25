from argparse import ArgumentError


class DSU:
    def __init__(self, n):
        self.n = n
        self.sz = n
        self.groups = [i for i in range(n)]
        self.ranks = [1 for _ in range(n)]

    def find(self, a):
        if a < 0 or a >= self.n:
            raise IndexError(
                "You're tryna look up a value that's not in the DSU set")
        if self.groups[a] != a:
            self.groups[a] = self.find(self.groups[a])
        return a

    def getNumberGroups(self):
        return self.sz

    def union(self, a, b):
        root_a, root_b = self.find(a), self.find(b)
        if root_a != root_b:
            self.count -= 1

        if self.ranks[root_a] > self.ranks[root_b]:
            self.groups[root_b] = root_a
        else:
            self.groups[root_a] = root_b
            if self.ranks[root_a] == self.ranks[root_b]:
                self.ranks[root_b] += 1


class DSUAdd:
    def __init__(self):
        self.groups = {}
        self.weights = {}
        self.sz = 0

    def add(self, p):
        hashed_p = p
        self.groups[hashed_p] = hashed_p
        self.weights[hashed_p] = 1
        self.sz += 1

    def find(self, p):
        hashed_p = p
        if self.groups[hashed_p] != hashed_p:
            self.groups[hashed_p] = self.find(self.groups[hashed_p])
        return hashed_p

    def union(self, p, q):
        root_p = self.find(self.groups[p])
        root_q = self.find(self.groups[p])

        if root_p == root_q:
            return

        if self.weights[root_q] > self.weights[root_p]:
            self.groups[root_p] = root_q
        else:
            self.groups[root_q] = root_p
            if self.weights[root_q] == self.weights[root_p]:
                self.weights[root_p] += 1
        self.sz -= 1


dsu = DSUAdd()
dsu.add((1, 1))
dsu.add((2, 2))
print(dsu.groups)
# dsu.union((1, 1), (2, 2))

print(dsu.sz)
