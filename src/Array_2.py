"""
    https://codingbat.com/python/List-2
    Medium python list problems -- 1 loop.. Use a[0], a[1], ... to access elements in a list, len(a) is the length.
"""


""" count_evens
    Return the number of even ints in the given array. Note: the % "mod" operator computes the remainder, e.g. 5 % 2
    is 1.
"""
def count_evens(nums):
    count = 0;
    for i in range(len(nums)):
        if nums[i] % 2 == 0: count += 1
    return count

assert count_evens([2, 1, 2, 3, 4]) == 3
assert count_evens([2, 2, 0]) == 3
assert count_evens([1, 3, 5]) == 0
assert count_evens([]) == 0
assert count_evens([11, 9, 0, 1]) == 1
assert count_evens([2, 11, 9, 0]) == 2
assert count_evens([2]) == 1
assert count_evens([2, 5, 12]) == 2


""" big_diff
    Given an array length 1 or more of ints, return the difference between the largest and smallest values in the 
    array.
"""
def big_diff(nums):
    small = nums[0]
    big = nums[0]
    for i in range(len(nums)):
        small = min(small, nums[i])
        big = max(big, nums[i])
    return big-small

assert big_diff([10, 3, 5, 6]) == 7
assert big_diff([7, 2, 10, 9]) == 8
assert big_diff([2, 10, 7, 2]) == 8
assert big_diff([2, 10]) == 8
assert big_diff([10, 2]) == 8
assert big_diff([10, 0]) == 10
assert big_diff([2, 3]) == 1
assert big_diff([2, 2]) == 0
assert big_diff([2]) == 0
assert big_diff([5, 1, 6, 1, 9, 9]) == 8
assert big_diff([7, 6, 8, 5]) == 3
assert big_diff([7, 7, 6, 8, 5, 5, 6]) == 3


""" centered_average
    Return the "centered" average of an array of ints, which we'll say is the mean average of the values, except 
    ignoring the largest and smallest values in the array. If there are multiple copies of the smallest value, 
    ignore just one copy, and likewise for the largest value. Use int division to produce the final average. You may 
    assume that the array is length 3 or more.
"""
def centered_average(nums):
    big = nums[0]
    small = nums[0]
    sum = 0

    for i in range(len(nums)):
        big = max(big, nums[i])
        small = min(small, nums[i])
        sum += nums[i]

    return int((sum - big - small) / (len(nums)-2))

assert centered_average([1, 2, 3, 4, 100]) == 3
assert centered_average([1, 1, 5, 5, 10, 8, 7]) == 5
assert centered_average([-10, -4, -2, -4, -2, 0]) == -3
assert centered_average([5, 3, 4, 6, 2]) == 4
assert centered_average([5, 3, 4, 0, 100]) == 4
assert centered_average([100, 0, 5, 3, 4]) == 4
assert centered_average([4, 0, 100]) == 4
assert centered_average([0, 2, 3, 4, 100]) == 3
assert centered_average([1, 1, 100]) == 1
assert centered_average([7, 7, 7]) == 7
assert centered_average([1, 7, 8]) == 7
assert centered_average([1, 1, 99, 99]) == 50
assert centered_average([1000, 0, 1, 99]) == 50
assert centered_average([4, 4, 4, 4, 5]) == 4
assert centered_average([4, 4, 4, 1, 5]) == 4
assert centered_average([6, 4, 8, 12, 3]) == 6


""" sum13
    Return the sum of the numbers in the array, returning 0 for an empty array. Except the number 13 is very 
    unlucky, so it does not count and numbers that come immediately after a 13 also do not count.
"""
def sum13(nums):
    seen13 = False
    res = 0
    for i in range(len(nums)):
        if nums[i] == 13:
            seen13 = True
        elif seen13:
            seen13 = False
        else:
            res += nums[i]
    return res

assert sum13([1, 2, 2, 1]) == 6
assert sum13([1, 1]) == 2
assert sum13([1, 2, 2, 1, 13]) == 6
assert sum13([1, 2, 13, 2, 1, 13]) == 4
assert sum13([13, 1, 2, 13, 2, 1, 13]) == 3
assert sum13([]) == 0
assert sum13([13]) == 0
assert sum13([13, 13]) == 0
assert sum13([13, 0, 13]) == 0
assert sum13([13, 1, 13]) == 0
assert sum13([5, 7, 2]) == 14
assert sum13([5, 13, 2]) == 5
assert sum13([0]) == 0
assert sum13([13, 0]) == 0
assert sum13([13, 13, 1]) == 0
assert sum13([2, 13, 13, 1]) == 2


""" sum67
    Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to
    the next 7 (every 6 will be followed by at least one 7). Return 0 for no numbers.
"""
def sum67(nums):
    seen6 = False
    sum = 0

    for i in range(len(nums)):
        if seen6:
            if nums[i] == 7: seen6 = False
            else: continue
        else:
            if nums[i] == 6: seen6 = True
            else: sum += nums[i]

    return sum

