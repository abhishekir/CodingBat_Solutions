/**
 * https://codingbat.com/java/Recursion-1
 * Basic recursion problems.
 */
public class Recursion_1 {
    /** factorial
     * Given n of 1 or more, return the factorial of n, which is n * (n-1) * (n-2) ... 1. Compute the result recursively
     * (without loops).
     */
    public int factorial(int n) {
        if (n == 1) return 1;
        else return n * factorial(n-1);
    }

    /** bunnyEars
     * We have a number of bunnies and each bunny has two big floppy ears. We want to compute the total number of ears
     * across all the bunnies recursively (without loops or multiplication).
     */
    public int bunnyEars(int bunnies) {
        if (bunnies == 0) return 0;
        else return 2 + bunnyEars(bunnies-1);
    }

    /** fibonacci
     * The fibonacci sequence is a famous bit of mathematics, and it happens to have a recursive definition. The first
     * two values in the sequence are 0 and 1 (essentially 2 base cases). Each subsequent value is the sum of the
     * previous two values, so the whole sequence is: 0, 1, 1, 2, 3, 5, 8, 13, 21 and so on. Define a recursive
     * fibonacci(n) method that returns the nth fibonacci number, with n=0 representing the start of the sequence.
     */
    public int fibonacci(int n) {
        if (n == 0 || n == 1) return n;
        else return fibonacci(n-1) + fibonacci(n-2);
    }

    /** bunnyEars2
     * We have bunnies standing in a line, numbered 1, 2, ... The odd bunnies (1, 3, ..) have the normal 2 ears. The
     * even bunnies (2, 4, ..) we'll say have 3 ears, because they each have a raised foot. Recursively return the
     * number of "ears" in the bunny line 1, 2, ... n (without loops or multiplication).
     */
    public int bunnyEars2(int bunnies) {
        if (bunnies == 0) return 0;
        else if (bunnies % 2 == 0) return 3 + bunnyEars2(bunnies-1);
        else return 2 + bunnyEars2(bunnies-1);
    }

    /** triangle
     * We have triangle made of blocks. The topmost row has 1 block, the next row down has 2 blocks, the next row has 3
     * blocks, and so on. Compute recursively (no loops or multiplication) the total number of blocks in such a triangle
     * with the given number of rows.
     */
    public int triangle(int rows) {
        if (rows == 0) return 0;
        else return rows + triangle(rows-1);
    }

    /** sumDigits
     * Given a non-negative int n, return the sum of its digits recursively (no loops).
     */
    public int sumDigits(int n) {
        if (n / 10 == 0) return n;
        else return n % 10 + sumDigits(n / 10);
    }

    /** count7
     * Given a non-negative int n, return the count of the occurrences of 7 as a digit, so for example 717 yields 2.
     * (no loops).
     */
    public int count7(int n) {
        if (n / 10 == 0) return n == 7 ? 1 : 0;
        else return n % 10 == 7 ? 1 + count7(n / 10) : count7(n / 10);
    }

    /** count8
     * Given a non-negative int n, compute recursively (no loops) the count of the occurrences of 8 as a digit, except
     * that an 8 with another 8 immediately to its left counts double, so 8818 yields 4.
     */
    public int count8(int n) {
        if (n == 0) return 0;
        else if (n % 10 == 8) {
            if (n % 100 == 88) return 2 + count8(n / 10);
            else return 1 + count8(n / 10);
        }
        else return count8(n / 10);
    }

    /** powerN
     * Given base and n that are both 1 or more, compute recursively (no loops) the value of base to the n power, so
     * powerN(3, 2) is 9 (3 squared).
     */
    public int powerN(int base, int n) {
        if (n == 1) return base;
        else return base * powerN(base, n-1);
    }

    /** countX
     * Given a string, compute recursively (no loops) the number of lowercase 'x' chars in the string.
     */
    public int countX(String str) {
        if (str.length() == 0) return 0;
        else return str.substring(0, 1).equals("x")
                ? 1 + countX(str.substring(1))
                : countX(str.substring(1));
    }

    /** countHi
     * Given a string, compute recursively (no loops) the number of times lowercase "hi" appears in the string.
     */
    public int countHi(String str) {
        if (str.length() < 2) return 0;
        else return str.substring(0, 2).equals("hi")
                ? 1 + countHi(str.substring(1))
                : countHi(str.substring(1));
    }

