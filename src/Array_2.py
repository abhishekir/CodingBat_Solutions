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


""" fizzArray
    Given a number n, create and return a new int array of length n, containing the numbers 0, 1, 2, ... n-1. The
    given n may be 0, in which case just return a length 0 array. You do not need a separate if-statement for the
    length-0 case; the for-loop should naturally execute 0 times in that case, so it just works. The syntax to make a
    new int array is: new int[desired_length]
"""
def fizzArray(n):
    res = []
    for i in range(n):
        res.append(i)
    return res

assert fizzArray(4) == [0, 1, 2, 3]
assert fizzArray(1) == [0]
assert fizzArray(10) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
assert fizzArray(0) == []
assert fizzArray(2) == [0, 1]
assert fizzArray(7) == [0, 1, 2, 3, 4, 5, 6]


""" only14
    Given an array of ints, return true if every element is a 1 or a 4.
"""
def only14(nums):
    for i in range(len(nums)):
        if not (nums[i] == 1 or nums[i] == 4):
            return False
    return True

assert only14([1, 4, 1, 4]) == True
assert only14([1, 4, 2, 4]) == False
assert only14([1, 1]) == True
assert only14([4, 1]) == True
assert only14([2]) == False
assert only14([]) == True
assert only14([1, 4, 1, 3]) == False
assert only14([3, 1, 3]) == False
assert only14([1]) == True
assert only14([4]) == True
assert only14([3, 4]) == False
assert only14([1, 3, 4]) == False
assert only14([1, 1, 1]) == True
assert only14([1, 1, 1, 5]) == False
assert only14([4, 1, 4, 1]) == True


""" fizzArray2
    Given a number n, create and return a new string array of length n, containing the strings "0", "1" "2" ..
    through n-1. N may be 0, in which case just return a length 0 array.
"""
def fizzArray2(n):
    res = []
    for i in range(n):
        res.append(str(i))
    return res

assert fizzArray2(4) == ["0", "1", "2", "3"]
assert fizzArray2(10) == ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
assert fizzArray2(2) == ["0", "1"]
assert fizzArray2(1) == ["0"]
assert fizzArray2(0) == []
assert fizzArray2(7) == ["0", "1", "2", "3", "4", "5", "6"]
assert fizzArray2(9) == ["0", "1", "2", "3", "4", "5", "6", "7", "8"]
assert fizzArray2(11) == ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]


""" no14
    Given an array of ints, return true if it contains no 1's or it contains no 4's.
"""
def no14(nums):
    seen1 = False
    seen4 = False
    for i in range(len(nums)):
        if nums[i] == 1:
            seen1 = True
        elif nums[i] == 4:
            seen4 = True
    return not (seen1 or seen4) or (seen1 ^ seen4)

assert no14([1, 2, 3]) == True
assert no14([1, 2, 3, 4]) == False
assert no14([2, 3, 4]) == True
assert no14([1, 1, 4, 4]) == False
assert no14([2, 2, 4, 4]) == True
assert no14([2, 3, 4, 1]) == False
assert no14([2, 1, 1]) == True
assert no14([1, 4]) == False
assert no14([2]) == True
assert no14([2, 1]) == True
assert no14([1]) == True
assert no14([4]) == True
assert no14([]) == True
assert no14([1, 1, 1, 1]) == True
assert no14([9, 4, 4, 1]) == False
assert no14([4, 2, 3, 1]) == False
assert no14([4, 2, 3, 5]) == True
assert no14([4, 4, 2]) == True
assert no14([1, 4, 4]) == False


""" isEverywhere
    We'll say that a value is "everywhere" in an array if for every pair of adjacent elements in the array, at least
    one of the pair is that value. Return true if the given value is everywhere in the array.
"""
def isEverywhere(nums, val):
    for i in range(len(nums)-1):
        if val not in nums[i:i+2]:
            return False
    return True

assert isEverywhere([1, 2, 1, 3], 1) == True
assert isEverywhere([1, 2, 1, 3], 2) == False
assert isEverywhere([1, 2, 1, 3, 4], 1) == False
assert isEverywhere([2, 1, 2, 1], 1) == True
assert isEverywhere([2, 1, 2, 1], 2) == True
assert isEverywhere([2, 1, 2, 3, 1], 2) == False
assert isEverywhere([3, 1], 3) == True
assert isEverywhere([3, 1], 2) == False
assert isEverywhere([3], 1) == True
assert isEverywhere([], 1) == True
assert isEverywhere([1, 2, 1, 2, 3, 2, 5], 2) == True
assert isEverywhere([1, 2, 1, 1, 1, 2], 2) == False
assert isEverywhere([2, 1, 2, 1, 1, 2], 2) == False
assert isEverywhere([2, 1, 2, 2, 2, 1, 1, 2], 2) == False
assert isEverywhere([2, 1, 2, 2, 2, 1, 2, 1], 2) == True
assert isEverywhere([2, 1, 2, 1, 2], 2) == True


