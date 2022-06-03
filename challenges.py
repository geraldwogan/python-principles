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

#### Middle Letter (2/10) ####

# Write a function named mid that takes a string as its parameter. Your function should extract and return the middle letter. If there is no middle letter, your function should return the empty string.

# For example, mid("abc") should return "b" and mid("aaaa") should return "".

def mid(string_in):
    length = len(string_in)
    if length % 2 == 0:
        return ""
    else:
        return string_in[int(length/2)] # OR string[len(string)//2]

print(mid("world"))

############################################

#### Online status (2/10) ####
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

