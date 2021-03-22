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

    /**
     *
     */
}
