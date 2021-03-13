/**
 * https://codingbat.com/java/Warmup-2
 * Medium warmup string/array loops
 */
public class Warmup_2 {
    /** stringTimes
     * Given a string and a non-negative int n, return a larger string that is n copies of the original string.
     */
    public String stringTimes(String str, int n) {
        String ret = "";
        for (int i = 0; i < n; i++)
            ret += str;
        return ret;
    }

    /** frontTimes
     * Given a string and a non-negative int n, we'll say that the front of the string is the first 3 chars, or whatever
     * is there if the string is less than length 3. Return n copies of the front;
     */
    public String frontTimes(String str, int n) {
        String front;
        if (str.length() < 3) front = str;
        else front = str.substring(0, 3);

        String ret = "";
        for (int i = 0; i < n; i++) {
            ret += front;
        }
        return ret;
    }

    /** countXX
     * Count the number of "xx" in the given string. We'll say that overlapping is allowed, so "xxx" contains 2 "xx".
     */
    int countXX(String str) {
        int count = 0;
        for (int i = 0; i < str.length() - 1; i++) {
            if (str.charAt(i) == str.charAt(i+1) && str.charAt(i) == 'x')
                count++;
        }
        return count;
    }

    /** doubleX
     * Given a string, return true if the first instance of "x" in the string is immediately followed by another "x".
     */
    boolean doubleX(String str) {
        boolean firstX = false;
        for (int i = 0; i < str.length(); i++) {
            char c = str.charAt(i);
            if (c == 'x' && !firstX) firstX = true;
            else if (c == 'x' && firstX) return true;
            else if (firstX) return false;
        }
        return false;
    }

    /** stringBits
     * Given a string, return a new string made of every other char starting with the first, so "Hello" yields "Hlo".
     */
    public String stringBits(String str) {
        String ret = "";
        if (str.length() % 2 == 0) {
            for (int i = 0; i < str.length() - 1; i+=2)
                ret += str.charAt(i);
        } else {
            for (int i = 0; i < str.length(); i+=2)
                ret += str.charAt(i);
        }
        return ret;
    }

    /** stringSplosion
     * Given a non-empty string like "Code" return a string like "CCoCodCode".
     */
    public String stringSplosion(String str) {
        String ret = "";
        for(int i = 0; i < str.length(); i++)
            for(int j = 0; j <= i; j++)
                ret += str.charAt(j);

        return ret;
    }

    /** last2
     * Given a string, return the count of the number of times that a substring length 2 appears in the string and also
     * as the last 2 chars of the string, so "hixxxhi" yields 1 (we won't count the end substring).
     */
    public int last2(String str) {
        String last;
        int count = 0;

        if (str.length() < 2) last = str;
        else last = str.substring(str.length()-2, str.length());

        for (int i = 0; i < str.length()-2; i++)
            if (str.substring(i, i+2).equals(last)) count++;

        return count;
    }

    /** arrayCount9
     * Given an array of ints, return the number of 9's in the array.
     */
    public int arrayCount9(int[] nums) {
        int count = 0;

        for (int i = 0; i < nums.length; i++)
            if (nums[i] == 9) count++;

        return count;
    }

    /** arrayFront9
     * Given an array of ints, return true if one of the first 4 elements in the array is a 9. The array length may be
     * less than 4.
     */
    public boolean arrayFront9(int[] nums) {
        int len = 0;
        if (nums.length < 4) len = nums.length;
        else len = 4;
        boolean b = false;

        for (int i = 0; i < len; i++)
            if (nums[i] == 9) return true;

        return false;
    }

    /** array123
     * Given an array of ints, return true if the sequence of numbers 1, 2, 3 appears in the array somewhere.
     */
    public boolean array123(int[] nums) {
        boolean seq = false;
        boolean seq2 = false;

        int t;
        for (int i = 0; i < nums.length; i++) {
            t = nums[i];
            if (t == 1) seq = true;
            else if (t == 2 && seq) seq2 = true;
            else if (t == 3 && seq2) return true;
            else {
                seq = false;
                seq2 = false;
            }
        }

        return false;
    }