assert sum67([1, 2, 2]) == 5
assert sum67([1, 2, 2, 6, 99, 99, 7]) == 5
assert sum67([1, 1, 6, 7, 2]) == 4
assert sum67([1, 6, 2, 2, 7, 1, 6, 99, 99, 7]) == 2
assert sum67([1, 6, 2, 6, 2, 7, 1, 6, 99, 99, 7]) == 2
assert sum67([2, 7, 6, 2, 6, 7, 2, 7]) == 18
assert sum67([7, 6, 7]) == 7
assert sum67([6, 7, 6, 7]) == 0
assert sum67([6, 1, 7, 6, 7]) == 0
assert sum67([6, 1, 7, 6, 2, 7]) == 0
assert sum67([6, 1, 2, 3, 7, 6, 7]) == 0
assert sum67([6, 1, 2, 3, 7, 6, 4, 5, 6, 7]) == 0
assert sum67([6, 1, 2, 3, 7, 6, 4, 5, 6, 7, 8]) == 8
assert sum67([7, 6, 1, 2, 3, 7, 6, 4, 5, 6, 7, 8]) == 15
assert sum67([6, 7]) == 0
assert sum67([7]) == 7
assert sum67([7, 2, 6, 7]) == 9
assert sum67([7, 2, 6, 7, 7, 2, 6, 7]) == 18
assert sum67([7, 2, 6, 7, 2, 6, 7]) == 11
assert sum67([2, 7, 6, 2, 6, 2, 7]) == 9
assert sum67([1, 6, 7, 7]) == 8
assert sum67([6, 7, 1, 6, 7, 7]) == 8
assert sum67([6, 8, 1, 6, 7]) == 0
assert sum67([6, 6, 7]) == 0
assert sum67([6, 6, 6, 6, 7, 7]) == 7
assert sum67([6, 6, 6, 6, 7, 7, 6, 2, 6, 7]) == 7
assert sum67([]) == 0
assert sum67([6, 7, 11]) == 11
assert sum67([11, 6, 7, 11]) == 22
assert sum67([2, 2, 6, 7, 7]) == 11


""" has22
    Given an array of ints, return True if the array contains a 2 next to a 2 somewhere.
"""
def has22(nums):
    seen2 = False

    for i in range(len(nums)):
        if nums[i]  == 2:
            if seen2: return True
            else: seen2 = True
        else:
            seen2 = False

    return False

assert has22([1, 2, 2]) == True
assert has22([1, 2, 1, 2]) == False
assert has22([2, 1, 2]) == False
assert has22([2, 2, 1, 2]) == True
assert has22([1, 3, 2]) == False
assert has22([1, 3, 2, 2]) == True
assert has22([2, 3, 2, 2]) == True
assert has22([4, 2, 4, 2, 2, 5]) == True
assert has22([1, 2]) == False
assert has22([2, 2]) == True
assert has22([2]) == False
assert has22([]) == False
assert has22([3, 3, 2, 2]) == True
assert has22([5, 2, 5, 2]) == False


""" lucky13
    Given an array of ints, return true if the array contains no 1's and no 3's.
"""
def lucky13(nums):
    for i in range(len(nums)):
        if nums[i] == 1 or nums[i] == 3:
            return False
    return True

assert lucky13([0, 2, 4]) == True
assert lucky13([1, 2, 3]) == False
assert lucky13([1, 2, 4]) == False
assert lucky13([2, 7, 2, 8]) == True
assert lucky13([2, 7, 1, 8]) == False
assert lucky13([3, 7, 2, 8]) == False
assert lucky13([2, 7, 2, 1]) == False
assert lucky13([1, 2]) == False
assert lucky13([2, 2]) == True
assert lucky13([2]) == True
assert lucky13([3]) == False
assert lucky13([]) == True


""" sum28
    Given an array of ints, return true if the sum of all the 2's in the array is exactly 8.
"""
def sum28(nums):
    s = 0
    for i in range(len(nums)):
        if nums[i] == 2:
            s += 2
    return s == 8

assert sum28([2, 3, 2, 2, 4, 2]) == True
assert sum28([2, 3, 2, 2, 4, 2, 2]) == False
assert sum28([1, 2, 3, 4]) == False
assert sum28([2, 2, 2, 2]) == True
assert sum28([1, 2, 2, 2, 2, 4]) == True
assert sum28([]) == False
assert sum28([2]) == False
assert sum28([8]) == False
assert sum28([2, 2, 2]) == False
assert sum28([2, 2, 2, 2, 2]) == False
assert sum28([1, 2, 2, 1, 2, 2]) == True
assert sum28([5, 2, 2, 2, 4, 2]) == True


""" more14
    Given an array of ints, return true if the number of 1's is greater than the number of 4's
"""
def more14(nums):
    count = 0
    for i in range(len(nums)):
        if nums[i] == 1:
            count -= 1
        elif nums[i] == 4:
            count += 1
    return count < 0

assert more14([1, 4, 1]) == True
assert more14([1, 4, 1, 4]) == False
assert more14([1, 1]) == True
assert more14([1, 6, 6]) == True
assert more14([1]) == True
assert more14([1, 4]) == False
assert more14([6, 1, 1]) == True
assert more14([1, 6, 4]) == False
assert more14([1, 1, 4, 4, 1]) == True
assert more14([1, 1, 6, 4, 4, 1]) == True
assert more14([]) == False
assert more14([4, 1, 4, 6]) == False
assert more14([4, 1, 4, 6, 1]) == False
assert more14([1, 4, 1, 4, 1, 6]) == True





