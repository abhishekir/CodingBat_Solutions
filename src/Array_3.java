/**
 * https://codingbat.com/java/Array-3
 * Harder array problems -- 2 loops, more complex logic.
 */
public class Array_3 {
    /** maxSpan
     * Consider the leftmost and righmost appearances of some value in an array. We'll say that the "span" is the number
     * of elements between the two inclusive. A single value has a span of 1. Returns the largest span found in the
     * given array.
     */
    public int maxSpan(int[] nums) {
        if (nums.length == 0) return 0;
        else if (nums.length == 1) return 1;

        int largestSpan = 1;
        int val;
        int span;

        for (int i = 0; i < nums.length; i++) {
            val = nums[i];
            for (int j = nums.length-1; j > i; j--) {
                if (val == nums[j]) {
                    span = j-i+1;
                    if (span > largestSpan) largestSpan = span;
                    break;
                }
            }
        }

        return largestSpan;
    }

    /** fix34
     * Return an array that contains exactly the same numbers as the given array, but rearranged so that every 3 is
     * immediately followed by a 4. Do not move the 3's, but every other number may move. The array contains the same
     * number of 3's and 4's, every 3 has a number after it that is not a 3, and a 3 appears in the array before any 4.
     */
    public int[] fix34(int[] nums) {
        int len = nums.length;

        for (int i = 0; i < len-1; i++) {
            if (nums[i] == 3 && nums[i+1] != 4) {
                for (int j = len-1; j > 0; j--) {
                    if (nums[j] == 4 && nums[j-1] != 3) {
                        nums[j] = nums[i+1];
                        nums[i+1] = 4;
                    }
                }
            }
        }

        return nums;
    }

    /** fix45
     * (This is a slightly harder version of the fix34 problem.) Return an array that contains exactly the same numbers
     * as the given array, but rearranged so that every 4 is immediately followed by a 5. Do not move the 4's, but every
     * other number may move. The array contains the same number of 4's and 5's, and every 4 has a number after it that
     * is not a 4. In this version, 5's may appear anywhere in the original array.
     */
    public int[] fix45(int[] nums) {
        int len = nums.length;

        for (int i = 0; i < len-1; i++) {
            if (nums[i] == 4 && nums[i+1] != 5) {
                for (int j = len-1; j >= 0; j--) {
                    if (nums[j] == 5 && (j == 0 || nums[j-1] != 4)) {
                        nums[j] = nums[i+1];
                        nums[i+1] = 5;
                    }
                }
            }
        }

        return nums;
    }

    /** canBalance
     * Given a non-empty array, return true if there is a place to split the array so that the sum of the numbers on one
     * side is equal to the sum of the numbers on the other side.
     */
    public boolean canBalance(int[] nums) {
        int len = nums.length;

        if (len < 2) return false;

        for (int i = 1; i < len; i++) {
            int lsum = 0;
            for (int j = 0; j < i; j++) {
                lsum += nums[j];
            }
            int rsum = 0;
            for (int k = len-1; k >= i; k--) {
                rsum += nums[k];
            }
            if (lsum == rsum) return true;
        }

        return false;
    }

    /** linearIn
     * Given two arrays of ints sorted in increasing order, outer and inner, return true if all of the numbers in inner
     * appear in outer. The best solution makes only a single "linear" pass of both arrays, taking advantage of the fact
     * that both arrays are already in sorted order.
     */
    public boolean linearIn(int[] outer, int[] inner) {
        if (inner.length == 0) return true;
        int inneridx = 0;

        for (int i = 0; i < outer.length; i++) {
            if (outer[i] == inner[inneridx])
                inneridx++;
            if (inneridx == inner.length)
                return true;
        }

        return false;
    }

    /** squareUp
     * Given n>=0, create an array length n*n with the following pattern, shown here for n=3 : {0, 0, 1, 0, 2, 1, 3, 2,
     * 1}
     */
    public int[] squareUp(int n) {
        int[] res = new int[n*n];
        int max = n;
        int inc = 1;

        for (int i = res.length - 1; i >= 0; i-=n) {
            for (int j = i; j > i-n; j--) {
                if (inc <= max) {
                    res[j] = inc;
                    inc++;
                } else
                    res[j] = 0;
            }
            max -= 1;
            inc = 1;
        }

        return res;
    }

    /** seriesUp
     * Given n>=0, create an array with the pattern {1,    1, 2,    1, 2, 3,   ... 1, 2, 3 .. n} (spaces added to show
     * the grouping).
     */
    public int[] seriesUp(int n) {
        int reslen = (n*(n+1))/2;
        int[] res = new int[reslen];
        int s = 1;
        int max = 1;

        for (int i = 0; i < reslen; i++) {
            res[i] = s;
            s++;
            if (s > max) {
                max += 1;
                s = 1;
            }
        }

        return res;
    }

    /** maxMirror
     * We'll say that a "mirror" section in an array is a group of contiguous elements such that somewhere in the array,
     * the same group appears in reverse order. For example, the largest mirror section in {1, 2, 3, 8, 9, 3, 2, 1} is
     * length 3 (the {1, 2, 3} part). Return the size of the largest mirror section found in the given array.
     */
    public int maxMirror(int[] nums) {
        int len = nums.length;
        int max = 0;

        for (int i = 0; i < len; i++) {
            int count = 0;
            for (int j = nums.length - 1; j >= 0 && i + count < nums.length; j--) {
                if(nums[i + count] == nums[j])
                    count++;
                else {
                    max = Math.max(max, count);
                    count = 0;
                }
            }
            max = Math.max(max, count);
        }

        return max;
    }

    /** countClumps
     * Say that a "clump" in an array is a series of 2 or more adjacent elements of the same value. Return the number of
     * clumps in the given array.
     */
    public int countClumps(int[] nums) {
        int len = nums.length;
        if (len < 2) return 0;

        boolean newclump = true;
        int count = 0;
        int prev = nums[0];
        int curr;

        for (int i = 1; i < nums.length; i++) {
            curr = nums[i];
            if (curr == prev) {
                if (newclump) {
                    count++;
                    newclump = false;
                }
            } else {
                newclump = true;
            }
            prev = curr;
        }

        return count;
    }
}