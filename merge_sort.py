from timeit import timeit 
from typing import List

def merge(left: List[int], right: List[int]):
    # If the first array is empty, then nothing needs 
    # to be merged and you can return the second array as the 
    # result 

    if len(left) == 0:
        return right
    
    # If the second array is empty then nothing needs to be merged
    # and you can return the first array as the result 

    if len(right) == 0:
        return left 
    
    result = []
    index_left = index_right = 0

    # Now go through both arrays until all the elements 
    # make it into the resultant array

    while len(result) < len(left) + len(right):
    # The elements need to be sorted to add them to the 
    # resultant array, so you need to decide whether to get 
    # the next element from the first or the second array
        if left[index_left] <= right[index_right]:
            result.append(left[index_left])
            index_left += 1
        else:
            result.append(right[index_right])
            index_right += 1 

        # If you reach the end of either array then you can add 
        # the remaining elements from the other array to the result 
        # and break the loop
        if index_right == len(right):
            result.extend(left[index_left:])
            break 
        if index_left == len(left):
            result.extend(right[index_right:])

    return result 

left_input = [1, 33, 5, 19, 41, 0, 22, 57]
right_input = [2, 55, 17, 35, 10, 48, 33]

execution_time = timeit(lambda: merge(left_input, right_input), number=1)
result = merge(left_input, right_input)
print(f'Sorted list: {result} and the execution time is {execution_time} seconds')