""" either24
    Given an array of ints, return true if the array contains a 2 next to a 2 or a 4 next to a 4, but not both.
"""
def either24(nums):
    double2 = False
    double4 = False
    for i in range(len(nums)-1):
        if nums[i] == 2 and nums[i+1] == 2:
            double2 = True
        elif nums[i] == 4 and nums[i+1] == 4:
            double4 = True
    return double2 ^ double4

assert either24([1, 2, 2]) == True
assert either24([4, 4, 1]) == True
assert either24([4, 4, 1, 2, 2]) == False
assert either24([1, 2, 3, 4]) == False
assert either24([3, 5, 9]) == False
assert either24([1, 2, 3, 4, 4]) == True
assert either24([2, 2, 3, 4]) == True
assert either24([1, 2, 3, 2, 2, 4]) == True
assert either24([1, 2, 3, 2, 2, 4, 4]) == False
assert either24([1, 2]) == False
assert either24([2, 2]) == True
assert either24([4, 4]) == True
assert either24([2]) == False
assert either24([]) == False


""" matchUp
    Given arrays nums1 and nums2 of the same length, for every element in nums1, consider the corresponding element
    in nums2 (at the same index). Return the count of the number of times that the two elements differ by 2 or less,
    but are not equal.
"""
def matchUp(nums1, nums2):
    count = 0
    for i in range(len(nums1)):
        if 0 < abs(nums1[i] - nums2[i]) <= 2:
            count += 1
    return count

assert matchUp([1, 2, 3], [2, 3, 10]) == 2
assert matchUp([1, 2, 3], [2, 3, 5]) == 3
assert matchUp([1, 2, 3], [2, 3, 3]) == 2
assert matchUp([5, 3], [5, 5]) == 1
assert matchUp([5, 3], [4, 4]) == 2
assert matchUp([5, 3], [3, 3]) == 1
assert matchUp([5, 3], [2, 2]) == 1
assert matchUp([5, 3], [1, 1]) == 1
assert matchUp([5, 3], [0, 0]) == 0
assert matchUp([4], [4]) == 0
assert matchUp([4], [5]) == 1


""" has77
    Given an array of ints, return true if the array contains two 7's next to each other, or there are two 7's
    separated by one element, such as with {7, 1, 7}.
"""
def has77(nums):
    for i in range(len(nums)-2):
        if nums[i] == 7 and (nums[i+1] == 7 or nums[i+2] == 7):
            return True
    return nums[-2:] == [7, 7]

assert has77([1, 7, 7]) == True
assert has77([1, 7, 1, 7]) == True
assert has77([1, 7, 1, 1, 7]) == False
assert has77([7, 7, 1, 1, 7]) == True
assert has77([2, 7, 2, 2, 7, 2]) == False
assert has77([2, 7, 2, 2, 7, 7]) == True
assert has77([7, 2, 7, 2, 2, 7]) == True
assert has77([7, 2, 6, 2, 2, 7]) == False
assert has77([7, 7, 7]) == True
assert has77([7, 1, 7]) == True
assert has77([7, 1, 1]) == False
assert has77([1, 2]) == False
assert has77([1, 7]) == False
assert has77([7]) == False


""" has12
    Given an array of ints, return true if there is a 1 in the array with a 2 somewhere later in the array.
"""
def has12(nums):
    seen1 = False
    for i in range(len(nums)):
        if nums[i] == 1:
            seen1 = True
        elif nums[i] == 2 and seen1:
            return True
    return False

assert has12([1, 3, 2]) == True
assert has12([3, 1, 2]) == True
assert has12([3, 1, 4, 5, 2]) == True
assert has12([3, 1, 4, 5, 6]) == False
assert has12([3, 1, 4, 1, 6, 2]) == True
assert has12([2, 1, 4, 1, 6, 2]) == True
assert has12([2, 1, 4, 1, 6]) == False
assert has12([1]) == False
assert has12([2, 1, 3]) == False
assert has12([2, 1, 3, 2]) == True
assert has12([2]) == False
assert has12([3, 2]) == False
assert has12([3, 1, 3, 2]) == True
assert has12([3, 5, 9]) == False
assert has12([3, 5, 1]) == False
assert has12([3, 2, 1]) == False
assert has12([1, 2]) == True


