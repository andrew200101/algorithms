def min_max_sliding_window(arr, k):

    dq = []
    for i in range(k):
        while dq and dq[-1] < arr[i]:
            dq.pop(-1)
        dq.append(arr[i])

        l, r = 0, k-1
        print(dq[0])
        while r < len(arr):
            r += 1
            while dq and dq[-1] < arr[r]:
                dq.pop(-1)
            dq.append(arr[r])
            lose = arr[l]
            if dq[0] == lose:
                dq.pop(0)
            l += 1
            print(dq[0])

    return


arry = [3, 4, 5, 6, 7, 1, 3, 5, 23, 2, 9, 3,
        3, 3, 5, 5, 2, 8, 11, 34, 23, 34, 2, 2]

min_max_sliding_window(arry, 4)
