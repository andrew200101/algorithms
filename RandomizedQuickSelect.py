"""
This function takes in an unsorted array and finds the median in O(N) time

Naive approach: Sort the array which takes O(nlogn) time using quicksort, then getting median. 
Optimized approach: Partition array around random pivot where all values to left of pivot is < pivot and vice versa. 


"""


def MedianQuickSelect(l):
