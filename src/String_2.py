"""
    https://codingbat.com/python/String-2
    Medium python string problems -- 1 loop.. Use + to combine strings, len(str) is the number of chars in a String,
    str[i:j] extracts the substring starting at index i and running up to but not including index j.
"""


""" double_char
    Given a string, return a string where for every char in the original, there are two chars.
"""
def double_char(str):
    result = ""
    for i in range(len(str)):
        result += str[i] + str[i]
    return result

assert double_char('The') == 'TThhee'
assert double_char('AAbb') == 'AAAAbbbb'
assert double_char('Hi-There') == 'HHii--TThheerree'
assert double_char('Word!') == 'WWoorrdd!!'
assert double_char('') == ''
assert double_char('a') == 'aa'
assert double_char('.') == '..'
assert double_char('aa') == 'aaaa'


""" count_hi
    Return the number of times that the string "hi" appears anywhere in the given string.
"""
def count_hi(str):
    count = 0
    for i in range(len(str)-1):
        if (str[i:i+2] == "hi"): count += 1
    return count

assert count_hi('abc hi ho') == 1
assert count_hi('ABChi hi') == 2
assert count_hi('hihi') == 2
assert count_hi('hiHIhi') == 2
assert count_hi('') == 0
assert count_hi('h') == 0
assert count_hi('hi') == 1
assert count_hi('Hi is no HI on ahI') == 0
assert count_hi('hiho not HOHIhi') == 2


""" cat_dog
    Return True if the string "cat" and "dog" appear the same number of times in the given string.
"""
def cat_dog(str):
    cat_count = 0
    dog_count = 0

    for i in range(len(str)-2):
        t = str[i:i+3]
        if t == "cat": cat_count += 1
        elif t == "dog": dog_count += 1

    return cat_count == dog_count

assert cat_dog('catdog') == True
assert cat_dog('catcat') == False
assert cat_dog('1cat1cadodog') == True
assert cat_dog('catxxdogxxxdog') == False
assert cat_dog('catxdogxdogxcat') == True
assert cat_dog('catxdogxdogxca') == False
assert cat_dog('dogdogcat') == False
assert cat_dog('dogogcat') == True
assert cat_dog('dog') == False
assert cat_dog('cat') == False
assert cat_dog('ca') == True
assert cat_dog('c') == True
assert cat_dog('') == True


""" count_code
    Return the number of times that the string "code" appears anywhere in the given string, except we'll accept any 
    letter for the 'd', so "cope" and "cooe" count.
"""
def count_code(str):
    count = 0
    if (len(str) < 4): return count
    for i in range(len(str)-3):
        if str[i:i+2] == "co" and str[i+3] == "e": count += 1
    return count

assert count_code('aaacodebbb') == 1
assert count_code('codexxcode') == 2
assert count_code('cozexxcope') == 2
assert count_code('cozfxxcope') == 1
assert count_code('xxcozeyycop') == 1
assert count_code('cozcop') == 0
assert count_code('abcxyz') == 0
assert count_code('code') == 1
assert count_code('ode') == 0
assert count_code('c') == 0
assert count_code('') == 0
assert count_code('AAcodeBBcoleCCccoreDD') == 3
assert count_code('AAcodeBBcoleCCccorfDD') == 2
assert count_code('coAcodeBcoleccoreDD') == 3


""" end_other
    Given two strings, return True if either of the strings appears at the very end of the other string, ignoring 
    upper/lower case differences (in other words, the computation should not be "case sensitive").
"""
def end_other(a, b):
    a = a.lower()
    b = b.lower()
    return b == a[-len(b):] if len(a) > len(b) else a == b[-len(a):]

assert end_other('Hiabc', 'abc') == True
assert end_other('AbC', 'HiaBc') == True
assert end_other('abc', 'abXabc') == True
assert end_other('Hiabc', 'abcd') == False
assert end_other('Hiabc', 'bc') == True
assert end_other('Hiabcx', 'bc') == False
assert end_other('abc', 'abc') == True
assert end_other('xyz', '12xyz') == True
assert end_other('yz', '12xz') == False
assert end_other('Z', '12xz') == True
assert end_other('12', '12') == True
assert end_other('abcXYZ', 'abcDEF') == False
assert end_other('ab', 'ab12') == False
assert end_other('ab', '12ab') == True


""" xyz_there
    Return True if the given string contains an appearance of "xyz" where the xyz is not directly preceeded by a 
    period (.). So "xxyz" counts but "x.xyz" does not.
"""
def xyz_there(str):
    if len(str) < 4:
        return str == "xyz"
    elif str[0:3] == "xyz": return True
    else:
        for i in range(len(str)-3):
            if str[i] != "." and str[i+1:i+4] == "xyz": return True
        return False

