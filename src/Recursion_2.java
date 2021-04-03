/**
 * https://codingbat.com/java/Recursion-2
 * Harder recursion problems. Currently, these are all recursive backtracking problems with arrays.
 */
public class Recursion_2 {
    /** groupSum
     * Given an array of ints, is it possible to choose a group of some of the ints, such that the group sums to the
     * given target? This is a classic backtracking recursion problem. Once you understand the recursive backtracking
     * strategy in this problem, you can use the same pattern for many problems to search a space of choices. Rather
     * than looking at the whole array, our convention is to consider the part of the array starting at index start and
     * continuing to the end of the array. The caller can specify the whole array simply by passing start as 0. No loops
     * are needed -- the recursive calls progress down the array.
     */
    public boolean groupSum(int start, int[] nums, int target) {
        if (start >= nums.length)
            return target == 0;
        if (groupSum(start+1, nums, target-nums[start]))
            return true;
        if (groupSum(start+1, nums, target))
            return true;
        return false;
    }

    /** groupSum6
     * Given an array of ints, is it possible to choose a group of some of the ints, beginning at the start index, such
     * that the group sums to the given target? However, with the additional constraint that all 6's must be chosen. (No
     * loops needed.)
     */
    public boolean groupSum6(int start, int[] nums, int target) {
        if (start >= nums.length)
            return target == 0;
        if (nums[start] == 6)
            return groupSum6(start+1, nums, target-6);
        if (groupSum6(start+1, nums, target-nums[start]))
            return true;
        if (groupSum6(start+1, nums, target))
            return true;
        return false;
    }

    /** groupNoAdj
     * Given an array of ints, is it possible to choose a group of some of the ints, such that the group sums to the
     * given target with this additional constraint: If a value in the array is chosen to be in the group, the value
     * immediately following it in the array must not be chosen. (No loops needed.)
     */
    public boolean groupNoAdj(int start, int[] nums, int target) {
        if (start >= nums.length)
            return target == 0;
        if (groupNoAdj(start+2, nums, target-nums[start]))
            return true;
        if (groupNoAdj(start+1, nums, target))
            return true;
        return false;
    }

    /** groupSum5
     * Given an array of ints, is it possible to choose a group of some of the ints, such that the group sums to the
     * given target with these additional constraints: all multiples of 5 in the array must be included in the group. If
     * the value immediately following a multiple of 5 is 1, it must not be chosen. (No loops needed.)
     */
    public boolean groupSum5(int start, int[] nums, int target) {
        if (start >= nums.length)
            return target == 0;
        if (nums[start] % 5 == 0)
            if (start < nums.length - 1 && nums[start+1] != 1)
                return groupSum5(start+1, nums, target-nums[start]);
            else
                return groupSum5(start+2, nums, target-nums[start]);
        if (groupSum5(start+1, nums, target-nums[start]))
            return true;
        if (groupSum5(start+1, nums, target))
            return true;
        return false;
    }

    /** groupSumClump
     * Given an array of ints, is it possible to choose a group of some of the ints, such that the group sums to the
     * given target, with this additional constraint: if there are numbers in the array that are adjacent and the
     * identical value, they must either all be chosen, or none of them chosen. For example, with the array {1, 2, 2, 2,
     * 5, 2}, either all three 2's in the middle must be chosen or not, all as a group. (one loop can be used to find
     * the extent of the identical values).
     */
    public boolean groupSumClump(int start, int[] nums, int target) {
        if (start >= nums.length)
            return target == 0;
        int sum = nums[start];
        while (start < nums.length-1 && nums[start] == nums[start+1]) {
            sum += nums[start];
            start += 1;
        }
        if (groupSumClump(start+1, nums, target-sum))
            return true;
        else
            return groupSumClump(start+1, nums, target);
    }

    /** splitArray
     * Given an array of ints, is it possible to divide the ints into two groups, so that the sums of the two groups are
     * the same. Every int must be in one group or the other. Write a recursive helper method that takes whatever
     * arguments you like, and make the initial call to your recursive helper from splitArray(). (No loops needed.)
     */
    public boolean splitArray(int[] nums) {
        return splitArrayHelper(0, 0, 0, nums);
    }

    public boolean splitArrayHelper(int start, int lsum, int rsum, int[] nums) {
        if (start >= nums.length)
            return lsum == rsum && arrSum(nums) == lsum + rsum;
        if (splitArrayHelper(start + 1, lsum + nums[start], rsum, nums))
            return true;
        if (splitArrayHelper(start + 1, lsum, rsum + nums[start], nums))
            return true;
        return false;
    }

    public int arrSum(int[] nums) {
        int sum = 0;
        for (int i = 0; i < nums.length; i++) {
            sum += nums[i];
        }
        return sum;
    }

    /** splitOdd10
     * Given an array of ints, is it possible to divide the ints into two groups, so that the sum of one group is a
     * multiple of 10, and the sum of the other group is odd. Every int must be in one group or the other. Write a
     * recursive helper method that takes whatever arguments you like, and make the initial call to your recursive
     * helper from splitOdd10(). (No loops needed.)
     */
    public boolean splitOdd10(int[] nums) {
        return splitOdd10Helper(0, 0, 0, nums);
    }

    public boolean splitOdd10Helper(int start, int tenSum, int oddSum, int[] nums) {
        if (start >= nums.length)
            return tenSum % 10 == 0 && oddSum % 2 == 1 && arrSum(nums) == tenSum + oddSum;
        if (splitOdd10Helper(start + 1, tenSum + nums[start], oddSum, nums))
            return true;
        if (splitOdd10Helper(start + 1, tenSum, oddSum + nums[start], nums))
            return true;
        return false;
    }

    /** split53
     * Given an array of ints, is it possible to divide the ints into two groups, so that the sum of the two groups is
     * the same, with these constraints: all the values that are multiple of 5 must be in one group, and all the values
     * that are a multiple of 3 (and not a multiple of 5) must be in the other. (No loops needed.)
     */
    public boolean split53(int[] nums) {
        return split53Helper(0, 0, 0, nums);
    }

    public boolean split53Helper(int start, int fiveSum, int threeSum, int[] nums) {
        if (start >= nums.length)
            return threeSum == fiveSum && arrSum(nums) == threeSum + fiveSum;
        int add = nums[start] % 5 != 0 ? nums[start] : 0;
        if (split53Helper(start + 1, fiveSum, threeSum + add, nums))
            return true;
        add = nums[start] % 3 != 0 ? nums[start] : 0;
        if (split53Helper(start + 1, fiveSum + add, threeSum, nums))
            return true;
        return false;
    }
}