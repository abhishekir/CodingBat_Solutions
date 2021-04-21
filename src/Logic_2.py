"""
    https://codingbat.com/python/Logic-2
    Medium boolean logic puzzles -- if else and or not
"""


""" make_bricks
    We want to make a row of bricks that is goal inches long. We have a number of small bricks (1 inch each) and big
    bricks (5 inches each). Return True if it is possible to make the goal by choosing from the given bricks. This
    is a little harder than it looks and can be done without any loops.
"""
def make_bricks(small, big, goal):
    if small >= goal:
        return True
    else:
        big_needed = int(goal / 5)
        goal -= big_needed * 5 if big_needed < big else big * 5
        return goal <= small

assert make_bricks(3, 1, 8) == True
assert make_bricks(3, 1, 9) == False
assert make_bricks(3, 2, 10) == True
assert make_bricks(3, 2, 8) == True
assert make_bricks(3, 2, 9) == False
assert make_bricks(6, 1, 11) == True
assert make_bricks(6, 0, 11) == False
assert make_bricks(1, 4, 11) == True
assert make_bricks(0, 3, 10) == True
assert make_bricks(1, 4, 12) == False
assert make_bricks(3, 1, 7) == True
assert make_bricks(1, 1, 7) == False
assert make_bricks(2, 1, 7) == True
assert make_bricks(7, 1, 11) == True
assert make_bricks(7, 1, 8) == True
assert make_bricks(7, 1, 13) == False
assert make_bricks(43, 1, 46) == True
assert make_bricks(40, 1, 46) == False
assert make_bricks(40, 2, 47) == True
assert make_bricks(40, 2, 50) == True
assert make_bricks(40, 2, 52) == False
assert make_bricks(22, 2, 33) == False
assert make_bricks(0, 2, 10) == True
assert make_bricks(1000000, 1000, 1000100) == True
assert make_bricks(2, 1000000, 100003) == False
assert make_bricks(20, 0, 19) == True
assert make_bricks(20, 0, 21) == False
assert make_bricks(20, 4, 51) == False
assert make_bricks(20, 4, 39) == True


""" lone_sum
    Given 3 int values, a b c, return their sum. However, if one of the values is the same as another of the values, 
    it does not count towards the sum.
"""
def lone_sum(a, b, c):
    return 0 if a==b and b==c else a if b==c else b if a==c else c if a==b else a+b+c

assert lone_sum(1, 2, 3) == 6
assert lone_sum(3, 2, 3) == 2
assert lone_sum(3, 3, 3) == 0
assert lone_sum(9, 2, 2) == 9
assert lone_sum(2, 2, 9) == 9
assert lone_sum(2, 9, 2) == 9
assert lone_sum(2, 9, 3) == 14
assert lone_sum(4, 2, 3) == 9
assert lone_sum(1, 3, 1) == 3


""" lucky_sum
    Given 3 int values, a b c, return their sum. However, if one of the values is 13 then it does not count towards 
    the sum and values to its right do not count. So for example, if b is 13, then both b and c do not count.
"""
def lucky_sum(a, b, c):
    return 0 if a==13 else a if b==13 else a+b if c==13 else a+b+c

assert lucky_sum(1, 2, 3) == 6
assert lucky_sum(1, 2, 13) == 3
assert lucky_sum(1, 13, 3) == 1
assert lucky_sum(1, 13, 13) == 1
assert lucky_sum(6, 5, 2) == 13
assert lucky_sum(13, 2, 3) == 0
assert lucky_sum(13, 2, 13) == 0
assert lucky_sum(13, 13, 2) == 0
assert lucky_sum(9, 4, 13) == 13
assert lucky_sum(8, 13, 2) == 8
assert lucky_sum(7, 2, 1) == 10
assert lucky_sum(3, 3, 13) == 6


""" no_teen_sum
    Given 3 int values, a b c, return their sum. However, if any of the values is a teen -- in the range 13..19 
    inclusive -- then that value counts as 0, except 15 and 16 do not count as a teens. Write a separate helper 
    "def fix_teen(n):"that takes in an int value and returns that value fixed for the teen rule. In this way, you 
    avoid repeating the teen code 3 times (i.e. "decomposition"). Define the helper below and at the same indent 
    level as the main no_teen_sum().
"""
def no_teen_sum(a, b, c):
    return fix_teen(a) + fix_teen(b) + fix_teen(c)

def fix_teen(n):
    return 15 if n==15 else 16 if n==16 else 0 if n<=19 and n>=13 else n

assert no_teen_sum(1, 2, 3) == 6
assert no_teen_sum(2, 13, 1) == 3
assert no_teen_sum(2, 1, 14) == 3
assert no_teen_sum(2, 1, 15) == 18
assert no_teen_sum(2, 1, 16) == 19
assert no_teen_sum(2, 1, 17) == 3
assert no_teen_sum(17, 1, 2) == 3
assert no_teen_sum(2, 15, 2) == 19
assert no_teen_sum(16, 17, 18) == 16
assert no_teen_sum(17, 18, 19) == 0
assert no_teen_sum(15, 16, 1) == 32
assert no_teen_sum(15, 15, 19) == 30
assert no_teen_sum(15, 19, 16) == 31
assert no_teen_sum(5, 17, 18) == 5
assert no_teen_sum(17, 18, 16) == 16
assert no_teen_sum(17, 19, 18) == 0


""" round_sum
    For this problem, we'll round an int value up to the next multiple of 10 if its rightmost digit is 5 or more, so 
    15 rounds up to 20. Alternately, round down to the previous multiple of 10 if its rightmost digit is less than 
    5, so 12 rounds down to 10. Given 3 ints, a b c, return the sum of their rounded values. To avoid code 
    repetition, write a separate helper "def round10(num):" and call it 3 times. Write the helper entirely below and 
    at the same indent level as round_sum().
"""
def round_sum(a, b, c):
    return round10(a) + round10(b) + round10(c)