assert xyz_there('abcxyz') == True
assert xyz_there('abc.xyz') == False
assert xyz_there('xyz.abc') == True
assert xyz_there('abcxy') == False
assert xyz_there('xyz') == True
assert xyz_there('xy') == False
assert xyz_there('x') == False
assert xyz_there('') == False
assert xyz_there('abc.xyzxyz') == True
assert xyz_there('abc.xxyz') == True
assert xyz_there('.xyz') == False
assert xyz_there('12.xyz') == False
assert xyz_there('12xyz') == True
assert xyz_there('1.xyz.xyz2.xyz') == False


""" bobThere
    Return true if the given string contains a "bob" string, but where the middle 'o' char can be any char.
"""
def bobThere(str):
    for i in range(len(str)-2):
        if str[i] == "b" and str[i+2] == "b":
            return True
    return False

assert bobThere("abcbob") == True
assert bobThere("b9b") == True
assert bobThere("bac") == False
assert bobThere("bbb") == True
assert bobThere("abcdefb") == False
assert bobThere("123abcbcdbabxyz") == True
assert bobThere("b12") == False
assert bobThere("b1b") == True
assert bobThere("b12b1b") == True
assert bobThere("bbc") == False
assert bobThere("bbb") == True
assert bobThere("bb") == False
assert bobThere("b") == False


""" xyBalance
    We'll say that a String is xy-balanced if for all the 'x' chars in the string, there exists a 'y' char somewhere
    later in the string. So "xxy" is balanced, but "xyx" is not. One 'y' can balance multiple 'x's. Return true if
    the given string is xy-balanced.
"""
def xyBalance(str):
    seenX = False
    for i in range(len(str)):
        if str[i] == "x":
            seenX = True
        elif str[i] == "y":
            seenX = False
    return not seenX

assert xyBalance("aaxbby") == True
assert xyBalance("aaxbb") == False
assert xyBalance("yaaxbb") == False
assert xyBalance("yaaxbby") == True
assert xyBalance("xaxxbby") == True
assert xyBalance("xaxxbbyx") == False
assert xyBalance("xxbxy") == True
assert xyBalance("xxbx") == False
assert xyBalance("bbb") == True
assert xyBalance("bxbb") == False
assert xyBalance("bxyb") == True
assert xyBalance("xy") == True
assert xyBalance("y") == True
assert xyBalance("x") == False
assert xyBalance("") == True
assert xyBalance("yxyxyxyx") == False
assert xyBalance("yxyxyxyxy") == True
assert xyBalance("12xabxxydxyxyzz") == True


""" mixString
    Given two strings, a and b, create a bigger string made of the first char of a, the first char of b, the second
    char of a, the second char of b, and so on. Any leftover chars go at the end of the result.
"""
def mixString(a, b):
    res = ""
    minlen = min(len(a), len(b))
    for i in range(minlen):
        res += a[i] + b[i]
    res += a[minlen:] + b[minlen:]
    return res

assert mixString("abc", "xyz") == "axbycz"
assert mixString("Hi", "There") == "HTihere"
assert mixString("xxxx", "There") == "xTxhxexre"
assert mixString("xxx", "X") == "xXxx"
assert mixString("2/", "27 around") == "22/7 around"
assert mixString("", "Hello") == "Hello"
assert mixString("Abc", "") == "Abc"
assert mixString("", "") == ""
assert mixString("a", "b") == "ab"
assert mixString("ax", "b") == "abx"
assert mixString("a", "bx") == "abx"
assert mixString("So", "Long") == "SLoong"
assert mixString("Long", "So") == "LSoong"


""" repeatEnd
    Given a string and an int n, return a string made of n repetitions of the last n characters of the string. You
    may assume that n is between 0 and the length of the string, inclusive.
"""
def repeatEnd(str, n):
    return n * str[-n:]

assert repeatEnd("Hello", 3) == "llollollo"
assert repeatEnd("Hello", 2) == "lolo"
assert repeatEnd("Hello", 1) == "o"
assert repeatEnd("Hello", 0) == ""
assert repeatEnd("abc", 3) == "abcabcabc"
assert repeatEnd("1234", 2) == "3434"
assert repeatEnd("1234", 3) == "234234234"
assert repeatEnd("", 0) == ""


""" repeatFront
    Given a string and an int n, return a string made of the first n characters of the string, followed by the first
    n-1 characters of the string, and so on. You may assume that n is between 0 and the length of the string,
    inclusive (i.e. n >= 0 and n <= str.length()).
"""
def repeatFront(str, n):
    res = ""
    while n >= 0:
        res += str[:n]
        n -= 1
    return res

