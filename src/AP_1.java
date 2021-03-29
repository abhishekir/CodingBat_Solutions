import java.util.ArrayList;

/**
 * https://codingbat.com/java/AP-1
 * AP CS medium problems.
 */
public class AP_1 {
    /** scoresIncreasing
     * Given an array of scores, return true if each score is equal or greater than the one before. The array will be
     * length 2 or more.
     */
    public boolean scoresIncreasing(int[] scores) {
        int prev = scores[0];
        for (int i = 1; i < scores.length; i++) {
            if (scores[i] < prev) return false;
            prev = scores[i];
        }
        return true;
    }

    /** scores100
     * Given an array of scores, return true if there are scores of 100 next to each other in the array. The array
     * length will be at least 2.
     */
    public boolean scores100(int[] scores) {
        boolean seen100 = false;
        for (int i = 0; i < scores.length; i++) {
            if (scores[i] == 100) {
                if (seen100) return true;
                else seen100 = true;
            } else seen100 = false;
        }
        return false;
    }

    /** scoresClump
     * Given an array of scores sorted in increasing order, return true if the array contains 3 adjacent scores that
     * differ from each other by at most 2, such as with {3, 4, 5} or {3, 5, 5}.
     */
    public boolean scoresClump(int[] scores) {
        if (scores.length < 3) return false;
        boolean prev2Diff = false;
        int prev = scores[0];

        for (int i = 0; i < scores.length-2; i++) {
            int a = scores[i];
            int b = scores[i+1];
            int c = scores[i+2];
            if (Math.abs(a-c) < 3 && Math.abs(a-b) < 3 && Math.abs(b-c) < 3)
                return true;
        }
        return false;
    }

    /** scoresAverage
     * Given an array of scores, compute the int average of the first half and the second half, and return whichever is
     * larger. We'll say that the second half begins at index length/2. The array length will be at least 2.
     */
    public int scoresAverage(int[] scores) {
        int halfidx = scores.length / 2;
        int firstavg = average(scores, 0, halfidx);
        int secondavg = average(scores, halfidx, scores.length);

        return Math.max(firstavg, secondavg);
    }

    int average(int[] scores, int start, int end) {
        int sum = 0;
        for (int i = start; i < end; i++) {
            sum += scores[i];
        }
        return sum / (end-start);
    }

    /** wordsCount
     * Given an array of strings, return the count of the number of strings with the given length.
     */
    public int wordsCount(String[] words, int len) {
        int count = 0;

        for (int i = 0; i < words.length; i++) {
            if (words[i].length() == len) count++;
        }

        return count;
    }

    /** wordsFront
     * Given an array of strings, return a new array containing the first N strings. N will be in the range 1..length.
     */
    public String[] wordsFront(String[] words, int n) {
        String[] result = new String[n];

        for (int i = 0; i < n; i++) {
            result[i] = words[i];
        }

        return result;
    }

    /** wordsWithoutList
     * Given an array of strings, return a new List (e.g. an ArrayList) where all the strings of the given length are
     * omitted.
     */
    public ArrayList<String> wordsWithoutList(String[] words, int len) {
        ArrayList<String> res = new ArrayList<String>();

        for (int i = 0; i < words.length; i++) {
            if (words[i].length() != len) res.add(words[i]);
        }

        return res;
    }

    /** hasOne
     * Given a positive int n, return true if it contains a 1 digit.
     */
    public boolean hasOne(int n) {
        if (n == 1) return true;
        else if (n / 10 == 0) return false;
        else if (n % 10 == 1) return true;
        else return hasOne(n / 10);
    }

    /** dividesSelf
     * We'll say that a positive int divides itself if every digit in the number divides into the number evenly. So for
     * example 128 divides itself since 1, 2, and 8 all divide into 128 evenly. We'll say that 0 does not divide into
     * anything evenly, so no number with a 0 digit divides itself.
     */
    public boolean dividesSelf(int n) {
        return dividesSelf(n, n);
    }

