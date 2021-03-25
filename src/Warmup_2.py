"""
    https://codingbat.com/python/Warmup-2
    Medium warmup string/list problems with loops
"""


""" string_times
    Given a string and a non-negative int n, return a larger string that is n copies of the original string.
"""
def string_times(str, n):
    result = ''
    for i in range(n):
        result += str
    return result

assert string_times('Hi', 2) == 'HiHi'
assert string_times('Hi', 3) == 'HiHiHi'
assert string_times('Hi', 1) == 'Hi'
assert string_times('Hi', 0) == ''
assert string_times('Hi', 5) == 'HiHiHiHiHi'
assert string_times('Oh Boy!', 2) == 'Oh Boy!Oh Boy!'
assert string_times('x', 4) == 'xxxx'
assert string_times('', 4) == ''
assert string_times('code', 2) == 'codecode'
assert string_times('code', 3) == 'codecodecode'


""" front_times
    Given a string and a non-negative int n, we'll say that the front of the string is the first 3 chars, or 
    whatever is there if the string is less than length 3. Return n copies of the front;
"""
def front_times(str, n):
    if (len(str) < 3):
        front = str
    else:
        front = str[0:3]
    result = ''
    for i in range(n):
        result += front
    return result

assert front_times('Chocolate', 2) == 'ChoCho'
assert front_times('Chocolate', 3) == 'ChoChoCho'
assert front_times('Abc', 3) == 'AbcAbcAbc'
assert front_times('Ab', 4) == 'AbAbAbAb'
assert front_times('A', 4) == 'AAAA'
assert front_times('', 4) == ''
assert front_times('Abc', 0) == ''


""" string_bits
    Given a string, return a new string made of every other char starting with the first, so "Hello" yields "Hlo".
"""
def string_bits(str):
    return str[::2]

""" string_splosion
    Given a non-empty string like "Code" return a string like "CCoCodCode".
"""
def string_splosion(str):
    result = ''
    for i in range(len(str)+1):
        result += str[0:i]
    return result

""" last2
    Given a string, return the count of the number of times that a substring length 2 appears in the string and also 
    as the last 2 chars of the string, so "hixxxhi" yields 1 (we won't count the end substring).
"""
def last2(str):
    count = 0
    if(len(str) <= 2):
        return count
    end = str[-2:]
    for i in range(len(str)-2):
        if(str[i:i+2] == end):
            count += 1
    return count

""" array_count9
    Given an array of ints, return the number of 9's in the array.
"""
def array_count9(nums):
    count = 0
    for i in range(len(nums)):
        if (nums[i] == 9):
            count += 1
    return count

""" array_front9
    Given an array of ints, return True if one of the first 4 elements in the array is a 9. The array length may be 
    less than 4.
"""
def array_front9(nums):
    max = 4 if len(nums) > 4 else len(nums)
    for i in range(max):
        if(nums[i] == 9):
            return True
    return False

""" array123
    Given an array of ints, return True if the sequence of numbers 1, 2, 3 appears in the array somewhere.
"""
def array123(nums):
    if len(nums) < 3:
        return False
    else:
        for i in range(len(nums)-2):
            if nums[i] == 1 and nums[i+1] == 2 and nums[i+2] == 3:
                return True
        return False

""" string_match
    Given 2 strings, a and b, return the number of the positions where they contain the same length 2 substring. So 
    "xxcaazz" and "xxbaaz" yields 3, since the "xx", "aa", and "az" substrings appear in the same place in both 
    strings.
"""
def string_match(a, b):
    match_count = 0
    for i in range(len(a)-1):
        if (a[i:i+2] == b[i:i+2]):
            match_count += 1
    return match_count