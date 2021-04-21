"""
    https://codingbat.com/python/Logic-1
    Basic boolean logic puzzles -- if else and or not
"""


""" cigar_party
    When squirrels get together for a party, they like to have cigars. A squirrel party is successful when the
    number of cigars is between 40 and 60, inclusive. Unless it is the weekend, in which case there is no upper
    bound on the number of cigars. Return True if the party with the given values is successful, or False otherwise.
"""
def cigar_party(cigars, is_weekend):
    return cigars >= 40 and (is_weekend or cigars <= 60)

assert cigar_party(30, False) == False
assert cigar_party(50, False) == True
assert cigar_party(70, True) == True
assert cigar_party(30, True) == False
assert cigar_party(50, True) == True
assert cigar_party(60, False) == True
assert cigar_party(61, False) == False
assert cigar_party(40, False) == True
assert cigar_party(39, False) == False
assert cigar_party(40, True) == True
assert cigar_party(39, True) == False


""" date_fashion
    You and your date are trying to get a table at a restaurant. The parameter "you" is the stylishness of your 
    clothes, in the range 0..10, and "date" is the stylishness of your date's clothes. The result getting the table 
    is encoded as an int value with 0=no, 1=maybe, 2=yes. If either of you is very stylish, 8 or more, then the 
    result is 2 (yes). With the exception that if either of you has style of 2 or less, then the result is 0 (no). 
    Otherwise the result is 1 (maybe).
"""
def date_fashion(you, date):
    if you <= 2 or date <= 2:
        return 0
    elif you >= 8 or date >= 8:
        return 2
    else:
        return 1

assert date_fashion(5, 10) == 2
assert date_fashion(5, 2) == 0
assert date_fashion(5, 5) == 1
assert date_fashion(3, 3) == 1
assert date_fashion(10, 2) == 0
assert date_fashion(2, 9) == 0
assert date_fashion(9, 9) == 2
assert date_fashion(10, 5) == 2
assert date_fashion(2, 2) == 0
assert date_fashion(3, 7) == 1
assert date_fashion(2, 7) == 0
assert date_fashion(6, 2) == 0


""" squirrel_play
    The squirrels in Palo Alto spend most of the day playing. In particular, they play if the temperature is between
     60 and 90 (inclusive). Unless it is summer, then the upper limit is 100 instead of 90. Given an int temperature 
     and a boolean is_summer, return True if the squirrels play and False otherwise.
"""
def squirrel_play(temp, is_summer):
    return temp >= 60 and ((is_summer and temp <= 100) or temp <= 90)

assert squirrel_play(70, False) == True
assert squirrel_play(95, False) == False
assert squirrel_play(95, True) == True
assert squirrel_play(90, False) == True
assert squirrel_play(90, True) == True
assert squirrel_play(50, False) == False
assert squirrel_play(50, True) == False
assert squirrel_play(100, False) == False
assert squirrel_play(100, True) == True
assert squirrel_play(105, True) == False
assert squirrel_play(59, False) == False
assert squirrel_play(59, True) == False
assert squirrel_play(60, False) == True


""" caught_speeding
    You are driving a little too fast, and a police officer stops you. Write code to compute the result, encoded as 
    an int value: 0=no ticket, 1=small ticket, 2=big ticket. If speed is 60 or less, the result is 0. If speed is 
    between 61 and 80 inclusive, the result is 1. If speed is 81 or more, the result is 2. Unless it is your 
    birthday -- on that day, your speed can be 5 higher in all cases.
"""
def caught_speeding(speed, is_birthday):
    if is_birthday:
        speed -= 5
    if speed <= 60:
        return 0
    elif speed <= 80:
        return 1
    else:
        return 2

assert caught_speeding(60, False) == 0
assert caught_speeding(65, False) == 1
assert caught_speeding(65, True) == 0
assert caught_speeding(80, False) == 1
assert caught_speeding(85, False) == 2
assert caught_speeding(85, True) == 1
assert caught_speeding(70, False) == 1
assert caught_speeding(75, False) == 1
assert caught_speeding(75, True) == 1
assert caught_speeding(40, False) == 0
assert caught_speeding(40, True) == 0
assert caught_speeding(90, False) == 2


