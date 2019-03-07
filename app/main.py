import random

###########################################################
#       Quick-Sort Algorithm in Python
###########################################################
#       Runtime: O(n log n)
###########################################################
#       Author: Trent Hardy
###########################################################

# sorting call function


def quickSort(unsortedArray):
    sorter(unsortedArray, 0, len(unsortedArray)-1)
# recursive sorter function


def sorter(unsortedArray, first, last):
    if first < last:
        split = partition(unsortedArray, first, last)
        sorter(unsortedArray, first, split - 1)
        sorter(unsortedArray, split + 1, last)
# partioning array function.


def partition(unsortedArray, first, last):
    pivotvalue = unsortedArray[first]
    left = first+1
    right = last
    completed = False
    while not completed:
        while left <= right and unsortedArray[left] <= pivotvalue:
            left = left + 1
        while unsortedArray[right] >= pivotvalue and right >= left:
            right = right - 1
        if right < left:
            completed = True
        else:
            temp = unsortedArray[left]
            unsortedArray[left] = unsortedArray[right]
            unsortedArray[right] = temp
    temp = unsortedArray[first]
    unsortedArray[first] = unsortedArray[right]
    unsortedArray[right] = temp
    return right


# call my functions
testArray = [1, 4, 92, 103.3, 6, 8, 9.5, 11, 23.5, 900, 120, 5, 1, 2]
quickSort(testArray)
print("Quick Sort:")
print(testArray)


###########################################################
#       Binary Search Tree Algorithm
###########################################################
#       Runtime: O(log n)
###########################################################
#       Author: Trent Hardy
###########################################################

def binSearch(unsortedArray, point):
    if len(unsortedArray) == 0:
        return False
    else:
        midpoint = len(unsortedArray)//2
        if unsortedArray[midpoint] == point:
            return True
        else:
            if point < unsortedArray[midpoint]:
                return binSearch(unsortedArray[:midpoint], point)
            else:
                return binSearch(unsortedArray[midpoint+1:], point)


testArray2 = [90, 5.5, 5.3, 2.9, 8.4, 2.3, 999, 0, 12, 13, 99.3,
              254, 23232, 2323121, 32324, 32321212, 323121445, 32323239]
print("Binary Search:")
# point identifies the target item
print(binSearch(testArray2, 12))
print(binSearch(testArray2, 2))
