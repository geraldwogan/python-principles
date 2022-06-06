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