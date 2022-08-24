from argparse import ArgumentError


class DSU:
    def __init__(self, n):
        self.n = n
        self.groups = [i for i in range(n)]
        self.ranks = [1 for _ in range(n)]

    def find(self, a):
        if a < 0 or a >= self.n:
            raise IndexError(
                "You're tryna look up a value that's not in the DSU set")
        if self.groups[a] != a:
            self.groups[a] = self.find(self.groups[a])
        return a

    def getSize(self, a):
        res = 0
        root_a = self.find(a)
        for i in range(self.n):
            if self.find(i) == root_a:
                print(i)
                res += self.ranks[i]
        return res

    def union(self, a, b):
        root_a, root_b = self.find(a), self.find(b)
        if self.ranks[root_a] > self.ranks[root_b]:
            self.groups[root_b] = root_a
        else:
            self.groups[root_a] = root_b
            if self.ranks[root_a] == self.ranks[root_b]:
                self.ranks[root_b] += 1


dsu = DSU(7)
dsu.union(2, 5)
dsu.union(4, 2)
dsu.union(2, 1)
print(dsu.getSize(5))
print((dsu.find(4) == dsu.find(4)))


class DSU:
    def __init__(self, n):
        self.n = n
        self.groups = [i for i in range(n)]
        self.ranks = [1 for _ in range(n)]

    def find(self, a):
        if self.groups[a] != a:
            self.groups[a] = self.find(self.groups[a])
        return self.groups[a]

    def union(self, a, b):
        root_a, root_b = self.find(a), self.find(b)

        if self.ranks[root_a] > self.ranks[root_b]:
            self.groups[root_b] = root_a
        else:
            self.groups[root_a] = root_b
            if self.ranks[root_a] == self.ranks[root_b]:
                self.ranks[root_b] += 1

    def getSize(self, a):
        counter = 0
        for i in range(self.n):
            if self.find(i) == self.find(a):
                counter += 1
        return counter