assert repeatFront("Chocolate", 4) == "ChocChoChC"
assert repeatFront("Chocolate", 3) == "ChoChC"
assert repeatFront("Ice Cream", 2) == "IcI"
assert repeatFront("Ice Cream", 1) == "I"
assert repeatFront("Ice Cream", 0) == ""
assert repeatFront("xyz", 3) == "xyzxyx"
assert repeatFront("", 0) == ""
assert repeatFront("Java", 4) == "JavaJavJaJ"
assert repeatFront("Java", 1) == "J"


""" repeatSeparator
    Given two strings, word and a separator sep, return a big string made of count occurrences of the word, separated
    by the separator string.
"""
def repeatSeparator(word, sep, count):
    if count == 0:
        return ""
    elif count == 1:
        return word
    else:
        count -= 1
        return count * (word + sep) + word

assert repeatSeparator("Word", "X", 3) == "WordXWordXWord"
assert repeatSeparator("This", "And", 2) == "ThisAndThis"
assert repeatSeparator("This", "And", 1) == "This"
assert repeatSeparator("Hi", "-n-", 2) == "Hi-n-Hi"
assert repeatSeparator("AAA", "", 1) == "AAA"
assert repeatSeparator("AAA", "", 4) == "AAAAAAAAAAAA"
assert repeatSeparator("AAA", "", 0) == ""
assert repeatSeparator("A", "B", 5) == "ABABABABA"
assert repeatSeparator("abc", "XX", 3) == "abcXXabcXXabc"
assert repeatSeparator("abc", "XX", 2) == "abcXXabc"
assert repeatSeparator("abc", "XX", 1) == "abc"
assert repeatSeparator("XYZ", "a", 2) == "XYZaXYZ"


""" prefixAgain
    Given a string, consider the prefix string made of the first N chars of the string. Does that prefix string
    appear somewhere else in the string? Assume that the string is not empty and that N is in the range
    1..str.length().
"""
def prefixAgain(str, n):
    pref = str[:n]
    for i in range(n, len(str) - len(pref) + 1):
        if str[i:i+len(pref)] == pref:
            return True
    return False

assert prefixAgain("abXYabc", 1) == True
assert prefixAgain("abXYabc", 2) == True
assert prefixAgain("abXYabc", 3) == False
assert prefixAgain("xyzxyxyxy", 2) == True
assert prefixAgain("xyzxyxyxy", 3) == False
assert prefixAgain("Hi12345Hi6789Hi10", 1) == True
assert prefixAgain("Hi12345Hi6789Hi10", 2) == True
assert prefixAgain("Hi12345Hi6789Hi10", 3) == True
assert prefixAgain("Hi12345Hi6789Hi10", 4) == False
assert prefixAgain("a", 1) == False
assert prefixAgain("aa", 1) == True
assert prefixAgain("ab", 1) == False


""" xyzMiddle
    Given a string, does "xyz" appear in the middle of the string? To define middle, we'll say that the number of
    chars to the left and right of the "xyz" must differ by at most one. This problem is harder than it looks.
"""
def xyzMiddle(str):
    if len(str) < 3:
        return False
    else:
        mid = int(len(str) / 2) - 1
        if len(str) % 2 == 1:
            return str[mid:mid+3] == "xyz"
        else:
            return str[mid-1:mid+2] == "xyz" or str[mid:mid+3] == "xyz"

assert xyzMiddle("AAxyzBB") == True
assert xyzMiddle("AxyzBB") == True
assert xyzMiddle("AxyzBBB") == False
assert xyzMiddle("AxyzBBBB") == False
assert xyzMiddle("AAAxyzB") == False
assert xyzMiddle("AAAxyzBB") == True
assert xyzMiddle("AAAAxyzBB") == False
assert xyzMiddle("AAAAAxyzBBB") == False
assert xyzMiddle("1x345xyz12x4") == True
assert xyzMiddle("xyzAxyzBBB") == True
assert xyzMiddle("xyzAxyzBxyz") == True
assert xyzMiddle("xyzxyzAxyzBxyzxyz") == True
assert xyzMiddle("xyzxyzAxyzBxyzxyz") == True
assert xyzMiddle("xyzxyzAxyzxyzxyz") == True
assert xyzMiddle("xyzxyzAxyzxyzxy") == False
assert xyzMiddle("AxyzxyzBB") == False
assert xyzMiddle("") == False
assert xyzMiddle("x") == False
assert xyzMiddle("xy") == False
assert xyzMiddle("xyz") == True
assert xyzMiddle("xyzz") == True


