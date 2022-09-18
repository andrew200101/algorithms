
res = []
a_1 = 3
for i in range(20):
    a_1 = (3*a_1 - 2) % 7
    res.append(a_1)

print(res)
