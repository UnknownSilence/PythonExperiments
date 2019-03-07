
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

# call functions
testArray = [54, 26, 93, 17, 77, 31, 44, 55, 20]
quickSort(testArray)
print(testArray)
