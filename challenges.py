############################################

#### Capital Indexes (2/10) ####

# Write a function named capital_indexes. The function takes a single parameter, which is a string. Your function should return a list of all the indexes in the string that have capital letters.

# For example, calling capital_indexes("HeLlO") should return the list [0, 2, 4].

def capital_indexes(string_in):
    capitals = []
    for idx, letter in enumerate(string_in):
        if letter.isupper():
            capitals.append(idx)
    return capitals

print(capital_indexes("heLIo"))

############################################

#### Middle letter (2/10) ####

# Write a function named mid that takes a string as its parameter. Your function should extract and return the middle letter. If there is no middle letter, your function should return the empty string.

# For example, mid("abc") should return "b" and mid("aaaa") should return "".

def mid(string_in):
    length = len(string_in)
    if length % 2 == 0:
        return ""
    else:
        return string_in[int(length/2)] # OR string[len(string)//2]

print(mid("world"))