""" sorta_sum
    Given 2 ints, a and b, return their sum. However, sums in the range 10..19 inclusive, are forbidden, so in that 
    case just return 20.
"""
def sorta_sum(a, b):
    sum = a+b
    return 20 if sum >= 10 and sum < 20 else sum

assert sorta_sum(3, 4) == 7
assert sorta_sum(9, 4) == 20
assert sorta_sum(10, 11) == 21
assert sorta_sum(12, -3) == 9
assert sorta_sum(-3, 12) == 9
assert sorta_sum(4, 5) == 9
assert sorta_sum(4, 6) == 20
assert sorta_sum(14, 7) == 21
assert sorta_sum(14, 6) == 20


""" alarm_clock
    Given a day of the week encoded as 0=Sun, 1=Mon, 2=Tue, ...6=Sat, and a boolean indicating if we are on 
    vacation, return a string of the form "7:00" indicating when the alarm clock should ring. Weekdays, the alarm 
    should be "7:00" and on the weekend it should be "10:00". Unless we are on vacation -- then on weekdays it 
    should be "10:00" and weekends it should be "off".
"""
def alarm_clock(day, vacation):
    seven = "7:00"
    ten = "10:00"
    off = "off"
    is_weekend = day == 0 or day == 6
    return off if is_weekend and vacation else ten if is_weekend or vacation else seven

assert alarm_clock(1, False) == '7:00'
assert alarm_clock(5, False) == '7:00'
assert alarm_clock(0, False) == '10:00'
assert alarm_clock(6, False) == '10:00'
assert alarm_clock(0, True) == 'off'
assert alarm_clock(6, True) == 'off'
assert alarm_clock(1, True) == '10:00'
assert alarm_clock(3, True) == '10:00'
assert alarm_clock(5, True) == '10:00'


""" love6
    The number 6 is a truly great number. Given two int values, a and b, return True if either one is 6. Or if their 
    sum or difference is 6.
"""
def love6(a, b):
    return a == 6 or b == 6 or a+b == 6 or abs(a-b) == 6

assert love6(6, 4) == True
assert love6(4, 5) == False
assert love6(1, 5) == True
assert love6(1, 6) == True
assert love6(1, 8) == False
assert love6(1, 7) == True
assert love6(7, 5) == False
assert love6(8, 2) == True
assert love6(6, 6) == True
assert love6(-6, 2) == False
assert love6(-4, -10) == True
assert love6(-7, 1) == False
assert love6(7, -1) == True
assert love6(-6, 12) == True
assert love6(-2, -4) == False
assert love6(7, 1) == True
assert love6(0, 9) == False
assert love6(8, 3) == False
assert love6(3, 3) == True
assert love6(3, 4) == False


""" in1to10
    Given a number n, return True if n is in the range 1..10, inclusive. Unless outside_mode is True, in which case 
    return True if the number is less or equal to 1, or greater or equal to 10.
"""
def in1to10(n, outside_mode):
    return n <= 1 or n >= 10 if outside_mode else n >= 1 and n <= 10

assert in1to10(5, False) == True
assert in1to10(11, False) == False
assert in1to10(11, True) == True
assert in1to10(10, False) == True
assert in1to10(10, True) == True
assert in1to10(9, False) == True
assert in1to10(9, True) == False
assert in1to10(1, False) == True
assert in1to10(1, True) == True
assert in1to10(0, False) == False
assert in1to10(0, True) == True
assert in1to10(-1, False) == False
assert in1to10(-1, True) == True
assert in1to10(99, False) == False
assert in1to10(-99, True) == True


""" specialEleven
    We'll say a number is special if it is a multiple of 11 or if it is one more than a multiple of 11. Return true
    if the given non-negative number is special.
"""
def specialEleven(n):
    return n % 11 == 0 or n % 11 == 1