    /** changeXY
     * Given a string, compute recursively (no loops) a new string where all the lowercase 'x' chars have been changed
     * to 'y' chars.
     */
    public String changeXY(String str) {
        if (str.length() == 0) return "";
        else return str.substring(0, 1).equals("x")
                ? "y" + changeXY(str.substring(1))
                : str.substring(0, 1) + changeXY(str.substring(1));
    }

    /** changePi
     * Given a string, compute recursively (no loops) a new string where all appearances of "pi" have been replaced by
     * "3.14".
     */
    public String changePi(String str) {
        if (str.length() < 2) return str;
        else return str.substring(0, 2).equals("pi")
                ? "3.14" + changePi(str.substring(2))
                : str.substring(0, 1) + changePi(str.substring(1));
    }

    /** noX
     * Given a string, compute recursively a new string where all the 'x' chars have been removed.
     */
    public String noX(String str) {
        if (str.length() == 0) return "";
        else return str.substring(0, 1).equals("x")
                ? noX(str.substring(1))
                : str.substring(0, 1) + noX(str.substring(1));
    }

    /** array6
     * Given an array of ints, compute recursively if the array contains a 6. We'll use the convention of considering
     * only the part of the array that begins at the given index. In this way, a recursive call can pass index+1 to move
     * down the array. The initial call will pass in index as 0.
     */
    public boolean array6(int[] nums, int index) {
        if (index == nums.length) return false;
        else if (nums[index] == 6) return true;
        else return array6(nums, index+=1);
    }

    /** array11
     * Given an array of ints, compute recursively the number of times that the value 11 appears in the array. We'll use
     * the convention of considering only the part of the array that begins at the given index. In this way, a recursive
     * call can pass index+1 to move down the array. The initial call will pass in index as 0.
     */
    public int array11(int[] nums, int index) {
        if (index == nums.length) return 0;
        else if (nums[index] == 11) return 1 + array11(nums, index+=1);
        else return array11(nums, index+=1);
    }

    /** array220
     * Given an array of ints, compute recursively if the array contains somewhere a value followed in the array by that
     * value times 10. We'll use the convention of considering only the part of the array that begins at the given
     * index. In this way, a recursive call can pass index+1 to move down the array. The initial call will pass in index
     * as 0.
     */
    public boolean array220(int[] nums, int index) {
        if (index == nums.length) return false;
        else if (index == 0) return array220(nums, index+=1);
        else if (nums[index] % 10 == 0 && nums[index] / 10 == nums[index-1]) return true;
        else return array220(nums, index+=1);
    }

    /** allStar
     * Given a string, compute recursively a new string where all the adjacent chars are now separated by a "*".
     */
    public String allStar(String str) {
        if (str.length() < 2) return str;
        else return str.substring(0, 1) + "*" + allStar(str.substring(1));
    }

    /** pairStar
     * Given a string, compute recursively a new string where identical chars that are adjacent in the original string
     * are separated from each other by a "*".
     */
    public String pairStar(String str) {
        if (str.length() < 2) return str;
        else if (str.substring(0, 1).equals(str.substring(1, 2)))
            return str.substring(0, 1) + "*" + pairStar(str.substring(1));
        else return str.substring(0, 1) + pairStar(str.substring(1));
    }

    /** endX
     * Given a string, compute recursively a new string where all the lowercase 'x' chars have been moved to the end of
     * the string.
     */
    public String endX(String str) {
        if (str.length() == 0)
            return "";
        else if (str.substring(0, 1).equals("x"))
            return endX(str.substring(1)) + "x";
        else
            return str.substring(0, 1) + endX(str.substring(1));
    }

    /** countPairs
     * We'll say that a "pair" in a string is two instances of a char separated by a char. So "AxA" the A's make a pair.
     * Pair's can overlap, so "AxAxA" contains 3 pairs -- 2 for A and 1 for x. Recursively compute the number of pairs
     * in the given string.
     */
    public int countPairs(String str) {
        if (str.length() < 3)
            return 0;
        else if (str.substring(0, 1).equals(str.substring(2, 3)))
            return 1 + countPairs(str.substring(1));
        else
            return countPairs(str.substring(1));
    }

