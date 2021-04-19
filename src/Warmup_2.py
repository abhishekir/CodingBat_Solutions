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


""" countXX
    Count the number of "xx" in the given string. We'll say that overlapping is allowed, so "xxx" contains 2 "xx".
"""
def countXX(str):
    count = 0
    for i in range(len(str)-1):
        if str[i:i+2] == "xx": count += 1
    return count

assert countXX("abcxx") == 1
assert countXX("xxx") == 2
assert countXX("xxxx") == 3
assert countXX("abc") == 0
assert countXX("Hello there") == 0
assert countXX("Hexxo thxxe") == 2
assert countXX("") == 0
assert countXX("Kittens") == 0
assert countXX("Kittensxxx") == 2


""" doubleX
    Given a string, return true if the first instance of "x" in the string is immediately followed by another "x".
"""
def doubleX(str):
    for i in range(len(str)-1):
        if str[i] == "x":
            return str[i+1] == "x"
    return False


assert doubleX("axxbb") == True
assert doubleX("axaxax") == False
assert doubleX("xxxxx") == True
assert doubleX("xaxxx") == False
assert doubleX("aaaax") == False
assert doubleX("") == False
assert doubleX("abc") == False
assert doubleX("x") == False
assert doubleX("xx") == True
assert doubleX("xax") == False
assert doubleX("xaxx") == False


""" string_bits
    Given a string, return a new string made of every other char starting with the first, so "Hello" yields "Hlo".
"""
def string_bits(str):
    return str[::2]

assert string_bits('Hello') == 'Hlo'
assert string_bits('Hi') == 'H'
assert string_bits('Heeololeo') == 'Hello'
assert string_bits('HiHiHi') == 'HHH'
assert string_bits('') == ''
assert string_bits('Greetings') == 'Getns'
assert string_bits('Chocoate') == 'Coot'
assert string_bits('pi') == 'p'
assert string_bits('Hello Kitten') == 'HloKte'
assert string_bits('hxaxpxpxy') == 'happy'


""" string_splosion
    Given a non-empty string like "Code" return a string like "CCoCodCode".
"""
def string_splosion(str):
    result = ''
    for i in range(len(str)+1):
        result += str[0:i]
    return result

assert string_splosion('Code') == 'CCoCodCode'
assert string_splosion('abc') == 'aababc'
assert string_splosion('ab') == 'aab'
assert string_splosion('x') == 'x'
assert string_splosion('fade') == 'ffafadfade'
assert string_splosion('There') == 'TThTheTherThere'
assert string_splosion('Kitten') == 'KKiKitKittKitteKitten'
assert string_splosion('Bye') == 'BByBye'
assert string_splosion('Good') == 'GGoGooGood'
assert string_splosion('Bad') == 'BBaBad'


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

assert last2('hixxhi') == 1
assert last2('xaxxaxaxx') == 1
assert last2('axxxaaxx') == 2
assert last2('xxaxxaxxaxx') == 3
assert last2('xaxaxaxx') == 0
assert last2('xxxx') == 2
assert last2('13121312') == 1
assert last2('11212') == 1
assert last2('13121311') == 0
assert last2('1717171') == 2
assert last2('hi') == 0
assert last2('h') == 0
assert last2('') == 0


""" array_count9
    Given an array of ints, return the number of 9's in the array.
"""
def array_count9(nums):
    count = 0
    for i in range(len(nums)):
        if (nums[i] == 9):
            count += 1
    return count

assert array_count9([1, 2, 9]) == 1
assert array_count9([1, 9, 9]) == 2
assert array_count9([1, 9, 9, 3, 9]) == 3
assert array_count9([1, 2, 3]) == 0
assert array_count9([]) == 0
assert array_count9([4, 2, 4, 3, 1]) == 0
assert array_count9([9, 2, 4, 3, 1]) == 1


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

assert array_front9([1, 2, 9, 3, 4]) == True
assert array_front9([1, 2, 3, 4, 9]) == False
assert array_front9([1, 2, 3, 4, 5]) == False
assert array_front9([9, 2, 3]) == True
assert array_front9([1, 9, 9]) == True
assert array_front9([1, 2, 3]) == False
assert array_front9([1, 9]) == True
assert array_front9([5, 5]) == False
assert array_front9([2]) == False
assert array_front9([9]) == True
assert array_front9([]) == False
assert array_front9([3, 9, 2, 3, 3]) == True


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

assert array123([1, 1, 2, 3, 1]) == True
assert array123([1, 1, 2, 4, 1]) == False
assert array123([1, 1, 2, 1, 2, 3]) == True
assert array123([1, 1, 2, 1, 2, 1]) == False
assert array123([1, 2, 3, 1, 2, 3]) == True
assert array123([1, 2, 3]) == True
assert array123([1, 1, 1]) == False
assert array123([1, 2]) == False
assert array123([1]) == False
assert array123([]) == False


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

assert string_match('xxcaazz', 'xxbaaz') == 3
assert string_match('abc', 'abc') == 2
assert string_match('abc', 'axc') == 0
assert string_match('hello', 'he') == 1
assert string_match('he', 'hello') == 1
assert string_match('h', 'hello') == 0
assert string_match('', 'hello') == 0
assert string_match('aabbccdd', 'abbbxxd') == 1
assert string_match('aaxxaaxx', 'iaxxai') == 3
assert string_match('iaxxai', 'aaxxaaxx') == 3


