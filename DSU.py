from argparse import ArgumentError


class DSU:
    def __init__(self):
        self.groups = {}
        self.size = {}
        self.ranks = {}

    def find(self, a):
        if a not in self.groups:
            self.groups[a] = a
            self.size[a] = 1
            self.ranks[a] = 1

        if self.groups[a] != a:
            self.groups[a] = self.find(self.groups[a])
            self.size[a] = 1

        return self.groups[a]

    def union(self, a, b):
        root_a, root_b = self.find(a), self.find(b)
        if self.ranks[root_a] > self.ranks[root_b]:
            self.groups[root_b] = root_a
            self.size[root_a] += self.size[root_b]
        else:
            if self.ranks[root_a] == self.ranks[root_b]:
                self.ranks[root_b] += 1
            self.groups[root_a] = root_b
            self.size[root_b] += self.size[root_a]


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
