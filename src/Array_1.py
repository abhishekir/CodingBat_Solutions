"""
    https://codingbat.com/python/List-1
    Basic python list problems -- no loops.. Use a[0], a[1], ... to access elements in a list, len(a) is the length.
"""


""" first_last6
    Given an array of ints, return True if 6 appears as either the first or last element in the array. The array
    will be length 1 or more.
"""
def first_last6(nums):
    return nums[0] == 6 or nums[len(nums)-1] == 6

assert first_last6([1, 2, 6]) == True
assert first_last6([6, 1, 2, 3]) == True
assert first_last6([13, 6, 1, 2, 3]) == False
assert first_last6([13, 6, 1, 2, 6]) == True
assert first_last6([3, 2, 1]) == False
assert first_last6([3, 6, 1]) == False
assert first_last6([3, 6]) == True
assert first_last6([6]) == True
assert first_last6([3]) == False
assert first_last6([5, 6]) == True
assert first_last6([5, 5]) == False
assert first_last6([1, 2, 3, 4, 6]) == True
assert first_last6([1, 2, 3, 4]) == False


""" same_first_last
    Given an array of ints, return True if the array is length 1 or more, and the first element and the last element 
    are equal.
"""
def same_first_last(nums):
    if len(nums) < 1:
        return False
    return nums[0] == nums[len(nums)-1]

assert same_first_last([1, 2, 3]) == False
assert same_first_last([1, 2, 3, 1]) == True
assert same_first_last([1, 2, 1]) == True
assert same_first_last([7]) == True
assert same_first_last([]) == False
assert same_first_last([1, 2, 3, 4, 5, 1]) == True
assert same_first_last([1, 2, 3, 4, 5, 13]) == False
assert same_first_last([13, 2, 3, 4, 5, 13]) == True
assert same_first_last([7, 7]) == True


""" make_pi
    Return an int array length 3 containing the first 3 digits of pi, {3, 1, 4}.
"""
def make_pi():
    return [3, 1, 4]

assert make_pi() == [3, 1, 4]


""" common_end
    Given 2 arrays of ints, a and b, return True if they have the same first element or they have the same last 
    element. Both arrays will be length 1 or more.
"""
def common_end(a, b):
    return a[0] == b[0] or a[len(a)-1] == b[len(b)-1]

assert common_end([1, 2, 3], [7, 3]) == True
assert common_end([1, 2, 3], [7, 3, 2]) == False
assert common_end([1, 2, 3], [1, 3]) == True
assert common_end([1, 2, 3], [1]) == True
assert common_end([1, 2, 3], [2]) == False


""" sum3
    Given an array of ints length 3, return the sum of all the elements.
"""
def sum3(nums):
    return nums[0] + nums[1] + nums[2]

assert sum3([1, 2, 3]) == 6
assert sum3([5, 11, 2]) == 18
assert sum3([7, 0, 0]) == 7
assert sum3([1, 2, 1]) == 4
assert sum3([1, 1, 1]) == 3
assert sum3([2, 7, 2]) == 11


""" rotate_left3
    Given an array of ints length 3, return an array with the elements "rotated left" so {1, 2, 3} yields {2, 3, 1}.
"""
def rotate_left3(nums):
    return [nums[1], nums[2], nums[0]]

assert rotate_left3([1, 2, 3]) == [2, 3, 1]
assert rotate_left3([5, 11, 9]) == [11, 9, 5]
assert rotate_left3([7, 0, 0]) == [0, 0, 7]
assert rotate_left3([1, 2, 1]) == [2, 1, 1]
assert rotate_left3([0, 0, 1]) == [0, 1, 0]


""" reverse3
    Given an array of ints length 3, return a new array with the elements in reverse order, so {1, 2, 3} becomes 
    {3, 2, 1}.
"""
def reverse3(nums):
    return [nums[2], nums[1], nums[0]]

assert reverse3([1, 2, 3]) == [3, 2, 1]
assert reverse3([5, 11, 9]) == [9, 11, 5]
assert reverse3([7, 0, 0]) == [0, 0, 7]
assert reverse3([2, 1, 2]) == [2, 1, 2]
assert reverse3([1, 2, 1]) == [1, 2, 1]
assert reverse3([2, 11, 3]) == [3, 11, 2]
assert reverse3([0, 6, 5]) == [5, 6, 0]
assert reverse3([7, 2, 3]) == [3, 2, 7]


""" max_end3
    Given an array of ints length 3, figure out which is larger, the first or last element in the array, and set all 
    the other elements to be that value. Return the changed array.
"""
def max_end3(nums):
    larger = nums[0] if nums[0] >= nums[len(nums)-1] else nums[len(nums)-1]
    return [larger, larger, larger]

