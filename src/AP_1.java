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

    
}
