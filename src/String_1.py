"""
    https://codingbat.com/python/String-1
    Basic python string problems -- no loops. Use + to combine strings, len(str) is the number of chars in a String,
    str[i:j] extracts the substring starting at index i and running up to but not including index j.
"""


""" hello_name
    Given a string name, e.g. "Bob", return a greeting of the form "Hello Bob!".
"""
def hello_name(name):
    return 'Hello ' + name + '!'

assert hello_name('Bob') == 'Hello Bob!'
assert hello_name('Alice') == 'Hello Alice!'
assert hello_name('X') == 'Hello X!'
assert hello_name('Dolly') == 'Hello Dolly!'
assert hello_name('Alpha') == 'Hello Alpha!'
assert hello_name('Omega') == 'Hello Omega!'
assert hello_name('Goodbye') == 'Hello Goodbye!'
assert hello_name('ho ho ho') == 'Hello ho ho ho!'
assert hello_name('xyz!') == 'Hello xyz!!'
assert hello_name('Hello') == 'Hello Hello!'


""" make_abba
    Given two strings, a and b, return the result of putting them together in the order abba, e.g. "Hi" and "Bye" 
    returns "HiByeByeHi".
"""
def make_abba(a, b):
    return a + b + b + a

assert make_abba('Hi', 'Bye') == 'HiByeByeHi'
assert make_abba('Yo', 'Alice') == 'YoAliceAliceYo'
assert make_abba('What', 'Up') == 'WhatUpUpWhat'
assert make_abba('aaa', 'bbb') == 'aaabbbbbbaaa'
assert make_abba('x', 'y') == 'xyyx'
assert make_abba('x', '') == 'xx'
assert make_abba('', 'y') == 'yy'
assert make_abba('Bo', 'Ya') == 'BoYaYaBo'
assert make_abba('Ya', 'Ya') == 'YaYaYaYa'


""" make_tags
    The web is built with HTML strings like "<i>Yay</i>" which draws Yay as italic text. In this example, the "i" 
    tag makes <i> and </i> which surround the word "Yay". Given tag and word strings, create the HTML string with 
    tags around the word, e.g. "<i>Yay</i>".
"""
def make_tags(tag, word):
    return '<' + tag + '>' + word + '</' + tag + '>'

assert make_tags('i', 'Yay') == '<i>Yay</i>'
assert make_tags('i', 'Hello') == '<i>Hello</i>'
assert make_tags('cite', 'Yay') == '<cite>Yay</cite>'
assert make_tags('address', 'here') == '<address>here</address>'
assert make_tags('body', 'Heart') == '<body>Heart</body>'
assert make_tags('i', 'i') == '<i>i</i>'
assert make_tags('i', '') == '<i></i>'


""" make_out_word
    Given an "out" string length 4, such as "<<>>", and a word, return a new string where the word is in the middle 
    of the out string, e.g. "<<word>>".
"""
def make_out_word(out, word):
    return out[:2] + word + out[2:]

assert make_out_word('<<>>', 'Yay') == '<<Yay>>'
assert make_out_word('<<>>', 'WooHoo') == '<<WooHoo>>'
assert make_out_word('[[]]', 'word') == '[[word]]'
assert make_out_word('HHoo', 'Hello') == 'HHHellooo'
assert make_out_word('abyz', 'YAY') == 'abYAYyz'


""" extra_end
    Given a string, return a new string made of 3 copies of the last 2 chars of the original string. The string 
    length will be at least 2.
"""
def extra_end(str):
    s = str[-2:]
    return s + s + s

assert extra_end('Hello') == 'lololo'
assert extra_end('ab') == 'ababab'
assert extra_end('Hi') == 'HiHiHi'
assert extra_end('Candy') == 'dydydy'
assert extra_end('Code') == 'dedede'


""" first_two
    Given a string, return the string made of its first two chars, so the String "Hello" yields "He". If the string
     is shorter than length 2, return whatever there is, so "X" yields "X", and the empty string "" yields the empty 
     string "".
"""
def first_two(str):
    return str[:2]

assert first_two('Hello') == 'He'
assert first_two('abcdefg') == 'ab'
assert first_two('ab') == 'ab'
assert first_two('a') == 'a'
assert first_two('') == ''
assert first_two('Kitten') == 'Ki'
assert first_two('hi') == 'hi'
assert first_two('hiya') == 'hi'


""" first_half
    Given a string of even length, return the first half. So the string "WooHoo" yields "Woo".
"""
def first_half(str):
    x = len(str) // 2
    return str[:x]