assert specialEleven(22) == True
assert specialEleven(23) == True
assert specialEleven(24) == False
assert specialEleven(21) == False
assert specialEleven(11) == True
assert specialEleven(12) == True
assert specialEleven(10) == False
assert specialEleven(9) == False
assert specialEleven(8) == False
assert specialEleven(0) == True
assert specialEleven(1) == True
assert specialEleven(2) == False
assert specialEleven(121) == True
assert specialEleven(122) == True
assert specialEleven(123) == False
assert specialEleven(46) == False
assert specialEleven(49) == False
assert specialEleven(52) == False
assert specialEleven(54) == False
assert specialEleven(55) == True


""" more20
    Return true if the given non-negative number is 1 or 2 more than a multiple of 20.
"""
def more20(n):
    return n % 20 == 1 or n % 20 == 2

assert more20(20) == False
assert more20(21) == True
assert more20(22) == True
assert more20(23) == False
assert more20(25) == False
assert more20(30) == False
assert more20(31) == False
assert more20(59) == False
assert more20(60) == False
assert more20(61) == True
assert more20(62) == True
assert more20(1020) == False
assert more20(1021) == True
assert more20(1000) == False
assert more20(1001) == True
assert more20(50) == False
assert more20(55) == False
assert more20(40) == False
assert more20(41) == True
assert more20(39) == False
assert more20(42) == True


""" old35
    Return true if the given non-negative number is a multiple of 3 or 5, but not both.
"""
def old35(n):
    return (n % 3 == 0) ^ (n % 5 == 0)

assert old35(3) == True
assert old35(10) == True
assert old35(15) == False
assert old35(5) == True
assert old35(9) == True
assert old35(8) == False
assert old35(7) == False
assert old35(6) == True
assert old35(17) == False
assert old35(18) == True
assert old35(29) == False
assert old35(20) == True
assert old35(21) == True
assert old35(22) == False
assert old35(45) == False
assert old35(99) == True


""" less20
    Return true if the given non-negative number is 1 or 2 less than a multiple of 20. So for example 38 and 39
    return true, but 40 returns false.
"""
def less20(n):
    return n % 20 == 18 or n % 20 == 19

assert less20(18) == True
assert less20(19) == True
assert less20(20) == False
assert less20(8) == False
assert less20(17) == False
assert less20(23) == False
assert less20(25) == False
assert less20(30) == False
assert less20(31) == False
assert less20(58) == True
assert less20(59) == True
assert less20(60) == False
assert less20(61) == False
assert less20(62) == False
assert less20(1017) == False
assert less20(1018) == True
assert less20(1019) == True
assert less20(1020) == False
assert less20(1021) == False
assert less20(1022) == False
assert less20(1023) == False
assert less20(37) == False


""" near_ten
    Given a non-negative number "num", return True if num is within 2 of a multiple of 10.
"""
def near_ten(num):
    return num % 10 <= 2 or num % 10 >= 8

assert near_ten(12) == True
assert near_ten(17) == False
assert near_ten(19) == True
assert near_ten(31) == True
assert near_ten(6) == False
assert near_ten(10) == True
assert near_ten(11) == True
assert near_ten(21) == True
assert near_ten(22) == True
assert near_ten(23) == False
assert near_ten(54) == False
assert near_ten(155) == False
assert near_ten(158) == True
assert near_ten(3) == False
assert near_ten(1) == True


""" teenSum
    Given 2 ints, a and b, return their sum. However, "teen" values in the range 13..19 inclusive, are extra lucky.
    So if either value is a teen, just return 19.
"""
def teenSum(a, b):
    return 19 if 13 <= a <= 19 or 13 <= b <= 19 else a + b

