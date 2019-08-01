# Author: Tobias Scott
# Website:  https://tobiascscott.com/
# https://www.hackerrank.com/t_cscott2023
# https://edabit.com/user/hQGgHwFhPE6fCkn8P

# Challenge: Create a function that takes in a word and determines whether or not it is plural. A plural word is one that ends in "s".

def is_plural(word):
    the_word = word.endswith("s")
    return the_word