assert first_half('WooHoo') == 'Woo'
assert first_half('HelloThere') == 'Hello'
assert first_half('abcdef') == 'abc'
assert first_half('ab') == 'a'
assert first_half('') == ''
assert first_half('0123456789') == '01234'
assert first_half('kitten') == 'kit'


""" without_end
    Given a string, return a version without the first and last char, so "Hello" yields "ell". The string length 
    will be at least 2.
"""
def without_end(str):
    return str[1:-1]

assert without_end('Hello') == 'ell'
assert without_end('java') == 'av'
assert without_end('coding') == 'odin'
assert without_end('code') == 'od'
assert without_end('ab') == ''
assert without_end('Chocolate!') == 'hocolate'
assert without_end('kitten') == 'itte'
assert without_end('woohoo') == 'ooho'


""" combo_string
    Given 2 strings, a and b, return a string of the form short+long+short, with the shorter string on the outside 
    and the longer string on the inside. The strings will not be the same length, but they may be empty (length 0).
"""
def combo_string(a, b):
    if len(a) > len(b):
        return b + a + b
    else:
        return a + b + a

assert combo_string('Hello', 'hi') == 'hiHellohi'
assert combo_string('hi', 'Hello') == 'hiHellohi'
assert combo_string('aaa', 'b') == 'baaab'
assert combo_string('b', 'aaa') == 'baaab'
assert combo_string('aaa', '') == 'aaa'
assert combo_string('', 'bb') == 'bb'
assert combo_string('aaa', '1234') == 'aaa1234aaa'
assert combo_string('aaa', 'bb') == 'bbaaabb'
assert combo_string('a', 'bb') == 'abba'
assert combo_string('bb', 'a') == 'abba'
assert combo_string('xyz', 'ab') == 'abxyzab'


""" non_start
    Given 2 strings, return their concatenation, except omit the first char of each. The strings will be at least 
    length 1.
"""
def non_start(a, b):
    return a[1:] + b[1:]

assert non_start('Hello', 'There') == 'ellohere'
assert non_start('java', 'code') == 'avaode'
assert non_start('shotl', 'java') == 'hotlava'
assert non_start('ab', 'xy') == 'by'
assert non_start('ab', 'x') == 'b'
assert non_start('ab', 'x') == 'b'
assert non_start('x', 'ac') == 'c'
assert non_start('a', 'x') == ''
assert non_start('kit', 'kat') == 'itat'
assert non_start('mart', 'dart') == 'artart'


""" left2
    Given a string, return a "rotated left 2" version where the first 2 chars are moved to the end. The string 
    length will be at least 2.
"""
def left2(str):
    return str[2:] + str[:2]

assert left2('Hello') == 'lloHe'
assert left2('java') == 'vaja'
assert left2('Hi') == 'Hi'
assert left2('code') == 'deco'
assert left2('cat') == 'tca'
assert left2('12345') == '34512'
assert left2('Chocolate') == 'ocolateCh'
assert left2('bricks') == 'icksbr'


""" right2
    Given a string, return a "rotated right 2" version where the last 2 chars are moved to the start. The string
    length will be at least 2.
"""
def right2(str):
    return str[-2:] + str[:-2]

assert right2("Hello") == "loHel"
assert right2("java") == "vaja"
assert right2("Hi") == "Hi"
assert right2("code") == "deco"
assert right2("cat") == "atc"
assert right2("12345") == "45123"


""" theEnd
    Given a string, return a string length 1 from its front, unless front is false, in which case return a string
    length 1 from its back. The string will be non-empty.
"""
def theEnd(str, front):
    return str[:1] if front else str[-1:]

assert theEnd("Hello", True) == "H"
assert theEnd("Hello", False) == "o"
assert theEnd("oh", True) == "o"
assert theEnd("oh", False) == "h"
assert theEnd("x", True) == "x"
assert theEnd("x", False) == "x"
assert theEnd("java", True) == "j"
assert theEnd("chocolate", False) == "e"
assert theEnd("1234", True) == "1"
assert theEnd("code", False) == "e"


""" withouEnd2
    Given a string, return a version without both the first and last char of the string. The string may be any
    length, including 0.
"""
def withouEnd2(str):
    return str[1:-1]

assert withouEnd2("Hello") == "ell"
assert withouEnd2("abc") == "b"
assert withouEnd2("ab") == ""
assert withouEnd2("a") == ""
assert withouEnd2("") == ""
assert withouEnd2("coldy") == "old"
assert withouEnd2("java code") == "ava cod"


