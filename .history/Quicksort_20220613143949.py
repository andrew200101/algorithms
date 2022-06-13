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

        if i == n or j >= n:
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


print(quicksort([2, 1]))