""" modThree
    Given an array of ints, return true if the array contains either 3 even or 3 odd values all next to each other.
"""
def modThree(nums):
    if len(nums) < 3:
        return False
    else:
        for i in range(len(nums)-2):
            if nums[i] % 2 == nums[i+1] % 2 == nums[i+2] % 2:
                return True
        return False

assert modThree([2, 1, 3, 5]) == True
assert modThree([2, 1, 2, 5]) == False
assert modThree([2, 4, 2, 5]) == True
assert modThree([1, 2, 1, 2, 1]) == False
assert modThree([9, 9, 9]) == True
assert modThree([1, 2, 1]) == False
assert modThree([1, 2]) == False
assert modThree([1]) == False
assert modThree([]) == False
assert modThree([9, 7, 2, 9]) == False
assert modThree([9, 7, 2, 9, 2, 2]) == False
assert modThree([9, 7, 2, 9, 2, 2, 6]) == True


""" haveThree
    Given an array of ints, return true if the value 3 appears in the array exactly 3 times, and no 3's are next to
    each other.
"""
def haveThree(nums):
    if len(nums) < 3:
        return False
    else:
        count3 = 0
        for i in range(len(nums)):
            if nums[i] == 3 and i+1 < len(nums) and nums[i+1] == 3:
                return False
            elif nums[i] == 3:
                count3 += 1
        return count3 == 3

assert haveThree([3, 1, 3, 1, 3]) == True
assert haveThree([3, 1, 3, 3]) == False
assert haveThree([3, 4, 3, 3, 4]) == False
assert haveThree([1, 3, 1, 3, 1, 2]) == False
assert haveThree([1, 3, 1, 3, 1, 3]) == True
assert haveThree([1, 3, 3, 1, 3]) == False
assert haveThree([1, 3, 1, 3, 1, 3, 4, 3]) == False
assert haveThree([3, 4, 3, 4, 3, 4, 4]) == True
assert haveThree([3, 3, 3]) == False
assert haveThree([1, 3]) == False
assert haveThree([3]) == False
assert haveThree([1]) == False


""" twoTwo
    Given an array of ints, return true if every 2 that appears in the array is next to another 2.
"""
def twoTwo(nums):
    for i in range(len(nums)):
        if nums[i] == 2:
            if i-1 >= 0 and nums[i-1] == 2 or i+1 < len(nums) and nums[i+1] == 2:
                continue
            else:
                return False
    return True

assert twoTwo([4, 2, 2, 3]) == True
assert twoTwo([2, 2, 4]) == True
assert twoTwo([2, 2, 4, 2]) == False
assert twoTwo([1, 3, 4]) == True
assert twoTwo([1, 2, 2, 3, 4]) == True
assert twoTwo([1, 2, 3, 4]) == False
assert twoTwo([2, 2]) == True
assert twoTwo([2, 2, 7]) == True
assert twoTwo([2, 2, 7, 2, 1]) == False
assert twoTwo([4, 2, 2, 2]) == True
assert twoTwo([2, 2, 2]) == True
assert twoTwo([1, 2]) == False
assert twoTwo([2]) == False
assert twoTwo([1]) == True
assert twoTwo([]) == True
assert twoTwo([5, 2, 2, 3]) == True
assert twoTwo([2, 2, 5, 2]) == False


""" sameEnds
    Return true if the group of N numbers at the start and end of the array are the same. For example, with {5, 6,
    45, 99, 13, 5, 6}, the ends are the same for n=0 and n=2, and false for n=1 and n=3. You may assume that n is in
    the range 0..nums.length inclusive.
"""
def sameEnds(nums, len):
    return len == 0 or nums[:len] == nums[-len:]

assert sameEnds([5, 6, 45, 99, 13, 5, 6], 1) == False
assert sameEnds([5, 6, 45, 99, 13, 5, 6], 2) == True
assert sameEnds([5, 6, 45, 99, 13, 5, 6], 3) == False
assert sameEnds([1, 2, 5, 2, 1], 1) == True
assert sameEnds([1, 2, 5, 2, 1], 2) == False
assert sameEnds([1, 2, 5, 2, 1], 0) == True
assert sameEnds([1, 2, 5, 2, 1], 5) == True
assert sameEnds([1, 1, 1], 0) == True
assert sameEnds([1, 1, 1], 1) == True
assert sameEnds([1, 1, 1], 2) == True
assert sameEnds([1, 1, 1], 3) == True
assert sameEnds([1], 1) == True
assert sameEnds([], 0) == True
assert sameEnds([4, 2, 4, 5], 1) == False


