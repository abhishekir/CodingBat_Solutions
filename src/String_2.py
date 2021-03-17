"""
    https://codingbat.com/python/String-2
    Medium python string problems -- 1 loop.. Use + to combine strings, len(str) is the number of chars in a String,
    str[i:j] extracts the substring starting at index i and running up to but not including index j.
"""
class String_2:
    """ double_char
        Given a string, return a string where for every char in the original, there are two chars.
    """
    def double_char(str):
        result = ""
        for i in range(len(str)):
            result += str[i] + str[i]
        return result

    """ count_hi
        Return the number of times that the string "hi" appears anywhere in the given string.
    """
    def count_hi(str):
        count = 0
        for i in range(len(str)-1):
            if (str[i:i+2] == "hi"): count += 1
        return count

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

    """ end_other
        Given two strings, return True if either of the strings appears at the very end of the other string, ignoring 
        upper/lower case differences (in other words, the computation should not be "case sensitive").
    """
    def end_other(a, b):
        a = a.lower()
        b = b.lower()
        return b == a[-len(b):] if len(a) > len(b) else a == b[-len(a):]

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