""" middleTwo
    Given a string of even length, return a string made of the middle two chars, so the string "string" yields "ri".
    The string length will be at least 2.
"""
def middleTwo(str):
    mid = int(len(str) / 2)
    return str[mid-1] + str[mid]

assert middleTwo("string") == "ri"
assert middleTwo("code") == "od"
assert middleTwo("Practice") == "ct"
assert middleTwo("ab") == "ab"
assert middleTwo("0123456789") == "45"


""" endsLy
    Given a string, return true if it ends in "ly".
"""
def endsLy(str):
    return str[-2:] == "ly"

assert endsLy("oddly") == True
assert endsLy("y") == False
assert endsLy("oddy") == False
assert endsLy("oddl") == False
assert endsLy("olydd") == False
assert endsLy("ly") == True
assert endsLy("") == False
assert endsLy("Falsey") == False
assert endsLy("evenly") == True


""" nTwice
    Given a string and an int n, return a string made of the first and last n chars from the string. The string
    length will be at least n.
"""
def nTwice(str, n):
    return "" if n == 0 else str[:n] + str[-n:]

assert nTwice("Hello", 2) == "Helo"
assert nTwice("Chocolate", 3) == "Choate"
assert nTwice("Chocolate", 1) == "Ce"
assert nTwice("Chocolate", 0) == ""
assert nTwice("Hello", 4) == "Hellello"
assert nTwice("Code", 4) == "CodeCode"
assert nTwice("Code", 2) == "Code"


""" twoChar
    Given a string and an index, return a string length 2 starting at the given index. If the index is too big or too
    small to define a string length 2, use the first 2 chars. The string length will be at least 2.
"""
def twoChar(str, index):
    return str[:2] if index + 2 > len(str) or index < 0 else str[index:index+2]

assert twoChar("java", 0) == "ja"
assert twoChar("java", 2) == "va"
assert twoChar("java", 3) == "ja"
assert twoChar("java", 4) == "ja"
assert twoChar("java", -1) == "ja"
assert twoChar("Hello", 0) == "He"
assert twoChar("Hello", 1) == "el"
assert twoChar("Hello", 99) == "He"
assert twoChar("Hello", 3) == "lo"
assert twoChar("Hello", 4) == "He"
assert twoChar("Hello", 5) == "He"
assert twoChar("Hello", -7) == "He"
assert twoChar("Hello", 6) == "He"
assert twoChar("Hello", -1) == "He"
assert twoChar("yay", 0) == "ya"


""" middleThree
    Given a string of odd length, return the string length 3 from its middle, so "Candy" yields "and". The string
    length will be at least 3.
"""
def middleThree(str):
    mid = int(len(str) / 2)
    return str[mid-1:mid+2]

assert middleThree("Candy") == "and"
assert middleThree("and") == "and"
assert middleThree("solving") == "lvi"
assert middleThree("Hi yet Hi") == "yet"
assert middleThree("java yet java") == "yet"
assert middleThree("Chocolate") == "col"
assert middleThree("XabcxyzabcX") == "xyz"


""" hasBad
    Given a string, return true if "bad" appears starting at index 0 or 1 in the string, such as with "badxxx" or
    "xbadxx" but not "xxbadxx". The string may be any length, including 0. Note: use .equals() to compare 2 strings.
"""
def hasBad(str):
    return len(str) > 2 and str[0:3] == "bad" or len(str) > 3 and str[1:4] == "bad"

assert hasBad("badxx") == True
assert hasBad("xbadxx") == True
assert hasBad("xxbadxx") == False
assert hasBad("code") == False
assert hasBad("bad") == True
assert hasBad("ba") == False
assert hasBad("xba") == False
assert hasBad("xbad") == True
assert hasBad("") == False
assert hasBad("badyy") == True


""" atFirst
    Given a string, return a string length 2 made of its first 2 chars. If the string length is less than 2, use '@'
    for the missing chars.
"""
def atFirst(str):
    return (str[0] if str else "@") + (str[1] if len(str) > 1 else "@")

assert atFirst("hello") == "he"
assert atFirst("hi") == "hi"
assert atFirst("h") == "h@"
assert atFirst("") == "@@"
assert atFirst("kitten") == "ki"
assert atFirst("java") == "ja"
assert atFirst("j") == "j@"


""" lastChars
    Given 2 strings, a and b, return a new string made of the first char of a and the last char of b, so "yo" and
    "java" yields "ya". If either string is length 0, use '@' for its missing char.
"""
def lastChars(a, b):
    return (a[0] if a else "@") + (b[-1:] if b else "@")

