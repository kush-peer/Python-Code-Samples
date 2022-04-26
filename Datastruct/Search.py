
from unicodedata import name
from Util.TimeDecorator import time_it

@time_it
def linear_search(numbers_list, number_to_find):
    for index, element in enumerate(numbers_list):
        if element == number_to_find:
            return index
           
@time_it
def binary_search(numbers_list, number_to_find):
    left_index = 0;
    right_index = len(numbers_list) - 1

    while left_index <= right_index:

        mid_index = (left_index + right_index) // 2
       
        # If number is greater, ignore left half 
        if numbers_list[mid_index] < number_to_find:
                left_index = mid_index + 1

         # If number is less, ignore right half 
        elif numbers_list[mid_index] > number_to_find:
                right_index = mid_index - 1

        # If means number is present
        else:
            return mid_index;
   

if __name__ == "__main__":
    numbers_list = [i for i in range(1000000)]
    number_to_find = 100000

    result = linear_search(numbers_list, number_to_find)
    result1 = binary_search(numbers_list, number_to_find)
    if result != -1:
        print("Found at index: ", result)
    else:
        print("Not Found")
    
    if result1 != -1:
            print("Found at index: ", result1)
    else:
        print("Not Found")
    