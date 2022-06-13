"""Returns a sorted list

:param l: a list of comparable objects
:returns l: the list in sorted order 

"""


def quicksort(l):
    print(l)
    if len(l) <= 1:
        return l
    pivot = l[-1]
    N = len(l)
    i = 0
    while i < N - 1:
        while l[i] <= pivot:
            i += 1

        j = i+1

        if j >= N:
            break

        while l[j] > pivot:
            j += 1

        temp = l[i]
        l[i] = l[j]
        l[j] = temp
        print("l: " + str(l))
        print(i, j)
        if l[i] == pivot:
            break
        i += 1

    left = quicksort(l[0: i])
    right = quicksort(l[i+1:])

    return left + [pivot] + right


print(quicksort([3, 4, 2, 1, 5, 3]))
