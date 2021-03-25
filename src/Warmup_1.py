"""
    https://codingbat.com/python/Warmup-1
    Simple warmup problems to get started, no loops
"""


""" sleep_in
    The parameter weekday is True if it is a weekday, and the parameter vacation is True if we are on vacation. We
    sleep in if it is not a weekday or we're on vacation. Return True if we sleep in.
"""
def sleep_in(weekday, vacation):
    return not weekday or vacation

assert sleep_in(False, False) == True
assert sleep_in(True, False) == False
assert sleep_in(False, True) == True
assert sleep_in(True, True) == True


""" monkey_trouble
    We have two monkeys, a and b, and the parameters a_smile and b_smile indicate if each is smiling. We are in 
    trouble if they are both smiling or if neither of them is smiling. Return True if we are in trouble.
"""
def monkey_trouble(a_smile, b_smile):
    return a_smile and b_smile or not a_smile and not b_smile

assert monkey_trouble(True, True) == True
assert monkey_trouble(False, False) == True
assert monkey_trouble(True, False) == False
assert monkey_trouble(False, True) == False


""" sum_double
    Given two int values, return their sum. Unless the two values are the same, then return double their sum.
"""
def sum_double(a, b):
    if (a == b):
        return 2 * (a + b)
    else:
        return a + b

assert sum_double(1, 2) == 3
assert sum_double(3, 2) == 5
assert sum_double(2, 2) == 8
assert sum_double(-1, 0) == -1
assert sum_double(3, 3) == 12
assert sum_double(0, 0) == 0
assert sum_double(0, 1) == 1
assert sum_double(3, 4) == 7


""" diff21
    Given an int n, return the absolute difference between n and 21, except return double the absolute difference if 
    n is over 21.
"""
def diff21(n):
    if (n > 21):
        return 2 * (n - 21)
    else:
        return 21 - n

assert diff21(19) == 2
assert diff21(10) == 11
assert diff21(21) == 0
assert diff21(22) == 2
assert diff21(25) == 8
assert diff21(30) == 18
assert diff21(0) == 21
assert diff21(1) == 20
assert diff21(2) == 19
assert diff21(-1) == 22
assert diff21(-2) == 23
assert diff21(50) == 58


""" parrot_trouble
    We have a loud talking parrot. The "hour" parameter is the current hour time in the range 0..23. We are in 
    trouble if the parrot is talking and the hour is before 7 or after 20. Return True if we are in trouble.
"""
def parrot_trouble(talking, hour):
    return talking and (hour < 7 or hour > 20)

assert parrot_trouble(True, 6) == True
assert parrot_trouble(True, 7) == False
assert parrot_trouble(False, 6) == False
assert parrot_trouble(True, 21) == True
assert parrot_trouble(False, 21) == False
assert parrot_trouble(False, 20) == False
assert parrot_trouble(True, 23) == True
assert parrot_trouble(False, 23) == False
assert parrot_trouble(True, 20) == False
assert parrot_trouble(False, 12) == False


""" makes10
    Given 2 ints, a and b, return True if one if them is 10 or if their sum is 10.
"""
def makes10(a, b):
    return a == 10 or b == 10 or a + b == 10

assert makes10(9, 10) == True
assert makes10(9, 9) == False
assert makes10(1, 9) == True
assert makes10(10, 1) == True
assert makes10(10, 10) == True
assert makes10(8, 2) == True
assert makes10(8, 3) == False
assert makes10(10, 42) == True
assert makes10(12, -2) == True


""" near_hundred
    Given an int n, return True if it is within 10 of 100 or 200. Note: abs(num) computes the absolute value of a 
    number.
"""
def near_hundred(n):
    return abs(n - 100) <= 10 or abs(n - 200) <= 10

assert near_hundred(93) == True
assert near_hundred(90) == True
assert near_hundred(89) == False
assert near_hundred(110) == True
assert near_hundred(111) == False
assert near_hundred(121) == False
assert near_hundred(-101) == False
assert near_hundred(-209) == False
assert near_hundred(190) == True
assert near_hundred(209) == True
assert near_hundred(0) == False
assert near_hundred(5) == False
assert near_hundred(-50) == False
assert near_hundred(191) == True
assert near_hundred(189) == False
assert near_hundred(200) == True
assert near_hundred(210) == True
assert near_hundred(211) == False
assert near_hundred(290) == False


""" pos_neg
    Given 2 int values, return True if one is negative and one is positive. Except if the parameter "negative" is 
    True, then return True only if both are negative.
"""
def pos_neg(a, b, negative):
    if negative:
        return a < 0 and b < 0
    else:
        return a < 0 and b > 0 or b < 0 and a > 0

assert pos_neg(1, -1, False) == True
assert pos_neg(-1, 1, False) == True
assert pos_neg(-4, -5, True) == True
assert pos_neg(-4, -5, False) == False
assert pos_neg(-4, 5, False) == True
assert pos_neg(-4, 5, True) == False
assert pos_neg(1, 1, False) == False
assert pos_neg(-1, -1, False) == False
assert pos_neg(1, -1, True) == False
assert pos_neg(-1, 1, True) == False
assert pos_neg(1, 1, True) == False
assert pos_neg(-1, -1, True) == True
assert pos_neg(5, -5, False) == True
assert pos_neg(-6, 6, False) == True
assert pos_neg(-5, -6, False) == False
assert pos_neg(-2, -1, False) == False
assert pos_neg(1, 2, False) == False
assert pos_neg(-5, 6, True) == False
assert pos_neg(-5, -5, True) == True