""" getSandwich
    A sandwich is two pieces of bread with something in between. Return the string that is between the first and last
    appearance of "bread" in the given string, or return the empty string "" if there are not two pieces of bread.
"""
def getSandwich(str):
    if len(str) <= 10:
        return ""
    else:
        i = 0
        firstBreadIdx = 0
        while i < len(str) - 4:
            if str[i:i+5] == "bread":
                firstBreadIdx = i+5
                break
            else:
                i += 1
        i = len(str) - 4
        secondBreadIdx = 0
        while i > 0:
            if str[i:i+5] == "bread":
                secondBreadIdx = i
                break
            else:
                i -= 1
        if secondBreadIdx > firstBreadIdx:
            return str[firstBreadIdx:secondBreadIdx]
        else:
            return ""

assert getSandwich("breadjambread") == "jam"
assert getSandwich("xxbreadjambreadyy") == "jam"
assert getSandwich("xxbreadyy") == ""
assert getSandwich("xxbreadbreadjambreadyy") == "breadjam"
assert getSandwich("breadAbread") == "A"
assert getSandwich("breadbread") == ""
assert getSandwich("abcbreaz") == ""
assert getSandwich("xyz") == ""
assert getSandwich("") == ""
assert getSandwich("breadbreaxbread") == "breax"
assert getSandwich("breaxbreadybread") == "y"
assert getSandwich("breadbreadbreadbread") == "breadbread"


""" sameStarChar
    Returns true if for every '*' (star) in the string, if there are chars both immediately before and after the
    star, they are the same.
"""
def sameStarChar(str):
    if not str:
        return True
    else:
        for i in range(1, len(str)-1):
            if str[i] == "*":
                if str[i-1] != str[i+1]:
                    return False
        return True

assert sameStarChar("xy*yzz") == True
assert sameStarChar("xy*zzz") == False
assert sameStarChar("*xa*az") == True
assert sameStarChar("*xa*bz") == False
assert sameStarChar("*xa*a*") == True
assert sameStarChar("") == True
assert sameStarChar("*xa*a*a") == True
assert sameStarChar("*xa*a*b") == False
assert sameStarChar("*12*2*2") == True
assert sameStarChar("12*2*3*") == False
assert sameStarChar("abcDEF") == True
assert sameStarChar("XY*YYYY*Z*") == False
assert sameStarChar("XY*YYYY*Y*") == True
assert sameStarChar("12*2*3*") == False
assert sameStarChar("*") == True
assert sameStarChar("**") == True


""" oneTwo
    Given a string, compute a new string by moving the first char to come after the next two chars, so "abc" yields
    "bca". Repeat this process for each subsequent group of 3 chars, so "abcdef" yields "bcaefd". Ignore any group of
    fewer than 3 chars at the end.
"""
def oneTwo(str):
    if len(str) < 3:
        return ""
    else:
        return str[1:3] + str[0] + oneTwo(str[3:])

assert oneTwo("abc") == "bca"
assert oneTwo("tca") == "cat"
assert oneTwo("tcagdo") == "catdog"
assert oneTwo("chocolate") == "hocolctea"
assert oneTwo("1234567890") == "231564897"
assert oneTwo("xabxabxabxabxabxabxab") == "abxabxabxabxabxabxabx"
assert oneTwo("abcdefx") == "bcaefd"
assert oneTwo("abcdefxy") == "bcaefd"
assert oneTwo("abcdefxyz") == "bcaefdyzx"
assert oneTwo("") == ""
assert oneTwo("x") == ""
assert oneTwo("xy") == ""
assert oneTwo("xyz") == "yzx"
assert oneTwo("abcdefghijklkmnopqrstuvwxyz1234567890") == "bcaefdhigkljmnkpqostrvwuyzx231564897"
assert oneTwo("abcdefghijklkmnopqrstuvwxyz123456789") == "bcaefdhigkljmnkpqostrvwuyzx231564897"
assert oneTwo("abcdefghijklkmnopqrstuvwxyz12345678") == "bcaefdhigkljmnkpqostrvwuyzx231564"


""" zipZap
    Look for patterns like "zip" and "zap" in the string -- length-3, starting with 'z' and ending with 'p'. Return
    a string where for all such words, the middle letter is gone, so "zipXzap" yields "zpXzp".
"""
def zipZap(str):
    res = ""
    if len(str) < 3:
        return str
    else:
        i = 0
        while i <= len(str)-3:
            if str[i] == "z" and str[i+2] == "p":
                res += "zp"
                i += 3
            else:
                res += str[i]
                i += 1
        res += str[i:]
        return res