    /** stringMatch
     * Given 2 strings, a and b, return the number of the positions where they contain the same length 2 substring. So
     * "xxcaazz" and "xxbaaz" yields 3, since the "xx", "aa", and "az" substrings appear in the same place in both
     * strings.
     */
    public int stringMatch(String a, String b) {
        int len;
        if (a.length() > b.length()) len = b.length();
        else len = a.length();


        int count = 0;
        for (int i = 0; i < len - 1; i++) {
            if (a.substring(i, i+2).equals(b.substring(i, i+2))) count++;
        }

        return count;
    }

    /** stringX
     * Given a string, return a version where all the "x" have been removed. Except an "x" at the very start or end
     * should not be removed.
     */
    public String stringX(String str) {
        if (str.length() < 2) return str;

        String ret = "";
        ret += str.charAt(0);
        for (int i = 1; i < str.length() - 1; i++)
            if (str.charAt(i) != 'x') ret += str.charAt(i);

        ret += str.charAt(str.length()-1);
        return ret;
    }

    /** altPairs
     * Given a string, return a string made of the chars at indexes 0,1, 4,5, 8,9 ... so "kittens" yields "kien".
     */
    public String altPairs(String str) {
        String ret = "";

        if (str.length() <= 2) return str;
        else {
            for (int i = 0; i < str.length(); i+=4) {
                ret += str.charAt(i);
                if (i+1 < str.length())
                    ret += str.charAt(i+1);
            }

            if (str.length() % 2 != 0 && str.length() % 3 != 0) {
                ret += str.charAt(str.length() - 1);
            }
        }

        return ret;
    }

    /** stringYak
     * Suppose the string "yak" is unlucky. Given a string, return a version where all the "yak" are removed, but the
     * "a" can be any char. The "yak" strings will not overlap.
     */
    public String stringYak(String str) {
        String ret = "";

        for (int i = 0; i < str.length(); i++)
            if (i+2 < str.length() && str.charAt(i) == 'y' && str.charAt(i+2) == 'k')
                i+=2;
            else
                ret += str.charAt(i);

        return ret;
    }

    /** array667
     * Given an array of ints, return the number of times that two 6's are next to each other in the array. Also count
     * instances where the second "6" is actually a 7.
     */
    public int array667(int[] nums) {
        int count = 0;
        for (int i = 0; i < nums.length - 1; i++) {
            if (nums[i] == 6 && (nums[i+1] == 6 || nums[i+1] == 7))
                count++;
        }
        return count;
    }

    /** noTriples
     * Given an array of ints, we'll say that a triple is a value appearing 3 times in a row in the array. Return true
     * if the array does not contain any triples.
     */
    public boolean noTriples(int[] nums) {
        if (nums.length < 3) return true;
        else {
            int last = nums[0];
            boolean dub = false;
            for (int i = 1; i < nums.length; i++) {
                if (last == nums[i] && !dub)
                    dub = true;
                else if (dub && last == nums[i])
                    return false;
                else {
                    dub = false;
                    last = nums[i];
                }
            }
        }
        return true;
    }

    /** has271
     * Given an array of ints, return true if it contains a 2, 7, 1 pattern: a value, followed by the value plus 5,
     * followed by the value minus 1. Additionally the 271 counts even if the "1" differs by 2 or less from the correct
     * value.
     */
    public boolean has271(int[] nums) {
        int len = nums.length;
        for (int i = 0; i < len - 1; i++) {
            if (i+2 < len){
                int j = Math.abs(nums[i] - 1);
                int k = Math.abs(j - nums[i+2]);
                if(nums[i+1] == nums[i]+5 && k <= 2)
                    return true;
            }
        } return false;
    }
}