assert teenSum(3, 4) == 7
assert teenSum(10, 13) == 19
assert teenSum(13, 2) == 19
assert teenSum(3, 19) == 19
assert teenSum(13, 13) == 19
assert teenSum(10, 10) == 20
assert teenSum(6, 14) == 19
assert teenSum(15, 2) == 19
assert teenSum(19, 19) == 19
assert teenSum(19, 20) == 19
assert teenSum(2, 18) == 19
assert teenSum(12, 4) == 16
assert teenSum(2, 20) == 22
assert teenSum(2, 17) == 19
assert teenSum(2, 16) == 19
assert teenSum(6, 7) == 13


""" answerCell
    Your cell phone rings. Return true if you should answer it. Normally you answer, except in the morning you only
    answer if it is your mom calling. In all cases, if you are asleep, you do not answer.
"""
def answerCell(isMorning, isMom, isAsleep):
    return True if not isAsleep and (isMom or not isMorning) else False

assert answerCell(False, False, False) == True
assert answerCell(False, False, True) == False
assert answerCell(True, False, False) == False
assert answerCell(True, True, False) == True
assert answerCell(False, True, False) == True
assert answerCell(True, True, True) == False


""" teaParty
    We are having a party with amounts of tea and candy. Return the int outcome of the party encoded as 0=bad,
    1=good, or 2=great. A party is good (1) if both tea and candy are at least 5. However, if either tea or candy is
    at least double the amount of the other one, the party is great (2). However, in all cases, if either tea or
    candy is less than 5, the party is always bad (0).
"""
def teaParty(tea, candy):
    return 0 if tea < 5 or candy < 5 else 2 if tea >= 2 * candy or candy >= 2 * tea else 1

assert teaParty(6, 8) == 1
assert teaParty(3, 8) == 0
assert teaParty(20, 6) == 2
assert teaParty(12, 6) == 2
assert teaParty(11, 6) == 1
assert teaParty(11, 4) == 0
assert teaParty(4, 5) == 0
assert teaParty(5, 5) == 1
assert teaParty(6, 6) == 1
assert teaParty(5, 10) == 2
assert teaParty(5, 9) == 1
assert teaParty(10, 4) == 0
assert teaParty(10, 20) == 2


""" fizzString
    Given a string str, if the string starts with "f" return "Fizz". If the string ends with "b" return "Buzz". If
    both the "f" and "b" conditions are true, return "FizzBuzz". In all other cases, return the string unchanged.
"""
def fizzString(str):
    res = ("Fizz" if str[:1] == "f" else "") + ("Buzz" if str[-1:] == "b" else "")
    return res if res else str

assert fizzString("fig") == "Fizz"
assert fizzString("dib") == "Buzz"
assert fizzString("fib") == "FizzBuzz"
assert fizzString("abc") == "abc"
assert fizzString("fooo") == "Fizz"
assert fizzString("booo") == "booo"
assert fizzString("ooob") == "Buzz"
assert fizzString("fooob") == "FizzBuzz"
assert fizzString("f") == "Fizz"
assert fizzString("b") == "Buzz"
assert fizzString("") == ""
assert fizzString("abcb") == "Buzz"
assert fizzString("Hello") == "Hello"
assert fizzString("Hellob") == "Buzz"
assert fizzString("af") == "af"
assert fizzString("bf") == "bf"
assert fizzString("fb") == "FizzBuzz"


""" fizzString2
    Given an int n, return the string form of the number followed by "!". So the int 6 yields "6!". Except if the
    number is divisible by 3 use "Fizz" instead of the number, and if the number is divisible by 5 use "Buzz", and if
    divisible by both 3 and 5, use "FizzBuzz".
"""
def fizzString2(n):
    s = ("Fizz" if n % 3 == 0 else "") + ("Buzz" if n % 5 == 0 else "")
    return (s if s else str(n)) + "!"