assert lastChars("last", "chars") == "ls"
assert lastChars("yo", "java") == "ya"
assert lastChars("hi", "") == "h@"
assert lastChars("", "hello") == "@o"
assert lastChars("", "") == "@@"
assert lastChars("kitten", "hi") == "ki"
assert lastChars("k", "zip") == "kp"
assert lastChars("kitten", "") == "k@"
assert lastChars("kitten", "zip") == "kp"


""" conCat
    Given two strings, append them together (known as "concatenation") and return the result. However, if the
    concatenation creates a double-char, then omit one of the chars, so "abc" and "cat" yields "abcat".
"""
def conCat(a, b):
    if a and not b:
        return a
    elif b and not a:
        return b
    else:
        return (a if a[-1:] != b[0] else a[:-1]) + b

assert conCat("abc", "cat") == "abcat"
assert conCat("dog", "cat") == "dogcat"
assert conCat("abc", "") == "abc"
assert conCat("", "cat") == "cat"
assert conCat("pig", "g") == "pig"
assert conCat("pig", "doggy") == "pigdoggy"


""" lastTwo
    Given a string of any length, return a new string where the last 2 chars, if present, are swapped, so "coding"
    yields "codign".
"""
def lastTwo(str):
    if len(str) < 2:
        return str
    else:
        return str[:-2] + str[-1:] + str[-2:-1]

assert lastTwo("coding") == "codign"
assert lastTwo("cat") == "cta"
assert lastTwo("ab") == "ba"
assert lastTwo("a") == "a"
assert lastTwo("") == ""


""" seeColor
    Given a string, if the string begins with "red" or "blue" return that color string, otherwise return the empty
    string.
"""
def seeColor(str):
    return "red" if str[:3] == "red" else "blue" if str[:4] == "blue" else ""

assert seeColor("redxx") == "red"
assert seeColor("xxred") == ""
assert seeColor("blueTimes") == "blue"
assert seeColor("NoColor") == ""
assert seeColor("red") == "red"
assert seeColor("re") == ""
assert seeColor("blu") == ""
assert seeColor("blue") == "blue"
assert seeColor("a") == ""
assert seeColor("") == ""
assert seeColor("xyzred") == ""


""" frontAgain
    Given a string, return true if the first 2 chars in the string also appear at the end of the string, such as with
    "edited".
"""
def frontAgain(str):
    if len(str) < 2:
        return False
    else:
        return str[:2] == str[-2:]

assert frontAgain("edited") == True
assert frontAgain("edit") == False
assert frontAgain("ed") == True
assert frontAgain("jj") == True
assert frontAgain("jjj") == True
assert frontAgain("jjjj") == True
assert frontAgain("jjjk") == False
assert frontAgain("x") == False
assert frontAgain("") == False
assert frontAgain("java") == False
assert frontAgain("javaja") == True


""" minCat
    Given two strings, append them together (known as "concatenation") and return the result. However, if the strings
    are different lengths, omit chars from the longer string so it is the same length as the shorter string. So
    "Hello" and "Hi" yield "loHi". The strings may be any length.
"""
def minCat(a, b):
    if a and b:
        shortest = len(a) if len(a) < len(b) else len(b)
        return a[-shortest:] + b[-shortest:]
    return ""

assert minCat("Hello", "Hi") == "loHi"
assert minCat("Hello", "java") == "ellojava"
assert minCat("java", "Hello") == "javaello"
assert minCat("abc", "x") == "cx"
assert minCat("x", "abc") == "xc"
assert minCat("abc", "") == ""


""" extraFront
    Given a string, return a new string made of 3 copies of the first 2 chars of the original string. The string may
    be any length. If there are fewer than 2 chars, use whatever is there.
"""
def extraFront(str):
    front = str[:2]
    return 3 * front

assert extraFront("Hello") == "HeHeHe"
assert extraFront("ab") == "ababab"
assert extraFront("H") == "HHH"
assert extraFront("") == ""
assert extraFront("Candy") == "CaCaCa"
assert extraFront("Code") == "CoCoCo"


""" without2
    Given a string, if a length 2 substring appears at both its beginning and end, return a string without the
    substring at the beginning, so "HelloHe" yields "lloHe". The substring may overlap with itself, so "Hi" yields
    "". Otherwise, return the original string unchanged.
"""
def without2(str):
    if len(str) < 2:
        return str
    else:
        return str[2:] if str[:2] == str[-2:] else str