assert zipZap("zipXzap") == "zpXzp"
assert zipZap("zopzop") == "zpzp"
assert zipZap("zzzopzop") == "zzzpzp"
assert zipZap("zibzap") == "zibzp"
assert zipZap("zip") == "zp"
assert zipZap("zi") == "zi"
assert zipZap("z") == "z"
assert zipZap("") == ""
assert zipZap("zzp") == "zp"
assert zipZap("abcppp") == "abcppp"
assert zipZap("azbcppp") == "azbcppp"
assert zipZap("azbcpzpp") == "azbcpzp"


""" starOut
    Return a version of the given string, where for every star (*) in the string the star and the chars immediately
    to its left and right are gone. So "ab*cd" yields "ad" and "ab**cd" also yields "ad".
"""
def starOut(str):
    if not str:
        return str
    else:
        res = ""
        i = 0
        while i < len(str):
            if (i > 0 and str[i-1] == "*") or str[i] == "*" or (i+1 < len(str) and str[i+1] == "*"):
                i += 1
            else:
                res += str[i]
                i += 1
        return res

assert starOut("ab*cd") == "ad"
assert starOut("ab**cd") == "ad"
assert starOut("sm*eilly") == "silly"
assert starOut("sm*eil*ly") == "siy"
assert starOut("sm**eil*ly") == "siy"
assert starOut("sm***eil*ly") == "siy"
assert starOut("stringy*") == "string"
assert starOut("*stringy") == "tringy"
assert starOut("*str*in*gy") == "ty"
assert starOut("abc") == "abc"
assert starOut("a*bc") == "c"
assert starOut("ab") == "ab"
assert starOut("a*b") == ""
assert starOut("a") == "a"
assert starOut("a*") == ""
assert starOut("*a") == ""
assert starOut("*") == ""
assert starOut("") == ""


""" plusOut
    Given a string and a non-empty word string, return a version of the original String where all chars have been
    replaced by pluses ("+"), except for appearances of the word string which are preserved unchanged.
"""
def plusOut(str, word):
    if not str:
        return str
    elif len(word) > len(str):
        return len(str) * "+"
    else:
        res = ""
        i = 0
        while i < len(str)-len(word)+1:
            if str[i:i+len(word)] == word:
                res += word
                i += len(word)
            else:
                res += "+"
                i += 1
        for i in range(len(str)-len(res)):
            res += "+"
        return res

assert plusOut("12xy34", "xy") == "++xy++"
assert plusOut("12xy34", "1") == "1+++++"
assert plusOut("12xy34xyabcxy", "xy") == "++xy++xy+++xy"
assert plusOut("abXYabcXYZ", "ab") == "ab++ab++++"
assert plusOut("abXYabcXYZ", "abc") == "++++abc+++"
assert plusOut("abXYabcXYZ", "XY") == "++XY+++XY+"
assert plusOut("abXYxyzXYZ", "XYZ") == "+++++++XYZ"
assert plusOut("--++ab", "++") == "++++++"
assert plusOut("aaxxxxbb", "xx") == "++xxxx++"
assert plusOut("123123", "3") == "++3++3"


""" wordEnds
    Given a string and a non-empty word string, return a string made of each char just before and just after every
    appearance of the word in the string. Ignore cases where there is no char before or after the word, and a char
    may be included twice if it is between two words.
"""
def wordEnds(str, word):
    if not str or len(word) > len(str):
        return str
    else:
        i = 0
        res = ""
        while i < len(str) - len(word) + 1:
            if str[i:i+len(word)] == word:
                prev = str[i-1] if i > 0 else ""
                post = str[i + len(word)] if i + len(word) < len(str) else ""
                res += prev + post
                i += len(word)
            else:
                i += 1
        return res

assert wordEnds("abcXY123XYijk", "XY") == "c13i"
assert wordEnds("XY123XY", "XY") == "13"
assert wordEnds("XY1XY", "XY") == "11"
assert wordEnds("XYXY", "XY") == "XY"
assert wordEnds("XY", "XY") == ""
assert wordEnds("Hi", "XY") == ""
assert wordEnds("", "XY") == ""
assert wordEnds("abc1xyz1i1j", "1") == "cxziij"
assert wordEnds("abc1xyz1", "1") == "cxz"
assert wordEnds("abc1xyz11", "1") == "cxz11"
assert wordEnds("abc1xyz1abc", "abc") == "11"
assert wordEnds("abc1xyz1abc", "b") == "acac"
assert wordEnds("abc1abc1abc", "abc") == "1111"