    /** countAbc
     * Count recursively the total number of "abc" and "aba" substrings that appear in the given string.
     */
    public int countAbc(String str) {
        if (str.length() < 3)
            return 0;
        else if (str.substring(0, 3).equals("abc") || str.substring(0, 3).equals("aba"))
            return 1 + countAbc(str.substring(1));
        else
            return countAbc(str.substring(1));
    }

    /** count11
     * Given a string, compute recursively (no loops) the number of "11" substrings in the string. The "11" substrings
     * should not overlap.
     */
    public int count11(String str) {
        if (str.length() < 2)
            return 0;
        else if (str.substring(0, 2).equals("11"))
            return 1 + count11(str.substring(2));
        else
            return count11(str.substring(1));
    }

    /** stringClean
     * Given a string, return recursively a "cleaned" string where adjacent chars that are the same have been reduced to
     * a single char. So "yyzzza" yields "yza".
     */
    public String stringClean(String str) {
        if (str.length() < 2)
            return str;
        else if (str.substring(0, 1).equals(str.substring(1, 2)))
            return stringClean(str.substring(1));
        else
            return str.substring(0, 1) + stringClean(str.substring(1));
    }

    /** countHi2
     * Given a string, compute recursively the number of times lowercase "hi" appears in the string, however do not
     * count "hi" that have an 'x' immedately before them.
     */
    public int countHi2(String str) {
        if (str.length() < 2)
            return 0;
        else if (str.length() < 3)
            return str.substring(0, 2).equals("hi")
                    ? 1 : 0;
        else if (str.substring(0, 2).equals("hi"))
            return 1 + countHi2(str.substring(1));
        else if (str.substring(1, 3).equals("hi"))
            return str.substring(0, 1).equals("x")
                    ? countHi2(str.substring(2)) : 1 + countHi2(str.substring(2));
        else
            return countHi2(str.substring(1));
    }

    /** parenBit
     * Given a string that contains a single pair of parenthesis, compute recursively a new string made of only of the
     * parenthesis and their contents, so "xyz(abc)123" yields "(abc)".
     */
    public String parenBit(String str) {
        int len = str.length();
        if (!str.substring(0, 1).equals("("))
            return parenBit(str.substring(1));
        else if (!str.substring(len-1).equals(")"))
            return parenBit(str.substring(0, len-1));
        else return str;
    }

    /** nestParen
     * Given a string, return true if it is a nesting of zero or more pairs of parenthesis, like "(())" or "((()))".
     */
    public boolean nestParen(String str) {
        int len = str.length();
        if (len == 0)
            return true;
        else if (str.substring(0, 1).equals("(") && str.substring(len-1).equals(")"))
            return nestParen(str.substring(1, len-1));
        else
            return false;
    }

    /** strCount
     * Given a string and a non-empty substring sub, compute recursively the number of times that sub appears in the
     * string, without the sub strings overlapping.
     */
    public int strCount(String str, String sub) {
        int strlen = str.length();
        int sublen = sub.length();
        if (strlen < sublen)
            return 0;
        else if (str.substring(0, sublen).equals(sub))
            return 1 + strCount(str.substring(sublen), sub);
        else
            return strCount(str.substring(1), sub);
    }

    /** strCopies
     * Given a string and a non-empty substring sub, compute recursively if at least n copies of sub appear in the
     * string somewhere, possibly with overlapping. N will be non-negative.
     */
    public boolean strCopies(String str, String sub, int n) {
        int strlen = str.length();
        int sublen = sub.length();
        if (strlen < sublen)
            return n == 0;
        else if (str.substring(0, sublen).equals(sub))
            return strCopies(str.substring(1), sub, n-1);
        else
            return strCopies(str.substring(1), sub, n);
    }

    /** strDist
     * Given a string and a non-empty substring sub, compute recursively the largest substring which starts and ends
     * with sub and return its length.
     */
    public int strDist(String str, String sub) {
        int strlen = str.length();
        int sublen = sub.length();
        if (strlen < sublen)
            return 0;
        else if (str.substring(0, sublen).equals(sub) && str.substring(strlen-sublen).equals(sub))
            return str.length();
        else if (str.substring(0, sublen).equals(sub))
            return strDist(str.substring(0, strlen-1), sub);
        else if (str.substring(strlen-sublen).equals(sub))
            return strDist(str.substring(1), sub);
        else
            return strDist(str.substring(1), sub);
    }
}