""" tripleUp
    Return true if the array contains, somewhere, three increasing adjacent numbers like .... 4, 5, 6, ... or 23, 24,
    25.
"""
def tripleUp(nums):
    for i in range(len(nums)-2):
        if nums[i+2] - nums[i+1] == 1 and nums[i+1] - nums[i] == 1:
            return True
    return False

assert tripleUp([1, 4, 5, 6, 2]) == True
assert tripleUp([1, 2, 3]) == True
assert tripleUp([1, 2, 4]) == False
assert tripleUp([1, 2, 4, 5, 7, 6, 5, 6, 7, 6]) == True
assert tripleUp([1, 2, 4, 5, 7, 6, 5, 7, 7, 6]) == False
assert tripleUp([1, 2]) == False
assert tripleUp([1]) == False
assert tripleUp([]) == False
assert tripleUp([10, 9, 8, -100, -99, -98, 100]) == True
assert tripleUp([10, 9, 8, -100, -99, 99, 100]) == False
assert tripleUp([-100, -99, -99, 100, 101, 102]) == True
assert tripleUp([2, 3, 5, 6, 8, 9, 2, 3]) == False


""" fizzArray3
    Given start and end numbers, return a new array containing the sequence of integers from start up to but not
    including end, so start=5 and end=10 yields {5, 6, 7, 8, 9}. The end number will be greater or equal to the start
    number.
"""
def fizzArray3(start, end):
    res = []
    for i in range(start, end):
        res.append(i)
    return res

assert fizzArray3(5, 10) == [5, 6, 7, 8, 9]
assert fizzArray3(11, 18) == [11, 12, 13, 14, 15, 16, 17]
assert fizzArray3(1, 3) == [1, 2]
assert fizzArray3(1, 2) == [1]
assert fizzArray3(1, 1) == []
assert fizzArray3(1000, 1005) == [1000, 1001, 1002, 1003, 1004]


""" shiftLeft
    Return an array that is "left shifted" by one -- so {6, 2, 5, 3} returns {2, 5, 3, 6}. You may modify and return
    the given array, or return a new array.
"""
def shiftLeft(nums):
    if len(nums) < 2:
        return nums
    else:
        temp = nums[0]
        for i in range(len(nums)-1):
            nums[i] = nums[i+1]
        nums[-1] = temp
        return nums


assert shiftLeft([6, 2, 5, 3]) == [2, 5, 3, 6]
assert shiftLeft([1, 2]) == [2, 1]
assert shiftLeft([1]) == [1]
assert shiftLeft([]) == []
assert shiftLeft([1, 1, 2, 2, 4]) == [1, 2, 2, 4, 1]
assert shiftLeft([1, 1, 1]) == [1, 1, 1]
assert shiftLeft([1, 2, 3]) == [2, 3, 1]


""" tenRun
    For each multiple of 10 in the given array, change all the values following it to be that multiple of 10, until
    encountering another multiple of 10. So {2, 10, 3, 4, 20, 5} yields {2, 10, 10, 10, 20, 20}.
"""
def tenRun(nums):
    tenMult = -1
    for i in range(len(nums)):
        if nums[i] % 10 == 0:
            tenMult = nums[i]
        elif tenMult != -1:
            nums[i] = tenMult
        else:
            continue
    return nums

assert tenRun([2, 10, 3, 4, 20, 5]) == [2, 10, 10, 10, 20, 20]
assert tenRun([10, 1, 20, 2]) == [10, 10, 20, 20]
assert tenRun([10, 1, 9, 20]) == [10, 10, 10, 20]
assert tenRun([1, 2, 50, 1]) == [1, 2, 50, 50]
assert tenRun([1, 20, 50, 1]) == [1, 20, 50, 50]
assert tenRun([10, 10]) == [10, 10]
assert tenRun([10, 2]) == [10, 10]
assert tenRun([0, 2]) == [0, 0]
assert tenRun([1, 2]) == [1, 2]
assert tenRun([1]) == [1]
assert tenRun([]) == []


