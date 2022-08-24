
def merge_interval(intervals):
    intervals = sorted(intervals, key=lambda x: x[0])

    res = []
    for s, e in intervals:
        if not res:
            res.append([s, e])
            continue
        if s <= res[-1][1]:
            res[-1][1] = max(res[-1][1], e)
            continue
        res.append([s, e])
    return res


intervals = [[1, 3], [2, 7], [9, 11], [2, 4], [10, 14], [-1, 2]]
print(merge_interval(intervals))
