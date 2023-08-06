from random import randint
from typing import List 
from timeit import timeit 

def quicksort(array: List[int])-> List[int]:
    ...
    # If the input array contains fewer than two elements,
    # then return it as the result of the function
    if len(array) < 2:
        return array 
    
    low, same, high = [], [], []

    # Select your pivot element randomly
    pivot = array[randint(0, len(array) - 1)]

    for item in array:
        # Elements that are smaller than the pivot go to the 
        # 'low' list. Element that are larger than pivot go to the 'high' list.
        # Elements that are equal to pivot go to the 'same' list.

        if item < pivot:
            low.append(item)
        elif item == pivot:
            same.append(item)
        elif item > pivot:
            high.append(item)

    # The final result combines the sorted 'low' list 
    # with the 'same' list and the sorted 'high' list 
    return quicksort(low) + same + quicksort(high)

if __name__ == "__main__":
    input_list = [400, -48, 133, 91, 18, 22, -5, -88]

    execution_time = timeit(stmt=lambda: quicksort(input_list),number=1)

    print("Sorted List: ",quicksort(input_list))
    print("Time taken: ", execution_time, "seconds")