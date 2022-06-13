from Testing import Test


class Sort:
    def __init__(self):
        pass

    """Returns a sorted list
    :param l: a list of comparable objects
    :returns l: the list in sorted order 
    """

    def quicksort(self, l):
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

            temp = l[i]
            l[i] = l[j]
            l[j] = temp

            if l[i] == pivot:
                break
            i += 1
        left = self.quicksort(l[:i])
        right = self.quicksort(l[i+1:])

        return left + [pivot] + right

    def mergesort(self, l):
        n = len(l)
        middle_idx = (n+1)//2

        if n <= 1:
            return l

        left = self.mergesort(l[:middle_idx])
        right = self.mergesort(l[middle_idx:])
        l_n, r_n = len(left), len(right)

        l_ptr, r_ptr = 0, 0

        res = []

        while l_ptr != l_n or r_ptr != r_n:
            if l_ptr == l_n:
                res.append(right[r_ptr])
                r_ptr += 1
            elif r_ptr == r_n:
                res.append(left[l_ptr])
                l_ptr += 1
            else:
                if right[r_ptr] >= left[l_ptr]:
                    res.append(left[l_ptr])
                    l_ptr += 1
                else:
                    res.append(right[r_ptr])
                    r_ptr += 1
        return res


sort = Sort()
test = Test()
print(test.time(sort.mergesort, [1, 2, 3, 4, 55, 6, 7, 7, 2, 3]))
print(test.time(sort.quicksort, [1, 2, 3, 4, 55, 6, 7, 7, 2, 3]))