    boolean dividesSelf(int n, int rem) {
        int r = rem % 10; //rightmost digit of remainder
        if (r == 0) return false;
        else if (n % r != 0) return false;
        else if (rem / 10 == 0 && n % r == 0) return true;
        else return dividesSelf(n, rem/10);
    }

    /** copyEvens
     * Given an array of positive ints, return a new array of length "count" containing the first even numbers from the
     * original array. The original array will contain at least "count" even numbers.
     */
    public int[] copyEvens(int[] nums, int count) {
        int[] res = new int[count];

        int idx = 0;
        for (int i = 0; i < nums.length && idx < count; i++) {
            if (nums[i] % 2 == 0) {
                res[idx] = nums[i];
                idx++;
            }
        }

        return res;
    }

    /** copyEndy
     * We'll say that a positive int n is "endy" if it is in the range 0..10 or 90..100 (inclusive). Given an array of
     * positive ints, return a new array of length "count" containing the first endy numbers from the original array.
     */
    public int[] copyEndy(int[] nums, int count) {
        int[] res = new int[count];
        int idx = 0;

        for (int i = 0; i < nums.length && idx < count; i++) {
            if (isEndy(nums[i])) {
                res[idx] = nums[i];
                idx++;
            }
        }

        return res;
    }

    boolean isEndy(int n) {
        return n >= 0 && n <= 10 || n >= 90 && n <= 100;
    }

    /** matchUp
     * Given 2 arrays that are the same length containing strings, compare the 1st string in one array to the 1st string
     * in the other array, the 2nd to the 2nd and so on. Count the number of times that the 2 strings are non-empty and
     * start with the same char. The strings may be any length, including 0.
     */
    public int matchUp(String[] a, String[] b) {
        int count = 0;

        for (int i = 0; i < a.length; i++) {
            if (match(a[i], b[i])) count++;
        }

        return count;
    }

    boolean match(String a, String b) {
        return !a.isEmpty() && !b.isEmpty() && a.substring(0, 1).equals(b.substring(0, 1));
    }

    /** scoreUp
     * The "key" array is an array containing the correct answers to an exam, like {"a", "a", "b", "b"}. the "answers"
     * array contains a student's answers, with "?" representing a question left blank. The two arrays are not empty and
     * are the same length. Return the score for this array of answers, giving +4 for each correct answer, -1 for each
     * incorrect answer, and +0 for each blank answer.
     */
    public int scoreUp(String[] key, String[] answers) {
        int score = 0;

        for (int i = 0; i < key.length; i++) {
            String k = key[i];
            String a = answers[i];

            if (k.equals(a)) score+=4;
            else if (a.equals("?")) continue;
            else score--;
        }

        return score;
    }

    /** wordsWithout
     * Given an array of strings, return a new array without the strings that are equal to the target string. One
     * approach is to count the occurrences of the target string, make a new array of the correct length, and then copy
     * over the correct strings.
     */
    public String[] wordsWithout(String[] words, String target) {
        int count = 0;

        for (int i = 0; i < words.length; i++) {
            if (!words[i].equals(target)) count++;
        }

        String[] result = new String[count];
        count = 0;

        for (int i = 0; i < words.length; i++) {
            if (!words[i].equals(target)) {
                result[count] = words[i];
                count++;
            }
        }

        return result;
    }

    /** scoresSpecial
     * Given two arrays, A and B, of non-negative int scores. A "special" score is one which is a multiple of 10, such
     * as 40 or 90. Return the sum of largest special score in A and the largest special score in B.
     */
    public int scoresSpecial(int[] a, int[] b) {
        return largestSpecial(a) + largestSpecial(b);
    }

    int largestSpecial(int[] a) {
        if (a.length == 0) return 0;
        int largest = 0;

        for (int i = 0; i < a.length; i++) {
            if (a[i] % 10 == 0 && a[i] > largest) largest = a[i];
        }

        return largest;
    }

