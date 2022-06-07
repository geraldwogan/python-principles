# https://pythonprinciples.com/challenges/

########################################################
#### Capital Indexes (2/10) ####
# https://pythonprinciples.com/challenges/Capital-indexes/

# Write a function named capital_indexes. The function takes a single parameter, which is a string. Your function should return a list of all the indexes in the string that have capital letters.

# For example, calling capital_indexes("HeLlO") should return the list [0, 2, 4].

def capital_indexes(string_in):
    capitals = []
    for idx, letter in enumerate(string_in):
        if letter.isupper():
            capitals.append(idx)
    return capitals

print(capital_indexes("heLIo"))

########################################################
#### Middle Letter (2/10) ####
# https://pythonprinciples.com/challenges/Middle-letter/

# Write a function named mid that takes a string as its parameter. Your function should extract and return the middle letter. If there is no middle letter, your function should return the empty string.

# For example, mid("abc") should return "b" and mid("aaaa") should return "".

def mid(string_in):
    length = len(string_in)
    if length % 2 == 0:
        return ""
    else:
        return string_in[int(length/2)] # OR string[len(string)//2]

print(mid("world"))

########################################################
#### Online Status (2/10) ####
# https://pythonprinciples.com/challenges/Online-status/

# The aim of this challenge is, given a dictionary of people's online status, to count the number of people who are online.

# For example, consider the following dictionary:

statuses = {
    "Alice": "online",
    "Bob": "offline",
    "Eve": "online",
}
# In this case, the number of people online is 2.

# Write a function named online_count that takes one parameter. The parameter is a dictionary that maps from strings of names to the string "online" or "offline", as seen above.

# Your function should return the number of people who are online.

def online_count(statuses):
    cnt = 0
    for value in statuses.values():
        print(value)
        if value == "online":
            cnt += 1
    return cnt

# OR
# def online_count(people):
#     return len([p for p in people if people[p] == "online"])

print(online_count(statuses))

########################################################
#### Randomness (2/10) ####
# https://pythonprinciples.com/challenges/Randomness/

# Define a function, random_number, that takes no parameters. The function must generate a random integer between 1 and 100, both inclusive, and return it.

# Calling the function multiple times should (usually) return different numbers.

# For example, calling random_number() some times might first return 42, then 63, then 1.

import random
from re import T

def random_number():
    return random.randint(0,100)

print(random_number())

########################################################
#### Type Check (2/10) ####
# https://pythonprinciples.com/challenges/Type-check/

# Write a function named only_ints that takes two parameters. Your function should return True if both parameters are integers, and False otherwise.

# For example, calling only_ints(1, 2) should return True, while calling only_ints("a", 1) should return False.

def only_ints(in_1, in_2):
    if isinstance(in_1, int) and isinstance(in_2, int) :
        return True
    return False

print(only_ints(1,'r'))

########################################################
#### Double Letters (3/10) ####
# https://pythonprinciples.com/challenges/Double-letters/

# The goal of this challenge is to analyze a string to check if it contains two of the same letter in a row. For example, the string "hello" has l twice in a row, while the string "nono" does not have two identical letters in a row.

# Define a function named double_letters that takes a single parameter. The parameter is a string. Your function must return True if there are two identical letters in a row in the string, and False otherwise.

def double_letters(string_in):
    for i, letter in enumerate(string_in):
        if i != 0: # Prevent 'IndexError: string index out of range'
            if string_in[i-1] is letter:
                return True
    return False

print(double_letters('hello'))

########################################################
#### Adding and Removing Dots (3/10) ####
# https://pythonprinciples.com/challenges/Adding-and-removing-dots/

# Write a function named add_dots that takes a string and adds "." in between each letter. For example, calling add_dots("test") should return the string "t.e.s.t".

# Then, below the add_dots function, write another function named remove_dots that removes all dots from a string. For example, calling remove_dots("t.e.s.t") should return "test".

# If both functions are correct, calling remove_dots(add_dots(string)) should return back the original string for any string.

# (You may assume that the input to add_dots does not itself contain any dots.)

def add_dots(string_in):
    dotted_string = ''
    for i, letter in enumerate(string_in):
        dotted_string += letter + '.'
    return dotted_string[:-1]

print(add_dots('test'))

def remove_dots(string_in):
    return string_in.replace('.','')

print(remove_dots('t.e.s.t'))

print(remove_dots(add_dots('test')))