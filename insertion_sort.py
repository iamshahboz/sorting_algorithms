from typing import List
from timeit import timeit 

def insertion_sort(array: List[int])-> List[int]:
    # Loop from the second element of the array until
    # the last element 
    for i in range(1, len(array)):
        # This is the element we want to position in its correct place
        key_item = array[i]

        # Initialize the variable that will be used to find the correct 
        # position of the element referenced by 'key_item' 

        j = i -1 

        # Run through the list of items (the left portion of the array)
        # and find the correct position of the element referenced by the 'key_item'
        # Do this only if key_item is smaller than its adjacent values.
        while j >= 0 and array[j] > key_item:
            # Shift the value one position to the left and reposition j to
            # point to the next element (from right to left)
            array[j+1] = array[j]
            j -= 1 
        # When you finish shifting the elements, you can position 'key_item'
        # in its correct location
        array[j+1] = key_item
    return array 


if __name__ == "__main__":
    input_list = [1, 20, 15, 44, 103, -7, -12, 39, 74, 86, 0]

    execution_time = timeit(stmt=lambda: insertion_sort(input_list),number=1)

    print("Sorted List: ",insertion_sort(input_list))
    print("Time taken: ", execution_time, "seconds")




