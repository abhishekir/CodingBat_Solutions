/**
 * https://codingbat.com/java/Array-2
 * Medium array problems -- 1 loop.
 */
public class Array_2 {
    /** countEvens
     * Return the number of even ints in the given array.
     */
    public int countEvens(int[] nums) {
        int count = 0;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] % 2 == 0) count++;
        }
        return count;
    }

    /** bigDiff
     * Given an array length 1 or more of ints, return the difference between the largest and smallest values in the
     * array.
     */
    public int bigDiff(int[] nums) {
        int smallest = nums[0];
        int largest = nums[0];
        for (int i = 1; i < nums.length; i++) {
            smallest = Math.min(smallest, nums[i]);
            largest = Math.max(largest, nums[i]);
        }
        return largest - smallest;
    }

    /** centeredAverage
     * Return the "centered" average of an array of ints, which we'll say is the mean average of the values, except
     * ignoring the largest and smallest values in the array. If there are multiple copies of the smallest value, ignore
     * just one copy, and likewise for the largest value. Use int division to produce the final average. You may assume
     * that the array is length 3 or more.
     */
    public int centeredAverage(int[] nums) {
        int smallest = nums[0];
        int largest = nums[0];
        int sum = nums[0];

        for (int i = 1; i < nums.length; i++) {
            smallest = Math.min(smallest, nums[i]);
            largest = Math.max(largest, nums[i]);
            sum += nums[i];
        }

        int result = (sum-smallest-largest)/(nums.length-2);
        return result;
    }

    /** sum13
     * Return the sum of the numbers in the array, returning 0 for an empty array. Except the number 13 is very unlucky,
     * so it does not count and numbers that come immediately after a 13 also do not count.
     */
    public int sum13(int[] nums) {
        int sum = 0;
        boolean after13 = false;

        for (int i = 0; i < nums.length; i++) {
            int j = nums[i];
            if (j == 13) after13 = true;
            else if (after13) after13 = false;
            else sum += j;
        }

        return sum;
    }

    /** sum67
     * Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to
     * the next 7 (every 6 will be followed by at least one 7). Return 0 for no numbers.
     */
    public int sum67(int[] nums) {
        int sum = 0;
        boolean seen6 = false;

        for (int i = 0; i < nums.length; i++) {
            int j = nums[i];
            if (j == 6) seen6 = true;
            else if (seen6 && j == 7) seen6 = false;
            else if (!seen6) sum += j;
        }

        return sum;
    }

    /** has22
     * Given an array of ints, return true if the array contains a 2 next to a 2 somewhere.
     */
    public boolean has22(int[] nums) {
        boolean seen2 = false;
        for (int i = 0; i < nums.length; i++) {
            int j = nums[i];
            if (!seen2 && j == 2) seen2 = true;
            else if (seen2 && j == 2) return true;
            else seen2 = false;
        }
        return false;
    }

    /** lucky13
     * Given an array of ints, return true if the array contains no 1's and no 3's.
     */
    public boolean lucky13(int[] nums) {
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] == 1 || nums[i] == 3) return false;
        }
        return true;
    }

    /** sum28
     * Given an array of ints, return true if the sum of all the 2's in the array is exactly 8.
     */
    public boolean sum28(int[] nums) {
        int sum = 0;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] == 2) sum += 2;
        }
        return sum == 8;
    }

    /** more14
     * Given an array of ints, return true if the number of 1's is greater than the number of 4's
     */
    public boolean more14(int[] nums) {
        int count1 = 0;
        int count4 = 0;

        for (int i = 0; i < nums.length; i++) {
            if (nums[i] == 1) count1++;
            else if (nums[i] == 4) count4++;
        }

        return count1 > count4;
    }

    /** fizzArray
     * Given a number n, create and return a new int array of length n, containing the numbers 0, 1, 2, ... n-1. The
     * given n may be 0, in which case just return a length 0 array. You do not need a separate if-statement for the
     * length-0 case; the for-loop should naturally execute 0 times in that case, so it just works. The syntax to make a
     * new int array is: new int[desired_length]
     */
    public int[] fizzArray(int n) {
        int[] result = new int[n];
        for (int i = 0; i < n; i++) result[i] = i;
        return result;
    }

    /** only14
     * Given an array of ints, return true if every element is a 1 or a 4.
     */
    public boolean only14(int[] nums) {
        for (int i = 0; i < nums.length; i++)
            if (nums[i] != 1 && nums[i] != 4) return false;
        return true;
    }

    /** fizzArray2
     * Given a number n, create and return a new string array of length n, containing the strings "0", "1" "2" ..
     * through n-1. N may be 0, in which case just return a length 0 array.
     */
    public String[] fizzArray2(int n) {
        String[] arr = new String[n];
        for (int i = 0; i < n; i++)
            arr[i] = String.valueOf(i);
        return arr;
    }

    /** no14
     * Given an array of ints, return true if it contains no 1's or it contains no 4's.
     */
    public boolean no14(int[] nums) {
        boolean has1 = false;
        boolean has4 = false;
        for (int i = 0; i < nums.length; i++) {
            int j = nums[i];
            if (j == 1) has1 = true;
            else if (j == 4) has4 = true;
        }
        return !(has1 && has4);
    }

    /** isEverywhere
     * We'll say that a value is "everywhere" in an array if for every pair of adjacent elements in the array, at least
     * one of the pair is that value. Return true if the given value is everywhere in the array.
     */
    public boolean isEverywhere(int[] nums, int val) {
        boolean res = true;
        for (int i = 0; i < nums.length - 1; i++) {
            res = res && (nums[i] == val || nums[i+1] == val);
        }
        return res;
    }

    /** either24
     * Given an array of ints, return true if the array contains a 2 next to a 2 or a 4 next to a 4, but not both.
     */
    public boolean either24(int[] nums) {
        boolean double2 = false;
        boolean double4 = false;
        for (int i = 0; i < nums.length-1; i++) {
            int j = nums[i];
            int k = nums[i+1];
            if (j == 2 && k == 2) double2 = true;
            else if (j == 4 && k == 4) double4 = true;
        }
        return double2 ^ double4;
    }

    /** matchUp
     * Given arrays nums1 and nums2 of the same length, for every element in nums1, consider the corresponding element
     * in nums2 (at the same index). Return the count of the number of times that the two elements differ by 2 or less,
     * but are not equal.
     */
    public int matchUp(int[] nums1, int[] nums2) {
        int count = 0;
        for (int i = 0; i < nums1.length; i++) {
            if (Math.abs(nums1[i]-nums2[i]) <= 2 && nums1[i] != nums2[i]) count++;
        }
        return count;
    }

    /** has77
     * Given an array of ints, return true if the array contains two 7's next to each other, or there are two 7's
     * separated by one element, such as with {7, 1, 7}.
     */
    public boolean has77(int[] nums) {
        boolean seen7 = false;
        boolean skip = false;

        for (int i = 0; i < nums.length; i++) {
            int j = nums[i];
            if (j == 7) {
                if (seen7) {
                    return true;
                } else {
                    seen7 = true;
                    skip = true;
                }
            }
            else if (skip)
                skip = false;
            else
                seen7 = false;
        }

        return false;
    }

    /** has12
     * Given an array of ints, return true if there is a 1 in the array with a 2 somewhere later in the array.
     */
    public boolean has12(int[] nums) {
        boolean seen1 = false;

        for (int i = 0; i < nums.length; i++) {
            if (nums[i] == 1) seen1 = true;
            if (seen1 && nums[i] == 2) return true;
        }

        return false;
    }

    /** modThree
     * Given an array of ints, return true if the array contains either 3 even or 3 odd values all next to each other.
     */
    public boolean modThree(int[] nums) {
        int len = nums.length;
        if (len < 3) return false;

        boolean prevodd = nums[0] % 2 == 1;
        boolean match1 = false;

        for (int i = 1; i < nums.length; i++) {
            boolean odd = nums[i] % 2 == 1;
            if (odd != prevodd) match1 = false;
            else if (!match1) match1 = true;
            else return true;
            prevodd = odd;
        }
        return false;
    }

    /** haveThree
     * Given an array of ints, return true if the value 3 appears in the array exactly 3 times, and no 3's are next to
     * each other.
     */
    public boolean haveThree(int[] nums) {
        int len = nums.length;
        if (len < 3) return false;

        boolean near3 = false;
        int count3 = 0;

        for (int i = 0; i < nums.length; i++) {
            int j = nums[i];
            if (j == 3) {
                count3++;
                if (near3) return false;
                else near3 = true;
            } else {
                near3 = false;
            }
        }

        return count3 == 3;
    }

    /** twoTwo
     * Given an array of ints, return true if every 2 that appears in the array is next to another 2.
     */
    public boolean twoTwo(int[] nums) {
        int len = nums.length;
        boolean seen2 = false;

        if (len == 0) return true;
        else if (len == 1) return nums[0] == 2 ? false : true;
        else if (nums[0] == 2) seen2 = true;

        for (int i = 1; i < len-1; i++) {
            if (nums[i] == 2) {
                if (!(seen2 || nums[i+1] == 2)) return false;
                seen2 = true;
            } else seen2 = false;
        }

        if (nums[len-1] == 2 && nums[len-2] != 2) return false;

        return true;
    }

    /** sameEnds
     * Return true if the group of N numbers at the start and end of the array are the same. For example, with {5, 6,
     * 45, 99, 13, 5, 6}, the ends are the same for n=0 and n=2, and false for n=1 and n=3. You may assume that n is in
     * the range 0..nums.length inclusive.
     */
    public boolean sameEnds(int[] nums, int len) {
        for (int i = 0; i < len; i++) {
            if (nums[i] != nums[nums.length-len+i]) return false;
        }
        return true;
    }

    /** tripleUp
     * Return true if the array contains, somewhere, three increasing adjacent numbers like .... 4, 5, 6, ... or 23, 24,
     * 25.
     */
    public boolean tripleUp(int[] nums) {
        int len = nums.length;
        if (len < 3) return false;
        int prev = nums[0];
        boolean doubleup = false;

        for (int i = 1; i < len; i++) {
            if (nums[i] == prev+1) {
                if (doubleup) return true;
                else doubleup = true;
            } else {
                doubleup = false;
            }
            prev = nums[i];
        }

        return false;
    }

    /** fizzArray3
     * Given start and end numbers, return a new array containing the sequence of integers from start up to but not
     * including end, so start=5 and end=10 yields {5, 6, 7, 8, 9}. The end number will be greater or equal to the start
     * number.
     */
    public int[] fizzArray3(int start, int end) {
        int[] result = new int[end-start];
        int j = 0;

        for (int i = start; i < end; i++) {
            result[j] = i;
            j++;
        }

        return result;
    }

    /** shiftLeft
     * Return an array that is "left shifted" by one -- so {6, 2, 5, 3} returns {2, 5, 3, 6}. You may modify and return
     * the given array, or return a new array.
     */
    public int[] shiftLeft(int[] nums) {
        int len = nums.length;
        if (len < 2) return nums;
        int[] result = new int[len];

        for (int i = 0; i < len-1; i++) {
            result[i] = nums[i+1];
        }
        result[len-1] = nums[0];

        return result;
    }

    /** tenRun
     * For each multiple of 10 in the given array, change all the values following it to be that multiple of 10, until
     * encountering another multiple of 10. So {2, 10, 3, 4, 20, 5} yields {2, 10, 10, 10, 20, 20}.
     */
    public int[] tenRun(int[] nums) {
        int len = nums.length;
        int[] result = new int[len];
        int currentmul = 0;
        boolean seenmul = false;

        for (int i = 0; i < len; i++) {
            if (nums[i] % 10 == 0) {
                seenmul = true;
                currentmul = nums[i];
            }
            if (seenmul) result[i] = currentmul;
            else result[i] = nums[i];
        }

        return result;
    }

    /** pre4
     * Given a non-empty array of ints, return a new array containing the elements from the original array that come
     * before the first 4 in the original array. The original array will contain at least one 4.
     */
    public int[] pre4(int[] nums) {
        int len = nums.length;
        int idx4 = 0;
        for (int i = 0; i < len; i++) {
            if (nums[i] == 4) {
                idx4 = i;
                break;
            }
        }

        int[] result = new int[idx4];

        for (int i = 0; i < idx4; i++) {
            result[i] = nums[i];
        }

        return result;
    }

    /** post4
     * Given a non-empty array of ints, return a new array containing the elements from the original array that come
     * after the last 4 in the original array. The original array will contain at least one 4.
     */
    public int[] post4(int[] nums) {
        int len = nums.length;
        int idx4 = 0;
        for (int i = 0; i < len; i++) {
            if (nums[i] == 4) {
                idx4 = i;
            }
        }

        int[] result = new int[len-idx4-1];
        int idx = 0;
        for (int i = idx4+1; i < len; i++) {
            result[idx] = nums[i];
            idx++;
        }

        return result;
    }

    /** notAlone
     * We'll say that an element in an array is "alone" if there are values before and after it, and those values are
     * different from it. Return a version of the given array where every instance of the given value which is alone is
     * replaced by whichever value to its left or right is larger.
     */
    public int[] notAlone(int[] nums, int val) {
        int len = nums.length;
        if (len < 3) return nums;
        int[] result = new int[len];
        result[0] = nums[0];

        result[len-1] = nums[len-1];
        for (int i = 1; i < len-1; i++) {
            int current = nums[i];
            int before = nums[i-1];
            int after = nums[i+1];
            if (current == val && !(before==val || after==val)) {
                result[i] = Math.max(before, after);
            } else {
                result[i] = current;
            }
        }

        return result;
    }

    /** zeroFront
     * Return an array that contains the exact same numbers as the given array, but rearranged so that all the zeros are
     * grouped at the start of the array. The order of the non-zero numbers does not matter. So {1, 0, 0, 1} becomes {0,
     * 0, 1, 1}. You may modify and return the given array or make a new array.
     */
    public int[] zeroFront(int[] nums) {
        int firstNon0 = 0;
        boolean foundNon0 = false;

        for (int i = 0; i < nums.length; i++) {
            if (foundNon0) {
                if (nums[i] == 0) {
                    int temp = nums[i];
                    nums[i] = nums[firstNon0];
                    nums[firstNon0] = temp;
                    firstNon0++;
                } else continue;
            }
            else if (nums[i] != 0) {
                firstNon0 = i;
                foundNon0 = true;
            }
        }

        return nums;
    }

    /** withoutTen
     * Return a version of the given array where all the 10's have been removed. The remaining elements should shift
     * left towards the start of the array as needed, and the empty spaces a the end of the array should be 0. So {1,
     * 10, 10, 2} yields {1, 2, 0, 0}. You may modify and return the given array or make a new array.
     */
    public int[] withoutTen(int[] nums) {
        int first10idx = 0;
        boolean found10 = false;
        for (int i = 0; i < nums.length; i++) {
            if (found10) {
                if (nums[i] == 10) {
                    nums[i] = 0;
                    continue;
                } else {
                    nums[first10idx] = nums[i];
                    nums[i] = 0;
                    first10idx++;
                }
            } else if (nums[i] == 10) {
                nums[i] = 0;
                found10 = true;
                first10idx = i;
            }
        }

        return nums;
    }

    /** zeroMax
     * Return a version of the given array where each zero value in the array is replaced by the largest odd value to
     * the right of the zero in the array. If there is no odd value to the right of the zero, leave the zero as a zero.
     */
    public int[] zeroMax(int[] nums) {
        int largest_odd = 0;
        int len = nums.length;

        for (int i = len-1; i >= 0; i--) {
            int curr = nums[i];
            if (curr % 2 == 1 && curr > largest_odd) largest_odd = curr;
            else if (nums[i] == 0) nums[i] = largest_odd;
        }

        return nums;
    }

    /** evenOdd
     * Return an array that contains the exact same numbers as the given array, but rearranged so that all the even
     * numbers come before all the odd numbers. Other than that, the numbers can be in any order. You may modify and
     * return the given array, or make a new array.
     */
    public int[] evenOdd(int[] nums) {
        int firstOddIdx = 0;
        boolean foundOdd = false;

        for (int i = 0; i < nums.length; i++) {
            boolean odd = nums[i] % 2 == 1;
            if (foundOdd) {
                if (!odd) {
                    int temp = nums[i];
                    nums[i] = nums[firstOddIdx];
                    nums[firstOddIdx] = temp;
                    firstOddIdx++;
                } else continue;
            } else if (odd) {
                foundOdd = true;
                firstOddIdx = i;
            }
        }

        return nums;
    }

    /** fizzBuzz
     * This is slightly more difficult version of the famous FizzBuzz problem which is sometimes given as a first
     * problem for job interviews. (See also: FizzBuzz Code.) Consider the series of numbers beginning at start and
     * running up to but not including end, so for example start=1 and end=5 gives the series 1, 2, 3, 4. Return a new
     * String[] array containing the string form of these numbers, except for multiples of 3, use "Fizz" instead of the
     * number, for multiples of 5 use "Buzz", and for multiples of both 3 and 5 use "FizzBuzz". In Java,
     * String.valueOf(xxx) will make the String form of an int or other type. This version is a little more complicated
     * than the usual version since you have to allocate and index into an array instead of just printing, and we vary
     * the start/end instead of just always doing 1..100.
     */
    public String[] fizzBuzz(int start, int end) {
        String[] result = new String[end-start];
        int val = start;

        for (int i = 0; i < result.length; i++) {
            boolean mod3 = val % 3 == 0;
            boolean mod5 = val % 5 == 0;
            if (mod3 && mod5) result[i] = "FizzBuzz";
            else if (mod3) result[i] = "Fizz";
            else if (mod5) result[i] = "Buzz";
            else result[i] = String.valueOf(val);
            val++;
        }

        return result;
    }
}