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







