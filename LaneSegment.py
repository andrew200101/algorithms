
import collections


def findslope(a, b):
    return (a[1] - b[1]) / (a[0] - b[0])


def laneSeg(input):
    seg_by_slope = collections.defaultdict(list)

    for s in input:
        slope = findslope(s[0], s[1])
        """
        Once we group the segments by slope, we can compress the (x,y) coordinates into simply 1-D
        """
        seg_by_slope[slope].append([s[0][0], s[-1][0]])

    for k in seg_by_slope:
        seg_by_slope[k] = sorted(seg_by_slope[k])

    """
    seg_by_slope:

    {
        1.0: [[1, 3], [2, 4], [2, 4], [3, 4], [3, 5], [5, 8], [7, 8], [10, 11]],
        2.0: [[1, 2]]
    }
    """

    # This function merges the segments, which you can think of as 'intervals'
    for k in seg_by_slope:
        curr_segs = seg_by_slope[k]
        merged_seg = [curr_segs.pop(0)]

        for interval in curr_segs:
            if merged_seg[-1][0] <= interval[0] and interval[0] <= merged_seg[-1][1]:
                merged_seg[-1][1] = max(merged_seg[-1][1], interval[1])
            else:
                merged_seg.append(interval)

        seg_by_slope[k] = merged_seg

    # print(seg_by_slope)
    """
    seg_by_slope:

    {
        1.0: [[1, 8], [10, 11]],
        2.0: [[1, 2]]
    }
    """

    # And finally just return all the points
    res = []
    for k in seg_by_slope:
        v = seg_by_slope[k]
        for seg in v:
            curr_seg = []
            for x in range(seg[0], seg[1]+1):
                # To get the appropriate y from x given slope m, we just do m*x
                curr_seg.append([x, int(x*k)])
            res.append(curr_seg)
    return res


lanes = [
    [[1, 1], [2, 2]],
    [[1, 1], [7, 7]]
]
print(laneSeg(lanes))