assert fizzString2(1) == "1!"
assert fizzString2(2) == "2!"
assert fizzString2(3) == "Fizz!"
assert fizzString2(4) == "4!"
assert fizzString2(5) == "Buzz!"
assert fizzString2(6) == "Fizz!"
assert fizzString2(7) == "7!"
assert fizzString2(8) == "8!"
assert fizzString2(9) == "Fizz!"
assert fizzString2(15) == "FizzBuzz!"
assert fizzString2(16) == "16!"
assert fizzString2(18) == "Fizz!"
assert fizzString2(19) == "19!"
assert fizzString2(21) == "Fizz!"
assert fizzString2(44) == "44!"
assert fizzString2(45) == "FizzBuzz!"
assert fizzString2(100) == "Buzz!"


""" twoAsOne
    Given three ints, a b c, return true if it is possible to add two of the ints to get the third.
"""
def twoAsOne(a, b, c):
    return a + b == c or a + c == b or b + c == a

assert twoAsOne(1, 2, 3) == True
assert twoAsOne(3, 1, 2) == True
assert twoAsOne(3, 2, 2) == False
assert twoAsOne(2, 3, 1) == True
assert twoAsOne(5, 3, -2) == True
assert twoAsOne(5, 3, -3) == False
assert twoAsOne(2, 5, 3) == True
assert twoAsOne(9, 5, 5) == False
assert twoAsOne(9, 4, 5) == True
assert twoAsOne(5, 4, 9) == True
assert twoAsOne(3, 3, 0) == True
assert twoAsOne(3, 3, 2) == False


""" inOrder
    Given three ints, a b c, return true if b is greater than a, and c is greater than b. However, with the exception
    that if "bOk" is true, b does not need to be greater than a.
"""

def inOrder(a, b, c, bOk):
    return c > b and (True if bOk else b > a)

assert inOrder(1, 2, 4, False) == True
assert inOrder(1, 2, 1, False) == False
assert inOrder(1, 1, 2, True) == True
assert inOrder(3, 2, 4, False) == False
assert inOrder(2, 3, 4, False) == True
assert inOrder(3, 2, 4, True) == True
assert inOrder(4, 2, 2, True) == False
assert inOrder(4, 5, 2, True) == False
assert inOrder(2, 4, 6, True) == True
assert inOrder(7, 9, 10, False) == True
assert inOrder(7, 5, 6, True) == True
assert inOrder(7, 5, 4, True) == False


""" inOrderEqual
    Given three ints, a b c, return true if they are in strict increasing order, such as 2 5 11, or 5 6 7, but not 6
    5 7 or 5 5 7. However, with the exception that if "equalOk" is true, equality is allowed, such as 5 5 7 or 5 5 5.
"""
def inOrderEqual(a, b, c, equalOk):
    return a <= b <= c if equalOk else a < b < c

assert inOrderEqual(2, 5, 11, False) == True
assert inOrderEqual(5, 7, 6, False) == False
assert inOrderEqual(5, 5, 7, True) == True
assert inOrderEqual(5, 5, 7, False) == False
assert inOrderEqual(2, 5, 4, False) == False
assert inOrderEqual(3, 4, 3, False) == False
assert inOrderEqual(3, 4, 4, False) == False
assert inOrderEqual(3, 4, 3, True) == False
assert inOrderEqual(3, 4, 4, True) == True
assert inOrderEqual(1, 5, 5, True) == True
assert inOrderEqual(5, 5, 5, True) == True
assert inOrderEqual(2, 2, 1, True) == False
assert inOrderEqual(9, 2, 2, True) == False
assert inOrderEqual(0, 1, 0, True) == False


""" lastDigit
    Given three ints, a b c, return true if two or more of them have the same rightmost digit. The ints are
    non-negative.
"""
def lastDigit(a, b, c):
    return a % 10 == b % 10 or a % 10 == c % 10 or b % 10 == c % 10

assert lastDigit(23, 19, 13) == True
assert lastDigit(23, 19, 12) == False
assert lastDigit(23, 19, 3) == True
assert lastDigit(23, 19, 39) == True
assert lastDigit(1, 2, 3) == False
assert lastDigit(1, 1, 2) == True
assert lastDigit(1, 2, 2) == True
assert lastDigit(14, 25, 43) == False
assert lastDigit(14, 25, 45) == True
assert lastDigit(248, 106, 1002) == False
assert lastDigit(248, 106, 1008) == True
assert lastDigit(10, 11, 20) == True
assert lastDigit(0, 11, 0) == True


