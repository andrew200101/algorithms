"""Returns a sorted list

:param l: a list of comparable objects
:returns l: the list in sorted order 

"""


def quicksort(l):

    if len(l) <= 1:
        return l
    i, n, pivot = 0, len(l)-1, l[-1]

    while i < n:
        while l[i] <= pivot:
            i += 1
            if i == n:
                break

        j = i+1

        if i == n:
            break

        while l[j] > pivot:
            j += 1

        print(i, j)

        temp = l[i]
        l[i] = l[j]
        l[j] = temp

        if l[i] == pivot:
            break
        i += 1
    left = quicksort(l[:i])
    right = quicksort(l[i+1:])
    print(left, right)

    return left + [pivot] + right


print(quicksort([2, 1, 23, 24, 4, 23, 1, 23, 4, 5, 6, 4, 3, 5, 2, 5]))
