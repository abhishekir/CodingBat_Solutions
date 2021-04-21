"""
    https://codingbat.com/python/List-2
    Medium python list problems -- 1 loop.. Use a[0], a[1], ... to access elements in a list, len(a) is the length.
"""
class List_2:
    """ count_evens
        Return the number of even ints in the given array. Note: the % "mod" operator computes the remainder, e.g. 5 % 2
        is 1.
    """
    def count_evens(nums):
        count = 0;
        for i in range(len(nums)):
            if nums[i] % 2 == 0: count += 1
        return count

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

    """ centered_average
        Return the "centered" average of an array of ints, which we'll say is the mean average of the values, except 
        ignoring the largest and smallest values in the array. If there are multiple copies of the smallest value, 
        ignore just one copy, and likewise for the largest value. Use int division to produce the final average. You may 
        assume that the array is length 3 or more.
    """
    def centered_average(nums):
        big = nums[0]
        small = nums[0]
        sum = 0;

        for i in range(len(nums)):
            big = max(big, nums[i])
            small = min(small, nums[i])
            sum += nums[i]

        return (sum - big - small) / (len(nums)-2)

    """ sum13
        Return the sum of the numbers in the array, returning 0 for an empty array. Except the number 13 is very 
        unlucky, so it does not count and numbers that come immediately after a 13 also do not count.
    """
    def sum13(nums):
        seen13 = False;
        sum = 0;

        for i in range(len(nums)):
            if seen13: seen13 = False
            elif nums[i] == 13: seen13 = True
            else: sum += nums[i]

        return sum

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