""" pre4
    Given a non-empty array of ints, return a new array containing the elements from the original array that come
    before the first 4 in the original array. The original array will contain at least one 4.
"""
def pre4(nums):
    res = []
    for i in range(len(nums)):
        if nums[i] == 4:
            return res
        else:
            res.append(nums[i])
    return res

assert pre4([1, 2, 4, 1]) == [1, 2]
assert pre4([3, 1, 4]) == [3, 1]
assert pre4([1, 4, 4]) == [1]
assert pre4([1, 4, 4, 2]) == [1]
assert pre4([1, 3, 4, 2, 4]) == [1, 3]
assert pre4([4, 4]) == []
assert pre4([3, 3, 4]) == [3, 3]
assert pre4([1, 2, 1, 4]) == [1, 2, 1]
assert pre4([2, 1, 4, 2]) == [2, 1]
assert pre4([2, 1, 2, 1, 4, 2]) == [2, 1, 2, 1]


""" post4
    Given a non-empty array of ints, return a new array containing the elements from the original array that come
    after the last 4 in the original array. The original array will contain at least one 4.
"""
def post4(nums):
    i = len(nums)-1
    while i >= 0:
        if nums[i] == 4:
            return nums[i+1:]
        i -= 1
    return

assert post4([2, 4, 1, 2]) == [1, 2]
assert post4([4, 1, 4, 2]) == [2]
assert post4([4, 4, 1, 2, 3]) == [1, 2, 3]
assert post4([4, 2]) == [2]
assert post4([4, 4, 3]) == [3]
assert post4([4, 4]) == []
assert post4([4]) == []
assert post4([2, 4, 1, 4, 3, 2]) == [3, 2]
assert post4([4, 1, 4, 2, 2, 2]) == [2, 2, 2]
assert post4([3, 4, 3, 2]) == [3, 2]


""" notAlone
    We'll say that an element in an array is "alone" if there are values before and after it, and those values are
    different from it. Return a version of the given array where every instance of the given value which is alone is
    replaced by whichever value to its left or right is larger.
"""
def notAlone(nums, val):
    if not nums:
        return nums
    else:
        for i in range(1, len(nums)-1):
            if nums[i] == val and nums[i-1] != val and nums[i+1] != val:
                nums[i] = max(nums[i-1], nums[i+1])
        return nums

assert notAlone([1, 2, 3], 2) == [1, 3, 3]
assert notAlone([1, 2, 3, 2, 5, 2], 2) == [1, 3, 3, 5, 5, 2]
assert notAlone([3, 4], 3) == [3, 4]
assert notAlone([3, 3], 3) == [3, 3]
assert notAlone([1, 3, 1, 2], 1) == [1, 3, 3, 2]
assert notAlone([3], 3) == [3]
assert notAlone([], 3) == []
assert notAlone([7, 1, 6], 1) == [7, 7, 6]
assert notAlone([1, 1, 1], 1) == [1, 1, 1]
assert notAlone([1, 1, 1, 2], 1) == [1, 1, 1, 2]


""" zeroFront
    Return an array that contains the exact same numbers as the given array, but rearranged so that all the zeros are
    grouped at the start of the array. The order of the non-zero numbers does not matter. So {1, 0, 0, 1} becomes {0,
    0, 1, 1}. You may modify and return the given array or make a new array.
"""
def zeroFront(nums):
    i = len(nums) - 1
    rightZero = i
    while i >= 0:
        while nums[rightZero] != 0:
            if rightZero == 0:
                break
            else:
                rightZero -= 1
        if nums[i] != 0 and i < rightZero:
            nums[rightZero] = nums[i]
            nums[i] = 0
        i -= 1
    return nums

assert zeroFront([1, 0, 0, 1]) == [0, 0, 1, 1]
assert zeroFront([0, 1, 1, 0, 1]) == [0, 0, 1, 1, 1]
assert zeroFront([1, 0]) == [0, 1]
assert zeroFront([0, 1]) == [0, 1]
assert zeroFront([1, 1, 1, 0]) == [0, 1, 1, 1]
assert zeroFront([2, 2, 2, 2]) == [2, 2, 2, 2]
assert zeroFront([0, 0, 1, 0]) == [0, 0, 0, 1]
assert zeroFront([-1, 0, 0, -1, 0]) == [0, 0, 0, -1, -1]
assert zeroFront([0, -3, 0, -3]) == [0, 0, -3, -3]
assert zeroFront([]) == []
assert zeroFront([9, 9, 0, 9, 0, 9]) == [0, 0, 9, 9, 9, 9]



