""" lessBy10
    Given three ints, a b c, return true if one of them is 10 or more less than one of the others.
"""
def lessBy10(a, b, c):
    smallest = min(a, b, c)
    largest = max(a, b, c)
    return largest - smallest >= 10

assert lessBy10(1, 7, 11) == True
assert lessBy10(1, 7, 10) == False
assert lessBy10(11, 1, 7) == True
assert lessBy10(10, 7, 1) == False
assert lessBy10(-10, 2, 2) == True
assert lessBy10(2, 11, 11) == False
assert lessBy10(3, 3, 30) == True
assert lessBy10(3, 3, 3) == False
assert lessBy10(10, 1, 11) == True
assert lessBy10(10, 11, 1) == True
assert lessBy10(10, 11, 2) == False
assert lessBy10(3, 30, 3) == True
assert lessBy10(2, 2, -8) == True
assert lessBy10(2, 8, 12) == True


""" withoutDoubles
    Return the sum of two 6-sided dice rolls, each in the range 1..6. However, if noDoubles is true, if the two dice
    show the same value, increment one die to the next value, wrapping around to 1 if its value was 6.
"""
def withoutDoubles(die1, die2, noDoubles):
    if noDoubles and die1 == die2:
        die1 = 1 if die1 == 6 else die1 + 1
    return die1 + die2

assert withoutDoubles(2, 3, True) == 5
assert withoutDoubles(3, 3, True) == 7
assert withoutDoubles(3, 3, False) == 6
assert withoutDoubles(2, 3, False) == 5
assert withoutDoubles(5, 4, True) == 9
assert withoutDoubles(5, 4, False) == 9
assert withoutDoubles(5, 5, True) == 11
assert withoutDoubles(5, 5, False) == 10
assert withoutDoubles(6, 6, True) == 7
assert withoutDoubles(6, 6, False) == 12
assert withoutDoubles(1, 6, True) == 7
assert withoutDoubles(6, 1, False) == 7


""" maxMod5
    Given two int values, return whichever value is larger. However if the two values have the same remainder when
    divided by 5, then the return the smaller value. However, in all cases, if the two values are the same, return 0.
"""
def maxMod5(a, b):
    return 0 if a == b else min(a, b) if a % 5 == b % 5 else max(a, b)

assert maxMod5(2, 3) == 3
assert maxMod5(6, 2) == 6
assert maxMod5(3, 2) == 3
assert maxMod5(8, 12) == 12
assert maxMod5(7, 12) == 7
assert maxMod5(11, 6) == 6
assert maxMod5(2, 7) == 2
assert maxMod5(7, 7) == 0
assert maxMod5(9, 1) == 9
assert maxMod5(9, 14) == 9
assert maxMod5(1, 2) == 2


""" redTicket
    You have a red lottery ticket showing ints a, b, and c, each of which is 0, 1, or 2. If they are all the value 2,
    the result is 10. Otherwise if they are all the same, the result is 5. Otherwise so long as both b and c are
    different from a, the result is 1. Otherwise the result is 0.
"""
def redTicket(a, b, c):
    return 10 if a == b == c == 2 else 5 if a == b == c else 1 if a != b and a != c else 0

assert redTicket(2, 2, 2) == 10
assert redTicket(2, 2, 1) == 0
assert redTicket(0, 0, 0) == 5
assert redTicket(2, 0, 0) == 1
assert redTicket(1, 1, 1) == 5
assert redTicket(1, 2, 1) == 0
assert redTicket(1, 2, 0) == 1
assert redTicket(0, 2, 2) == 1
assert redTicket(1, 2, 2) == 1
assert redTicket(0, 2, 0) == 0
assert redTicket(1, 1, 2) == 0