assert max_end3([1, 2, 3]) == [3, 3, 3]
assert max_end3([11, 5, 9]) == [11, 11, 11]
assert max_end3([2, 11, 3]) == [3, 3, 3]
assert max_end3([11, 3, 3]) == [11, 11, 11]
assert max_end3([3, 11, 11]) == [11, 11, 11]
assert max_end3([2, 2, 2]) == [2, 2, 2]
assert max_end3([2, 11, 2]) == [2, 2, 2]
assert max_end3([0, 0, 1]) == [1, 1, 1]


""" sum2
    Given an array of ints, return the sum of the first 2 elements in the array. If the array length is less than 2, 
    just sum up the elements that exist, returning 0 if the array is length 0.
"""
def sum2(nums):
    if len(nums) == 0:
        return 0
    elif len(nums) < 2:
        return nums[0]
    else:
        return nums[0] + nums[1]

assert sum2([1, 2, 3]) == 3
assert sum2([1, 1]) == 2
assert sum2([1, 1, 1, 1]) == 2
assert sum2([1, 2]) == 3
assert sum2([1]) == 1
assert sum2([]) == 0
assert sum2([4, 5, 6]) == 9
assert sum2([4]) == 4


""" middle_way
    Given 2 int arrays, a and b, each length 3, return a new array length 2 containing their middle elements.
"""
def middle_way(a, b):
    return [a[1], b[1]]

assert middle_way([1, 2, 3], [4, 5, 6]) == [2, 5]
assert middle_way([7, 7, 7], [3, 8, 0]) == [7, 8]
assert middle_way([5, 2, 9], [1, 4, 5]) == [2, 4]
assert middle_way([1, 9, 7], [4, 8, 8]) == [9, 8]
assert middle_way([1, 2, 3], [3, 1, 4]) == [2, 1]
assert middle_way([1, 2, 3], [4, 1, 1]) == [2, 1]


""" make_ends
    Given an array of ints, return a new array length 2 containing the first and last elements from the original 
    array. The original array will be length 1 or more.
"""
def make_ends(nums):
    return [nums[0], nums[len(nums)-1]]

assert make_ends([1, 2, 3]) == [1, 3]
assert make_ends([1, 2, 3, 4]) == [1, 4]
assert make_ends([7, 4, 6, 2]) == [7, 2]
assert make_ends([1, 2, 2, 2, 2, 2, 2, 3]) == [1, 3]
assert make_ends([7, 4]) == [7, 4]
assert make_ends([7]) == [7, 7]
assert make_ends([5, 2, 9]) == [5, 9]
assert make_ends([2, 3, 4, 1]) == [2, 1]


""" has23
    Given an int array length 2, return True if it contains a 2 or a 3.
"""
def has23(nums):
    return nums[0] == 2 or nums[0] == 3 or nums[1] == 2 or nums[1] == 3

assert has23([2, 5]) == True
assert has23([4, 3]) == True
assert has23([4, 5]) == False
assert has23([2, 2]) == True
assert has23([3, 2]) == True
assert has23([3, 3]) == True
assert has23([7, 7]) == False
assert has23([3, 9]) == True
assert has23([9, 5]) == False


""" no23
    Given an int array length 2, return true if it does not contain a 2 or 3.
"""
def no23(nums):
    return not (2 in nums or 3 in nums)

assert no23([4, 5]) == True
assert no23([4, 2]) == False
assert no23([3, 5]) == False
assert no23([1, 9]) == True
assert no23([2, 9]) == False
assert no23([1, 3]) == False
assert no23([1, 1]) == True
assert no23([2, 2]) == False
assert no23([3, 3]) == False
assert no23([7, 8]) == True
assert no23([8, 7]) == True


""" makeLast
    Given an int array, return a new array with double the length where its last element is the same as the original
    array, and all the other elements are 0. The original array will be length 1 or more.
"""
def makeLast(nums):
    l = len(nums) * 2
    lst = [0] * l
    lst[l-1] = nums[-1:][0]
    return lst

assert makeLast([4, 5, 6]) == [0, 0, 0, 0, 0, 6]
assert makeLast([1, 2]) == [0, 0, 0, 2]
assert makeLast([3]) == [0, 3]
assert makeLast([0]) == [0, 0]
assert makeLast([7, 7, 7]) == [0, 0, 0, 0, 0, 7]
assert makeLast([3, 1, 4]) == [0, 0, 0, 0, 0, 4]
assert makeLast([1, 2, 3, 4]) == [0, 0, 0, 0, 0, 0, 0, 4]
assert makeLast([1, 2, 3, 0]) == [0, 0, 0, 0, 0, 0, 0, 0]
assert makeLast([2, 4]) == [0, 0, 0, 4]


