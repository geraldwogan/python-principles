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

def test_mid1():
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