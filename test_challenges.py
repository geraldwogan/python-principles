import pytest
import challenges as ch

# https://pythonprinciples.com/challenges/

############################################
#### Capital Indexes (2/10) ####
# https://pythonprinciples.com/challenges/Capital-indexes/

# Write a function named capital_indexes. The function takes a single parameter, which is a string. Your function should return a list of all the indexes in the string that have capital letters.

# For example, calling capital_indexes("HeLlO") should return the list [0, 2, 4].

def test_capital_indexes():
    capitals = ch.capital_indexes("heLLo")
    assert capitals == [2,3]

############################################
#### Middle Letter (2/10) ####
# https://pythonprinciples.com/challenges/Middle-letter/

# Write a function named mid that takes a string as its parameter. Your function should extract and return the middle letter. If there is no middle letter, your function should return the empty string.

# For example, mid("abc") should return "b" and mid("aaaa") should return "".

def test_mid_odd():
    letter = ch.mid("abc")
    assert letter == 'b'

def test_mid_even():
    letter = ch.mid("abcd")
    assert letter == ''

############################################
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

def test_online_count():
    count = ch.online_count(statuses)
    assert count == 2

########################################################
#### Randomness (2/10) ####
# https://pythonprinciples.com/challenges/Randomness/

# Define a function, random_number, that takes no parameters. The function must generate a random integer between 1 and 100, both inclusive, and return it.

# Calling the function multiple times should (usually) return different numbers.

# For example, calling random_number() some times might first return 42, then 63, then 1.

def test_random_number():
    randoms = []
    for i in range(0,100):
        randoms.append(ch.random_number())
    res = all(num >= 0 and num <= 100 for num in randoms)
    assert res == True

########################################################
#### Type Check (2/10) ####
# https://pythonprinciples.com/challenges/Type-check/

# Write a function named only_ints that takes two parameters. Your function should return True if both parameters are integers, and False otherwise.

# For example, calling only_ints(1, 2) should return True, while calling only_ints("a", 1) should return False.

def test_only_ints():
    is_only_ints = ch.only_ints(1,2)
    assert is_only_ints == True
    is_only_ints = ch.only_ints(1,'2')
    assert is_only_ints == False
    is_only_ints = ch.only_ints('1',2)
    assert is_only_ints == False

########################################################
#### Double Letters (3/10) ####
# https://pythonprinciples.com/challenges/Double-letters/

# The goal of this challenge is to analyze a string to check if it contains two of the same letter in a row. For example, the string "hello" has l twice in a row, while the string "nono" does not have two identical letters in a row.

# Define a function named double_letters that takes a single parameter. The parameter is a string. Your function must return True if there are two identical letters in a row in the string, and False otherwise.

def test_double_letters():
    assert ch.double_letters('a') == False
    assert ch.double_letters('aba') == False
    assert ch.double_letters('bab') == False

    assert ch.double_letters('aa') == True
    assert ch.double_letters('abba') == True
    assert ch.double_letters('aabb') == True

########################################################
#### Adding and Removing Dots (3/10) ####
# https://pythonprinciples.com/challenges/Adding-and-removing-dots/

# Write a function named add_dots that takes a string and adds "." in between each letter. For example, calling add_dots("test") should return the string "t.e.s.t".

# Then, below the add_dots function, write another function named remove_dots that removes all dots from a string. For example, calling remove_dots("t.e.s.t") should return "test".

# If both functions are correct, calling remove_dots(add_dots(string)) should return back the original string for any string.

# (You may assume that the input to add_dots does not itself contain any dots.)

def test_add_dots():
    assert ch.add_dots('a') == 'a'
    assert ch.add_dots('test') == 't.e.s.t'

def test_remove_dots():
    assert ch.remove_dots('a') == 'a'
    assert ch.remove_dots('t.e.s.t') == 'test'

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

def test_count():
    assert ch.count('cat') == 1
    assert ch.count('ho-tel') == 2
    assert ch.count('met-a-phor') == 3
    assert ch.count('ter-min-a-tor') == 4

########################################################
#### Anagrams (3/10) ####
# https://pythonprinciples.com/challenges/Anagrams/

# Two strings are anagrams if you can make one from the other by rearranging the letters.

# Write a function named is_anagram that takes two strings as its parameters. Your function should return True if the strings are anagrams, and False otherwise.

# For example, the call is_anagram("typhoon", "opython") should return True while the call is_anagram("Alice", "Bob") should return False.

def test_is_anagram():
    assert ch.is_anagram("typhoon", "opython") == True 
    assert ch.is_anagram("Alice", "Bob") == False
    assert ch.is_anagram('test', 'tess') == False

########################################################
#### Flatten a List (3/10) ####
# https://pythonprinciples.com/challenges/Flatten-a-list/

# Write a function that takes a list of lists and flattens it into a one-dimensional list.

# Name your function flatten. It should take a single parameter and return a list.

# For example, calling: flatten([[1, 2], [3, 4]])

# Should return the list: [1, 2, 3, 4]

def test_flatten():
    assert ch.flatten([[1, 2], [3, 4]]) == [1,2,3,4]

########################################################
#### Min-maxing (3/10) ####
# https://pythonprinciples.com/challenges/Minmaxing/

# Define a function named largest_difference that takes a list of numbers as its only parameter.

# Your function should compute and return the difference between the largest and smallest number in the list.

# For example, the call largest_difference([1, 2, 3]) should return 2 because 3 - 1 is 2.

# You may assume that no numbers are smaller or larger than -100 and 100.

def test_largest_difference():
    assert ch.largest_difference([1, 2, 3]) == 2
    assert ch.largest_difference([-1, 2, -3]) == 5