def round10(n):
    return int(n/10)*10 if n % 10 < 5 else (int(n/10)+1)*10

assert round_sum(16, 17, 18) == 60
assert round_sum(12, 13, 14) == 30
assert round_sum(6, 4, 4) == 10
assert round_sum(4, 6, 5) == 20
assert round_sum(4, 4, 6) == 10
assert round_sum(9, 4, 4) == 10
assert round_sum(0, 0, 1) == 0
assert round_sum(0, 9, 0) == 10
assert round_sum(10, 10, 19) == 40
assert round_sum(20, 30, 40) == 90
assert round_sum(45, 21, 30) == 100
assert round_sum(23, 11, 26) == 60
assert round_sum(23, 24, 25) == 70
assert round_sum(25, 24, 25) == 80
assert round_sum(23, 24, 29) == 70
assert round_sum(11, 24, 36) == 70
assert round_sum(24, 36, 32) == 90
assert round_sum(14, 12, 26) == 50
assert round_sum(12, 10, 24) == 40


""" close_far
    Given three ints, a b c, return True if one of b or c is "close" (differing from a by at most 1), while the 
    other is "far", differing from both other values by 2 or more.
"""
def close_far(a, b, c):
    close = abs(b-a) < 2 or abs(c-a) < 2
    far = (abs(b-a) > 1 and abs(b-c) > 1) or (abs(c-a) > 1 and abs(c-b) > 1)
    return close and far

assert close_far(1, 2, 10) == True
assert close_far(1, 2, 3) == False
assert close_far(4, 1, 3) == True
assert close_far(4, 5, 3) == False
assert close_far(4, 3, 5) == False
assert close_far(-1, 10, 0) == True
assert close_far(0, -1, 10) == True
assert close_far(10, 10, 8) == True
assert close_far(10, 8, 9) == False
assert close_far(8, 9, 10) == False
assert close_far(8, 9, 7) == False
assert close_far(8, 6, 9) == True


""" blackjack
    Given 2 int values greater than 0, return whichever value is nearest to 21 without going over. Return 0 if they
    both go over.
"""
def blackjack(a, b):
    return 0 if a > 21 and b > 21 else a if b > 21 or a <= 21 and 21 - a < 21 - b else b

assert blackjack(19, 21) == 21
assert blackjack(21, 19) == 21
assert blackjack(19, 22) == 19
assert blackjack(22, 19) == 19
assert blackjack(22, 50) == 0
assert blackjack(22, 22) == 0
assert blackjack(33, 1) == 1
assert blackjack(1, 2) == 2
assert blackjack(34, 33) == 0
assert blackjack(17, 19) == 19
assert blackjack(18, 17) == 18
assert blackjack(16, 23) == 16
assert blackjack(3, 4) == 4
assert blackjack(3, 2) == 3
assert blackjack(21, 20) == 21


""" evenlySpaced
    Given three ints, a b c, one of them is small, one is medium and one is large. Return true if the
    three values are evenly spaced, so the difference between small and medium is the same as the difference between
    medium and large.
"""
def evenlySpaced(a, b, c):
    return (a + b + c) / 3 in [a, b, c]

assert evenlySpaced(2, 4, 6) == True
assert evenlySpaced(4, 6, 2) == True
assert evenlySpaced(4, 6, 3) == False
assert evenlySpaced(6, 2, 4) == True
assert evenlySpaced(6, 2, 8) == False
assert evenlySpaced(2, 2, 2) == True
assert evenlySpaced(2, 2, 3) == False
assert evenlySpaced(9, 10, 11) == True
assert evenlySpaced(10, 9, 11) == True
assert evenlySpaced(10, 9, 9) == False
assert evenlySpaced(2, 4, 4) == False
assert evenlySpaced(2, 2, 4) == False
assert evenlySpaced(3, 6, 12) == False
assert evenlySpaced(12, 3, 6) == False


""" make_chocolate
    We want make a package of goal kilos of chocolate. We have small bars (1 kilo each) and big bars (5 kilos each). 
    Return the number of small bars to use, assuming we always use big bars before small bars. Return -1 if it can't 
    be done.
"""
def make_chocolate(small, big, goal):
    big_needed = int(goal / 5)
    goal -= big*5 if big_needed > big else big_needed*5
    return goal if goal <= small else -1

assert make_chocolate(4, 1, 9) == 4
assert make_chocolate(4, 1, 10) == -1
assert make_chocolate(4, 1, 7) == 2
assert make_chocolate(6, 2, 7) == 2
assert make_chocolate(4, 1, 5) == 0
assert make_chocolate(4, 1, 4) == 4
assert make_chocolate(5, 4, 9) == 4
assert make_chocolate(9, 3, 18) == 3
assert make_chocolate(3, 1, 9) == -1
assert make_chocolate(1, 2, 7) == -1
assert make_chocolate(1, 2, 6) == 1
assert make_chocolate(1, 2, 5) == 0
assert make_chocolate(6, 1, 10) == 5
assert make_chocolate(6, 1, 11) == 6
assert make_chocolate(6, 1, 12) == -1
assert make_chocolate(6, 1, 13) == -1
assert make_chocolate(6, 2, 10) == 0
assert make_chocolate(6, 2, 11) == 1
assert make_chocolate(6, 2, 12) == 2
assert make_chocolate(60, 100, 550) == 50
assert make_chocolate(1000, 1000000, 5000006) == 6
assert make_chocolate(7, 1, 12) == 7
assert make_chocolate(7, 1, 13) == -1
assert make_chocolate(7, 2, 13) == 3