""" stringX
    Given a string, return a version where all the "x" have been removed. Except an "x" at the very start or end
    should not be removed.
"""
def stringX(str):
    res = ""
    if len(str) == 0:
        return res
    elif len(str) == 1:
        return str
    else:
        res += str[0]
        for i in range(1, len(str)-1):
            if str[i] != "x":
                res += str[i]
        res += str[len(str)-1]
    return res

assert stringX("xxHxix") == "xHix"
assert stringX("abxxxcd") == "abcd"
assert stringX("xabxxxcdx") == "xabcdx"
assert stringX("xKittenx") == "xKittenx"
assert stringX("Hello") == "Hello"
assert stringX("xx") == "xx"
assert stringX("x") == "x"
assert stringX("") == ""


""" altPairs
    Given a string, return a string made of the chars at indexes 0,1, 4,5, 8,9 ... so "kittens" yields "kien".
"""
def altPairs(str):
    res = ""
    i = 0
    while i < len(str):
        res += str[i:i+2]
        i += 4
    return res

assert altPairs("kitten") == "kien"
assert altPairs("Chocolate") == "Chole"
assert altPairs("CodingHorror") == "Congrr"
assert altPairs("yak") == "ya"
assert altPairs("ya") == "ya"
assert altPairs("y") == "y"
assert altPairs("") == ""
assert altPairs("ThisThatTheOther") == "ThThThth"


""" stringYak
    Suppose the string "yak" is unlucky. Given a string, return a version where all the "yak" are removed, but the
    "a" can be any char. The "yak" strings will not overlap.
"""
def stringYak(str):
    res = ""
    if len(str) == 0:
        return res
    else:
        i = 0
        while i < len(str):
            if i < len(str) - 2 and str[i] == "y" and str[i+2] == "k":
                i += 3
            else:
                res += str[i]
                i += 1
    return res


assert stringYak("yakpak") == "pak"
assert stringYak("pakyak") == "pak"
assert stringYak("yak123ya") == "123ya"
assert stringYak("yak") == ""
assert stringYak("yakxxxyak") == "xxx"
assert stringYak("HiyakHi") == "HiHi"
assert stringYak("xxxyakyyyakzzz") == "xxxyyzzz"


""" array667
    Given an array of ints, return the number of times that two 6's are next to each other in the array. Also count
    instances where the second "6" is actually a 7.
"""
def array667(nums):
    count = 0
    for i in range(len(nums)-1):
        if nums[i] == 6 and nums[i+1] == 6 or nums[i+1] == 7:
            count += 1
    return count

assert array667([6, 6, 2]) == 1
assert array667([6, 6, 2, 6]) == 1
assert array667([6, 7, 2, 6]) == 1
assert array667([6, 6, 2, 6, 7]) == 2
assert array667([1, 6, 3]) == 0
assert array667([6, 1]) == 0
assert array667([]) == 0
assert array667([3, 6, 7, 6]) == 1
assert array667([3, 6, 6, 7]) == 2
assert array667([6, 3, 6, 6]) == 1
assert array667([6, 7, 6, 6]) == 2
assert array667([1, 2, 3, 5, 6]) == 0
assert array667([1, 2, 3, 6, 6]) == 1


""" noTriples
    Given an array of ints, we'll say that a triple is a value appearing 3 times in a row in the array. Return true
    if the array does not contain any triples.
"""
def noTriples(nums):
    if len(nums) < 3:
        return True
    else:
        for i in range(len(nums)-2):
            if nums[i] == nums[i+1] == nums[i+2]:
                return False
    return True


assert noTriples([1, 1, 2, 2, 1]) == True
assert noTriples([1, 1, 2, 2, 2, 1]) == False
assert noTriples([1, 1, 1, 2, 2, 2, 1]) == False
assert noTriples([1, 1, 2, 2, 1, 2, 1]) == True
assert noTriples([1, 2, 1]) == True
assert noTriples([1, 1, 1]) == False
assert noTriples([1, 1]) == True
assert noTriples([1]) == True
assert noTriples([]) == True


""" has271
    Given an array of ints, return true if it contains a 2, 7, 1 pattern: a value, followed by the value plus 5,
    followed by the value minus 1. Additionally the 271 counts even if the "1" differs by 2 or less from the correct
    value.
"""
def has271(nums):
    if len(nums) < 3:
        return False
    else:
        for i in range(len(nums)-2):
            if nums[i+1] == nums[i] + 5 and nums[i] - nums[i+2] in range(-1, 4):
                return True
        return False

assert has271([1, 2, 7, 1]) == True
assert has271([1, 2, 8, 1]) == False
assert has271([2, 7, 1]) == True
assert has271([3, 8, 2]) == True
assert has271([2, 7, 3]) == True
assert has271([2, 7, 4]) == False
assert has271([2, 7, -1]) == True
assert has271([2, 7, -2]) == False
assert has271([4, 5, 3, 8, 0]) == True
assert has271([2, 7, 5, 10, 4]) == True
assert has271([2, 7, -2, 4, 9, 3]) == True
assert has271([2, 7, 5, 10, 1]) == False
assert has271([2, 7, -2, 4, 10, 2]) == False
assert has271([1, 1, 4, 9, 0]) == False
assert has271([1, 1, 4, 9, 4, 9, 2]) == True
