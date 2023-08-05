from typing import List
from timeit import timeit

def buble_sort(array: List[int])-> List[int]:
    n = len(array)

    for i in range(n):
        # Create a flag that will allow the function to 
        # terminate early if there's nothing left to sort
        already_sorted = True 

        # Start looking at each item of the list one by one,
        # comparing it with its adjacent value. With each iteration,
        # the portion of the array that you look at shrinks because the
        # remaining items have already been sorted

        for j in range(n-i-1):
            if array[j] > array[j+1]:
                # If the item you are looking at is greater than its 
                # adjacent  value, then swap them
                array[j], array[j+1] = array[j+1],array[j]

                # Since you had to swap two elements set the already
                # sorted flag to False so the algorithm doesn't finish
                # permanently
                already_sorted = False 

        # If there were no swap during the last iteration, the array
        # is already sorted and you can terminate
        if already_sorted:
            break

    return array

if __name__ == "__main__":
    input_list = [3, 19, 4, 0, 77, 90, 18, 25, 103]

    execution_time = timeit(stmt=lambda: buble_sort(input_list),number=1)

    print("Sorted List: ",buble_sort(input_list))
    print("Time taken: ", execution_time, "seconds")









