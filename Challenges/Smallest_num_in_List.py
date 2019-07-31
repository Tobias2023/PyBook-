# Author: Tobias Scott
# Website:  https://tobiascscott.com/
# https://www.hackerrank.com/t_cscott2023
# https://edabit.com/user/hQGgHwFhPE6fCkn8P

# Challenge: Create a function that takes a list of numbers and returns the smallest number in the list.

def findSmallestNum(my_list):
    entire_list = my_list[0]
    for i in my_list:
        if i < entire_list:
            entire_list = i
    return entire_list
        