""" double23
    Given an int array, return true if the array contains 2 twice, or 3 twice. The array will be length 0, 1, or 2.
"""
def double23(nums):
    return nums == [2, 2] or nums == [3, 3]

assert double23([2, 2]) == True
assert double23([3, 3]) == True
assert double23([2, 3]) == False
assert double23([3, 2]) == False
assert double23([4, 5]) == False
assert double23([2]) == False
assert double23([3]) == False
assert double23([]) == False
assert double23([3, 4]) == False


""" fix23
    Given an int array length 3, if there is a 2 in the array immediately followed by a 3, set the 3 element to 0.
    Return the changed array.
"""
def fix23(nums):
    if nums[0] == 2 and nums[1] == 3:
        nums[1] = 0
    elif nums[1] == 2 and nums[2] == 3:
        nums[2] = 0
    return nums

assert fix23([1, 2, 3]) == [1, 2, 0]
assert fix23([2, 3, 5]) == [2, 0, 5]
assert fix23([1, 2, 1]) == [1, 2, 1]
assert fix23([3, 2, 1]) == [3, 2, 1]
assert fix23([3, 2, 3]) == [3, 2, 0]
assert fix23([3, 2, 2]) == [3, 2, 2]
assert fix23([2, 2, 3]) == [2, 2, 0]
assert fix23([2, 3, 3]) == [2, 0, 3]


""" start1
    Start with 2 int arrays, a and b, of any length. Return how many of the arrays have 1 as their first element.
"""
def start1(a, b):
    return (1 if a and a[0] == 1 else 0) + (1 if b and b[0] == 1 else 0)

assert start1([1, 2, 3], [1, 3]) == 2
assert start1([7, 2, 3], [1]) == 1
assert start1([1, 2], []) == 1
assert start1([], [1, 2]) == 1
assert start1([7], []) == 0
assert start1([7], [1]) == 1
assert start1([1], [1]) == 2
assert start1([7], [8]) == 0
assert start1([], []) == 0
assert start1([1, 3], [1]) == 2


""" biggerTwo
    Start with 2 int arrays, a and b, each length 2. Consider the sum of the values in each array. Return the array
    which has the largest sum. In event of a tie, return a.
"""
def biggerTwo(a, b):
    return a if sum(a) >= sum(b) else b

assert biggerTwo([1, 2], [3, 4]) == [3, 4]
assert biggerTwo([3, 4], [1, 2]) == [3, 4]
assert biggerTwo([1, 1], [1, 2]) == [1, 2]
assert biggerTwo([2, 1], [1, 1]) == [2, 1]
assert biggerTwo([2, 2], [1, 3]) == [2, 2]
assert biggerTwo([1, 3], [2, 2]) == [1, 3]
assert biggerTwo([6, 7], [3, 1]) == [6, 7]


""" makeMiddle
    Given an array of ints of even length, return a new array length 2 containing the middle two elements from the
    original array. The original array will be length 2 or more.
"""
def makeMiddle(nums):
    mid = int((len(nums) / 2)) - 1
    return nums[mid:mid+2]

assert makeMiddle([1, 2, 3, 4]) == [2, 3]
assert makeMiddle([7, 1, 2, 3, 4, 9]) == [2, 3]
assert makeMiddle([1, 2]) == [1, 2]
assert makeMiddle([5, 2, 4, 7]) == [2, 4]
assert makeMiddle([9, 0, 4, 3, 9, 1]) == [4, 3]


""" plusTwo
    Given 2 int arrays, each length 2, return a new array length 4 containing all their elements.
"""
def plusTwo(a, b):
    return a + b

assert plusTwo([1, 2], [3, 4]) == [1, 2, 3, 4]
assert plusTwo([4, 4], [2, 2]) == [4, 4, 2, 2]
assert plusTwo([9, 2], [3, 4]) == [9, 2, 3, 4]


""" swapEnds
    Given an array of ints, swap the first and last elements in the array. Return the modified array. The array
    length will be at least 1.
"""
def swapEnds(nums):
    return nums[-1:] + nums[1:-1] + nums[:1] if len(nums) > 1 else nums

assert swapEnds([1, 2, 3, 4]) == [4, 2, 3, 1]
assert swapEnds([1, 2, 3]) == [3, 2, 1]
assert swapEnds([8, 6, 7, 9, 5]) == [5, 6, 7, 9, 8]
assert swapEnds([3, 1, 4, 1, 5, 9]) == [9, 1, 4, 1, 5, 3]
assert swapEnds([1, 2]) == [2, 1]
assert swapEnds([1]) == [1]


""" midThree
    Given an array of ints of odd length, return a new array length 3 containing the elements from the middle of the
    array. The array length will be at least 3.
"""
def midThree(nums):
    mid = int(len(nums) / 2)
    return nums[mid-1:mid+2]