assert without2("HelloHe") == "lloHe"
assert without2("HelloHi") == "HelloHi"
assert without2("Hi") == ""
assert without2("Chocolate") == "Chocolate"
assert without2("xxx") == "x"
assert without2("xx") == ""
assert without2("x") == "x"
assert without2("") == ""
assert without2("Fruits") == "Fruits"


""" deFront
    Given a string, return a version without the first 2 chars. Except keep the first char if it is 'a' and keep the
    second char if it is 'b'. The string may be any length. Harder than it looks.
"""
def deFront(str):
    return (str[0] if str and str[0] == "a" else "") \
           + (str[1] if len(str) > 1 and str[1] == "b" else "") \
           + (str[2:] if len(str) > 2 else "")

assert deFront("Hello") == "llo"
assert deFront("java") == "va"
assert deFront("away") == "aay"
assert deFront("axy") == "ay"
assert deFront("abc") == "abc"
assert deFront("xby") == "by"
assert deFront("ab") == "ab"
assert deFront("ax") == "a"
assert deFront("axb") == "ab"
assert deFront("aaa") == "aa"
assert deFront("xbc") == "bc"
assert deFront("bbb") == "bb"
assert deFront("bazz") == "zz"
assert deFront("ba") == ""
assert deFront("abxyz") == "abxyz"
assert deFront("hi") == ""
assert deFront("his") == "s"
assert deFront("xz") == ""
assert deFront("zzz") == "z"


""" startWord
    Given a string and a second "word" string, we'll say that the word matches the string if it appears at the front
    of the string, except its first char does not need to match exactly. On a match, return the front of the string,
    or otherwise return the empty string. So, so with the string "hippo" the word "hi" returns "hi" and "xip" returns
    "hip". The word will be at least length 1.
"""
def startWord(str, word):
    if not str:
        return str
    match = str[1:len(word)] == word[1:]
    return str[:len(word)] if match else ""

assert startWord("hippo", "hi") == "hi"
assert startWord("hippo", "xip") == "hip"
assert startWord("hippo", "i") == "h"
assert startWord("hippo", "ix") == ""
assert startWord("h", "ix") == ""
assert startWord("", "i") == ""
assert startWord("hip", "zi") == "hi"
assert startWord("hip", "zip") == "hip"
assert startWord("hip", "zig") == ""
assert startWord("h", "z") == "h"
assert startWord("hippo", "xippo") == "hippo"
assert startWord("hippo", "xyz") == ""
assert startWord("hippo", "hip") == "hip"
assert startWord("kitten", "cit") == "kit"
assert startWord("kit", "cit") == "kit"


""" withoutX
    Given a string, if the first or last chars are 'x', return the string without those 'x' chars, and otherwise
    return the string unchanged.
"""
def withoutX(str):
    if not str:
        return str
    else:
        return (str[0] if str[0] != "x" else "") + (str[1:-1]) + (str[-1] if str[-1] != "x" else "")

assert withoutX("xHix") == "Hi"
assert withoutX("xHi") == "Hi"
assert withoutX("Hxix") == "Hxi"
assert withoutX("Hi") == "Hi"
assert withoutX("xxHi") == "xHi"
assert withoutX("Hix") == "Hi"
assert withoutX("xaxbx") == "axb"
assert withoutX("xx") == ""
assert withoutX("x") == ""
assert withoutX("") == ""
assert withoutX("Hello") == "Hello"
assert withoutX("Hexllo") == "Hexllo"


""" withoutX2
    Given a string, if one or both of the first 2 chars is 'x', return the string without those 'x' chars, and
    otherwise return the string unchanged. This is a little harder than it looks.
"""
def withoutX2(str):
    if not str:
        return str
    else:
        return (str[0] if str[0] != "x" else "") + (str[1] if len(str) > 1 and str[1] != "x" else "") + str[2:]

assert withoutX2("xHi") == "Hi"
assert withoutX2("Hxi") == "Hi"
assert withoutX2("Hi") == "Hi"
assert withoutX2("xxHi") == "Hi"
assert withoutX2("Hix") == "Hix"
assert withoutX2("xaxb") == "axb"
assert withoutX2("axxb") == "axb"
assert withoutX2("xx") == ""
assert withoutX2("x") == ""
assert withoutX2("") == ""
assert withoutX2("Hello") == "Hello"
assert withoutX2("Hexllo") == "Hexllo"
assert withoutX2("xHxllo") == "Hxllo"
