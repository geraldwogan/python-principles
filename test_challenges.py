import pytest
import challenges as ch

############################################

#### Capital Indexes (2/10) ####

# Write a function named capital_indexes. The function takes a single parameter, which is a string. Your function should return a list of all the indexes in the string that have capital letters.

# For example, calling capital_indexes("HeLlO") should return the list [0, 2, 4].

def test_capital_indexes():
    capitals = ch.capital_indexes("heLLo")
    assert capitals == [2,3]

############################################

#### Middle letter (2/10) ####

# Write a function named mid that takes a string as its parameter. Your function should extract and return the middle letter. If there is no middle letter, your function should return the empty string.

# For example, mid("abc") should return "b" and mid("aaaa") should return "".

def test_mid0():
    letter = ch.mid("abc")
    assert letter == 'b'

def test_mid1():
    letter = ch.mid("abcd")
    assert letter == ''