""" not_string
    Given a string, return a new string where "not " has been added to the front. However, if the string already 
    begins with "not", return the string unchanged.
"""
def not_string(str):
    if (str[0:3] == 'not'):
        return str
    else:
        return "not " + str

assert not_string('candy') == 'not candy'
assert not_string('x') == 'not x'
assert not_string('not bad') == 'not bad'
assert not_string('bad') == 'not bad'
assert not_string('not') == 'not'
assert not_string('is not') == 'not is not'
assert not_string('no') == 'not no'


""" missing_char
    Given a non-empty string and an int n, return a new string where the char at index n has been removed. The value
     of n will be a valid index of a char in the original string (i.e. n will be in the range 0..len(str)-1 
     inclusive).
"""
def missing_char(str, n):
    return str[0:n] + str[n + 1:len(str)]

assert missing_char('kitten', 1) == 'ktten'
assert missing_char('kitten', 0) == 'itten'
assert missing_char('kitten', 4) == 'kittn'
assert missing_char('Hi', 0) == 'i'
assert missing_char('Hi', 1) == 'H'
assert missing_char('code', 0) == 'ode'
assert missing_char('code', 1) == 'cde'
assert missing_char('code', 2) == 'coe'
assert missing_char('code', 3) == 'cod'
assert missing_char('chocolate', 8) == 'chocolat'


""" front_back
    Given a string, return a new string where the first and last chars have been exchanged.
"""
def front_back(str):
    if (len(str)) > 1:
        return str[-1:] + str[1:-1] + str[:1]
    return str

assert front_back('code') == 'eodc'
assert front_back('a') == 'a'
assert front_back('ab') == 'ba'
assert front_back('abc') == 'cba'
assert front_back('') == ''
assert front_back('Chocolate') == 'ehocolatC'
assert front_back('aavJ') == 'Java'
assert front_back('hello') == 'oellh'


""" front3
    Given a string, we'll say that the front is the first 3 chars of the string. If the string length is less than 
    3, the front is whatever is there. Return a new string which is 3 copies of the front.
"""
def front3(str):
    if (len(str) < 3):
        return str + str + str
    else:
        sub = str[0:3]
        return sub + sub + sub

assert front3('Java') == 'JavJavJav'
assert front3('Chocolate') == 'ChoChoCho'
assert front3('abc') == 'abcabcabc'
assert front3('abcXYZ') == 'abcabcabc'
assert front3('ab') == 'ababab'
assert front3('a') == 'aaa'
assert front3('') == ''


""" backAround
    Given a string, take the last char and return a new string with the last char added at the front and back, so "cat" 
    yields "tcatt". The original string will be length 1 or more.
"""
def backAround(str):
    return str[-1:] + str + str[-1:]

assert backAround("cat") == "tcatt"
assert backAround("Hello") == "oHelloo"
assert backAround("a") == "aaa"
assert backAround("abc") == "cabcc"
assert backAround("read") == "dreadd"
assert backAround("boo") == "obooo"


""" or35
    Return true if the given non-negative number is a multiple of 3 or a multiple of 5.
"""
def or35(n):
    return n % 5 == 0 or n % 3 == 0

assert or35(3) == True
assert or35(10) == True
assert or35(8) == False
assert or35(15) == True
assert or35(5) == True
assert or35(9) == True
assert or35(4) == False
assert or35(7) == False
assert or35(6) == True
assert or35(17) == False
assert or35(18) == True
assert or35(29) == False
assert or35(20) == True
assert or35(21) == True
assert or35(22) == False
assert or35(45) == True
assert or35(99) == True
assert or35(100) == True
assert or35(101) == False
assert or35(121) == False
assert or35(122) == False
assert or35(123) == True


""" front22
    Given a string, take the first 2 chars and return the string with the 2 chars added at both the front and back, so 
    "kitten" yields"kikittenki". If the string length is less than 2, use whatever chars are there.
"""
def front22(str):
    return str[:2] + str + str[:2]

assert front22("kitten") == "kikittenki"
assert front22("Ha") == "HaHaHa"
assert front22("abc") == "ababcab"
assert front22("ab") == "ababab"
assert front22("a") == "aaa"
assert front22("") == ""
assert front22("Logic") == "LoLogicLo"


""" startHi
    Given a string, return true if the string starts with "hi" and false otherwise.
"""
def startHi(str):
    return str[:2] == "hi"

assert startHi("hi there") == True
assert startHi("hi") == True
assert startHi("hello hi") == False
assert startHi("he") == False
assert startHi("h") == False
assert startHi("") == False
assert startHi("ho hi") == False
assert startHi("hi ho") == True


""" icyHot
    Given two temperatures, return true if one is less than 0 and the other is greater than 100.
"""
def icyHot(temp1, temp2):
    return temp1 < 0 < 100 < temp2 or temp2 < 0 < 100 < temp1

assert icyHot(120, -1) == True
assert icyHot(-1, 120) == True
assert icyHot(2, 120) == False
assert icyHot(-1, 100) == False
assert icyHot(-2, -2) == False
assert icyHot(120, 120) == False


"""
"""