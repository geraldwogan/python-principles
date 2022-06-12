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

from calendar import c
import enum
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

def only_ints(int_1, int_2):
    return type(int_1) == int and type(int_2) == int

print(only_ints(1, True))

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
    return ".".join(string_in)

print(add_dots('test'))

def remove_dots(string_in):
    return string_in.replace('.','')

print(remove_dots('t.e.s.t'))

print(remove_dots(add_dots('test')))

########################################################
#### Counting Syllables (3/10) ####
# https://pythonprinciples.com/challenges/Counting-syllables/

# Define a function named count that takes a single parameter. The parameter is a string. The string will contain a single word divided into syllables by hyphens, such as these:

# "ho-tel"
# "cat"
# "met-a-phor"
# "ter-min-a-tor"

# Your function should count the number of syllables and return it.

# For example, the call count("ho-tel") should return 2.

def count(string_in):
    return string_in.count('-') + 1

print(count('ho-tel'))

########################################################
#### Anagrams (3/10) ####
# https://pythonprinciples.com/challenges/Anagrams/

# Two strings are anagrams if you can make one from the other by rearranging the letters.

# Write a function named is_anagram that takes two strings as its parameters. Your function should return True if the strings are anagrams, and False otherwise.

# For example, the call is_anagram("typhoon", "opython") should return True while the call is_anagram("Alice", "Bob") should return False.

def is_anagram(str_1, str_2):
    return sorted(str_1) == sorted(str_2)

print(is_anagram("typhoon", "opython"))
print(is_anagram('test', 'tess'))

########################################################
#### Flatten a List (3/10) ####
# https://pythonprinciples.com/challenges/Flatten-a-list/

# Write a function that takes a list of lists and flattens it into a one-dimensional list.

# Name your function flatten. It should take a single parameter and return a list.

# For example, calling: flatten([[1, 2], [3, 4]])

# Should return the list: [1, 2, 3, 4]

def flatten(list_in):
    return [item for inner_list in list_in for item in inner_list]

print(flatten([[1, 2], [3, 4]]))

########################################################
#### Min-maxing (3/10) ####
# https://pythonprinciples.com/challenges/Minmaxing/

# Define a function named largest_difference that takes a list of numbers as its only parameter.

# Your function should compute and return the difference between the largest and smallest number in the list.

# For example, the call largest_difference([1, 2, 3]) should return 2 because 3 - 1 is 2.

# You may assume that no numbers are smaller or larger than -100 and 100.

def largest_difference(list_in):
    return max(list_in) - min(list_in)

print(largest_difference([-1, 2, -3]))

########################################################
#### Divisible by 3 (3/10) ####
# https://pythonprinciples.com/challenges/Divisible-by-3/

# Define a function named div_3 that returns True if its single integer parameter is divisible by 3 and False otherwise.

# For example, div_3(6) is True because 6/3 does not leave any remainder. However div_3(5) is False because 5/3 leaves 2 as a remainder.

def div_3(int_in):
    return int_in % 3 == 0 

print(div_3(6))

########################################################
#### Tic tac toe input (4/10) ####
# https://pythonprinciples.com/challenges/Tic-tac-toe-input/

# Here's the backstory for this challenge: imagine you're writing a tic-tac-toe game, where the board looks like this:

# 1|  X | O | X
#  | -----------
# 2|    |   |  
#  | -----------
# 3|  O |   |
#  |____________
#     A   B   C

# The board is represented as a 2D list:

# board = [
#     ["X", "O", "X"],
#     [" ", " ", " "],
#     ["O", " ", " "],
# ]

# Imagine if your user enters "C1" and you need to see if there's an X or O in that cell on the board. To do so, you need to translate from the string "C1" to row 0 and column 2 so that you can check board[row][column].

# Your task is to write a function that can translate from strings of length 2 to a tuple (row, column). Name your function get_row_col; it should take a single parameter which is a string of length 2 consisting of an uppercase letter and a digit.

# For example, calling get_row_col("A3") should return the tuple (2, 0) because A3 corresponds to the row at index 2 and column at index 0in the board.

def get_row_col(string_in):
    return (int(string_in[-1])-1, int(chr(ord(string_in[0])-17)) )
    
print(get_row_col("A2"))
print(get_row_col("B3"))
print(get_row_col("C1"))

########################################################
#### Palindrome (4/10) ####
# https://pythonprinciples.com/challenges/Palindrome/

# A string is a palindrome when it is the same when read backwards.

# For example, the string "bob" is a palindrome. So is "abba". But the string "abcd" is not a palindrome, because "abcd" != "dcba".

# Write a function named palindrome that takes a single string as its parameter. Your function should return True if the string is a palindrome, and False otherwise.

def palindrome(string_in):
    return string_in == string_in[::-1] # reverse the string

print(palindrome('abba'))
print(palindrome('bob'))
print(palindrome('abcd'))

########################################################
#### Up and Down (4/10) ####
# https://pythonprinciples.com/challenges/Up-and-down/

# Define a function named up_down that takes a single number as its parameter. Your function should return a tuple containing two numbers; the first should be one lower than the parameter, and the second should be one higher.

# For example, calling up_down(5) should return (4, 6).

def up_down(int_in):
    return (int_in-1, int_in+1)

print(up_down(5))

########################################################
#### Consecutive zeros (4/10) ####
# https://pythonprinciples.com/challenges/Consecutive-zeros/

# The goal of this challenge is to analyze a binary string consisting of only zeros and ones. Your code should find the biggest number of consecutive zeros in the string. For example, given the string:

# "1001101000110"

# The biggest number of consecutive zeros is 3.

# Define a function named consecutive_zeros that takes a single parameter, which is the string of zeros and ones. Your function should return the number described above.

def consecutive_zeros(string_in):
    return max([len(s) for s in string_in.split('1')])

print(consecutive_zeros("1001101000110"))

########################################################
#### All Equal (4/10) ####
# https://pythonprinciples.com/challenges/All-equal/

# Define a function named all_equal that takes a list and checks whether all elements in the list are the same.

# For example, calling all_equal([1, 1, 1]) should return True.

def all_equal(list_in):
    return len(set(list_in)) <= 1

print(all_equal([1,1,1]))
print(all_equal([1,2,1]))

########################################################
#### Boolean and (4/10) ####
# https://pythonprinciples.com/challenges/Boolean-and/

# Define a function named triple_and that takes three parameters and returns True only if they are all True and False otherwise.

def triple_and(bool_1, bool_2, bool_3):
    return all([bool_1, bool_2, bool_3])
    # this also works:
    # return bool_1 and bool_2 and bool_3

print(triple_and(True, True, True))
print(triple_and(True, True, False))