""" greenTicket
    You have a green lottery ticket, with ints a, b, and c on it. If the numbers are all different from each other,
    the result is 0. If all of the numbers are the same, the result is 20. If two of the numbers are the same, the
    result is 10.
"""
def greenTicket(a, b, c):
    return 20 if a == b == c else 10 if a == b or a == c or b == c else 0

assert greenTicket(1, 2, 3) == 0
assert greenTicket(2, 2, 2) == 20
assert greenTicket(1, 1, 2) == 10
assert greenTicket(2, 1, 1) == 10
assert greenTicket(1, 2, 1) == 10
assert greenTicket(3, 2, 1) == 0
assert greenTicket(0, 0, 0) == 20
assert greenTicket(2, 0, 0) == 10
assert greenTicket(0, 9, 10) == 0
assert greenTicket(0, 10, 0) == 10
assert greenTicket(9, 9, 9) == 20
assert greenTicket(9, 0, 9) == 10


""" blueTicket
    You have a blue lottery ticket, with ints a, b, and c on it. This makes three pairs, which we'll call ab, bc, and
    ac. Consider the sum of the numbers in each pair. If any pair sums to exactly 10, the result is 10. Otherwise if
    the ab sum is exactly 10 more than either bc or ac sums, the result is 5. Otherwise the result is 0.
"""
def blueTicket(a, b, c):
    ab = a + b
    ac = a + c
    bc = b + c
    return 10 if ab == 10 or ac == 10 or bc == 10 else 5 if ab == bc + 10 or ab == ac + 10 else 0

assert blueTicket(9, 1, 0) == 10
assert blueTicket(9, 2, 0) == 0
assert blueTicket(6, 1, 4) == 10
assert blueTicket(6, 1, 5) == 0
assert blueTicket(10, 0, 0) == 10
assert blueTicket(15, 0, 5) == 5
assert blueTicket(5, 15, 5) == 10
assert blueTicket(4, 11, 1) == 5
assert blueTicket(13, 2, 3) == 5
assert blueTicket(8, 4, 3) == 0
assert blueTicket(8, 4, 2) == 10
assert blueTicket(8, 4, 1) == 0


""" shareDigit
    Given two ints, each in the range 10..99, return true if there is a digit that appears in both numbers, such as
    the 2 in 12 and 23.
"""
def shareDigit(a, b):
    a1 = int(a / 10)
    a2 = a % 10
    b1 = int(b / 10)
    b2 = b % 10
    return a1 == b1 or a1 == b2 or a2 == b1 or a2 == b2

assert shareDigit(12, 23) == True
assert shareDigit(12, 43) == False
assert shareDigit(12, 44) == False
assert shareDigit(23, 12) == True
assert shareDigit(23, 24) == True
assert shareDigit(23, 39) == True
assert shareDigit(23, 19) == False
assert shareDigit(30, 90) == True
assert shareDigit(30, 91) == False
assert shareDigit(55, 55) == True
assert shareDigit(55, 44) == False


""" sumLimit
    Given 2 non-negative ints, a and b, return their sum, so long as the sum has the same number of digits as a. If
    the sum has more digits than a, just return a without b.
"""
def sumLimit(a, b):
    return a + b if len(str(a)) == len(str(a+b)) else a

assert sumLimit(2, 3) == 5
assert sumLimit(8, 3) == 8
assert sumLimit(8, 1) == 9
assert sumLimit(11, 39) == 50
assert sumLimit(11, 99) == 11
assert sumLimit(0, 0) == 0
assert sumLimit(99, 0) == 99
assert sumLimit(99, 1) == 99
assert sumLimit(123, 1) == 124
assert sumLimit(1, 123) == 1
assert sumLimit(23, 60) == 83
assert sumLimit(23, 80) == 23
assert sumLimit(9000, 1) == 9001
assert sumLimit(90000000, 1) == 90000001
assert sumLimit(9000, 1000) == 9000