    /** sumHeights
     * We have an array of heights, representing the altitude along a walking trail. Given start/end indexes into the
     * array, return the sum of the changes for a walk beginning at the start index and ending at the end index. For
     * example, with the heights {5, 3, 6, 7, 2} and start=2, end=4 yields a sum of 1 + 5 = 6. The start end end index
     * will both be valid indexes into the array with start <= end.
     */
    public int sumHeights(int[] heights, int start, int end) {
        int sum = 0;

        for (int i = start; i < end; i++) {
            sum += Math.abs(heights[i+1] - heights[i]);
        }

        return sum;
    }

    /** sumHeights2
     * (A variation on the sumHeights problem.) We have an array of heights, representing the altitude along a walking
     * trail. Given start/end indexes into the array, return the sum of the changes for a walk beginning at the start
     * index and ending at the end index, however increases in height count double. For example, with the heights {5, 3,
     * 6, 7, 2} and start=2, end=4 yields a sum of 1*2 + 5 = 7. The start end end index will both be valid indexes into
     * the array with start <= end.
     */
    public int sumHeights2(int[] heights, int start, int end) {
        int sum = 0;

        for (int i = start; i < end; i++) {
            int current = heights[i];
            int next = heights[i+1];
            int change = next - current;
            if (change > 0) sum += change*2;
            else sum += change*-1;
        }

        return sum;
    }

    /** bigHeights
     * (A variation on the sumHeights problem.) We have an array of heights, representing the altitude along a walking
     * trail. Given start/end indexes into the array, return the number of "big" steps for a walk starting at the start
     * index and ending at the end index. We'll say that step is big if it is 5 or more up or down. The start end end
     * index will both be valid indexes into the array with start <= end.
     */
    public int bigHeights(int[] heights, int start, int end) {
        int count = 0;

        for (int i = start; i < end; i++) {
            if (Math.abs(heights[i+1]-heights[i]) >= 5) count++;
        }

        return count;
    }

    /** userCompare
     * We have data for two users, A and B, each with a String name and an int id. The goal is to order the users such
     * as for sorting. Return -1 if A comes before B, 1 if A comes after B, and 0 if they are the same. Order first by
     * the string names, and then by the id numbers if the names are the same.
     */
    public int userCompare(String aName, int aId, String bName, int bId) {
        if (aName.compareTo(bName) < 0) return -1;
        else if (aName.compareTo(bName) > 0) return 1;
        else if (aId < bId) return -1;
        else if (aId > bId) return 1;
        else return 0;
    }

    /** mergeTwo
     * Start with two arrays of strings, A and B, each with its elements in alphabetical order and without duplicates.
     * Return a new array containing the first N elements from the two arrays. The result array should be in
     * alphabetical order and without duplicates. A and B will both have a length which is N or more. The best "linear"
     * solution makes a single pass over A and B, taking advantage of the fact that they are in alphabetical order,
     * copying elements directly to the new array.
     */
    public String[] mergeTwo(String[] a, String[] b, int n) {
        String[] result = new String[n];

        for (int i = 0, j = 0, count = 0; i < a.length && j < b.length && count < n; i+=0) {
            String acurr = a[i];
            String bcurr = b[j];
            if (acurr.compareTo(bcurr) < 0) {
                result[count] = acurr;
                i++;
            } else if (acurr.compareTo(bcurr) > 0) {
                result[count] = bcurr;
                j++;
            } else {
                result[count] = acurr;
                i++;
                j++;
            }
            count++;
        }

        return result;
    }

    /** commonTwo
     * Start with two arrays of strings, a and b, each in alphabetical order, possibly with duplicates. Return the count
     * of the number of strings which appear in both arrays. The best "linear" solution makes a single pass over both
     * arrays, taking advantage of the fact that they are in alphabetical order.
     */
    public int commonTwo(String[] a, String[] b) {
        int common = 0;
        String prev = "";

        for (int i = 0, j = 0; i < a.length && j < b.length; i+=0) {
            if (a[i].compareTo(b[j]) < 0) i++;
            else if (a[i].compareTo(b[j]) > 0) j++;
            else {
                if (a[i].equals(prev)) {
                    i++;
                    j++;
                } else {
                    prev = a[i];
                    common++;
                    i++;
                    j++;
                }
            }
        }

        return common;
    }
}