assert midThree([1, 2, 3, 4, 5]) == [2, 3, 4]
assert midThree([8, 6, 7, 5, 3, 0, 9]) == [7, 5, 3]
assert midThree([1, 2, 3]) == [1, 2, 3]


""" maxTriple
    Given an array of ints of odd length, look at the first, last, and middle values in the array and return the
    largest. The array length will be a least 1.
"""
def maxTriple(nums):
    mid = int(len(nums) / 2)
    return max(nums[0], nums[mid], nums[-1])

assert maxTriple([1, 2, 3]) == 3
assert maxTriple([1, 5, 3]) == 5
assert maxTriple([5, 2, 3]) == 5
assert maxTriple([1, 2, 3, 1, 1]) == 3
assert maxTriple([1, 7, 3, 1, 5]) == 5
assert maxTriple([5, 1, 3, 7, 1]) == 5
assert maxTriple([5, 1, 7, 3, 7, 8, 1]) == 5
assert maxTriple([5, 1, 7, 9, 7, 8, 1]) == 9
assert maxTriple([5, 1, 7, 3, 7, 8, 9]) == 9
assert maxTriple([2, 2, 5, 1, 1]) == 5


""" frontPiece
    Given an int array of any length, return a new array of its first 2 elements. If the array is smaller than length
    2, use whatever elements are present.
"""
def frontPiece(nums):
    return nums[:2]

assert frontPiece([1, 2, 3]) == [1, 2]
assert frontPiece([1, 2]) == [1, 2]
assert frontPiece([1]) == [1]
assert frontPiece([]) == []
assert frontPiece([6, 5, 0]) == [6, 5]
assert frontPiece([6, 5]) == [6, 5]
assert frontPiece([3, 1, 4, 1, 5]) == [3, 1]
assert frontPiece([6]) == [6]


""" unlucky1
    We'll say that a 1 immediately followed by a 3 in an array is an "unlucky" 1. Return true if the given array
    contains an unlucky 1 in the first 2 or last 2 positions in the array.
"""
def unlucky1(nums):
    return nums[:2] == [1, 3] or nums[1:3] == [1, 3] or nums[-2:] == [1, 3]

assert unlucky1([1, 3, 4, 5]) == True
assert unlucky1([2, 1, 3, 4, 5]) == True
assert unlucky1([1, 1, 1]) == False
assert unlucky1([1, 3, 1]) == True
assert unlucky1([1, 1, 3]) == True
assert unlucky1([1, 2, 3]) == False
assert unlucky1([3, 3, 3]) == False
assert unlucky1([1, 3]) == True
assert unlucky1([1, 4]) == False
assert unlucky1([1]) == False
assert unlucky1([]) == False
assert unlucky1([1, 1, 1, 3, 1]) == False
assert unlucky1([1, 1, 3, 1, 1]) == True
assert unlucky1([1, 1, 1, 1, 3]) == True
assert unlucky1([1, 4, 1, 5]) == False
assert unlucky1([1, 1, 2, 3]) == False
assert unlucky1([2, 3, 2, 1]) == False
assert unlucky1([2, 3, 1, 3]) == True
assert unlucky1([1, 2, 3, 4, 1, 3]) == True


""" make2
    Given 2 int arrays, a and b, return a new array length 2 containing, as much as will fit, the elements from a
    followed by the elements from b. The arrays may be any length, including 0, but there will be 2 or more elements
    available between the 2 arrays.
"""
def make2(a, b):
    return (a + b)[:2]

assert make2([4, 5], [1, 2, 3]) == [4, 5]
assert make2([4], [1, 2, 3]) == [4, 1]
assert make2([], [1, 2]) == [1, 2]
assert make2([1, 2], []) == [1, 2]
assert make2([3], [1, 2, 3]) == [3, 1]
assert make2([3], [1]) == [3, 1]
assert make2([3, 1, 4], []) == [3, 1]
assert make2([1], [1]) == [1, 1]
assert make2([1, 2, 3], [7, 8]) == [1, 2]
assert make2([7, 8], [1, 2, 3]) == [7, 8]
assert make2([7], [1, 2, 3]) == [7, 1]
assert make2([5, 4], [2, 3, 7]) == [5, 4]


""" front11
    Given 2 int arrays, a and b, of any length, return a new array with the first element of each array. If either
    array is length 0, ignore that array.
"""
def front11(a, b):
    return a[:1] + b[:1]

assert front11([1, 2, 3], [7, 9, 8]) == [1, 7]
assert front11([1], [2]) == [1, 2]
assert front11([1, 7], []) == [1]
assert front11([], [2, 8]) == [2]
assert front11([], []) == []
assert front11([3], [1, 4, 1, 9]) == [3, 1]
assert front11([1, 4, 1, 9], []) == [1]
