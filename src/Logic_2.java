/**
 * https://codingbat.com/java/Logic-2
 * Medium boolean logic puzzles -- if else && || !
 */
public class Logic_2 {
    /** makeBricks
     * We want to make a row of bricks that is goal inches long. We have a number of small bricks (1 inch each) and big
     * bricks (5 inches each). Return true if it is possible to make the goal by choosing from the given bricks. This is
     * a little harder than it looks and can be done without any loops.
     */
    public boolean makeBricks(int small, int big, int goal) {
        if (big == 0) {
            if (goal > small) return false;
            else return true;
        }
        else if (goal > (big*5 + small)) return false;

        else if (goal % 5 > small) return false;

        else return true;
    }

    /** loneSum
     * Given 3 int values, a b c, return their sum. However, if one of the values is the same as another of the values,
     * it does not count towards the sum.
     */
    public int loneSum(int a, int b, int c) {
        int sum = 0;
        if (a != b && a != c) sum += a;
        if (b != a && b != c) sum += b;
        if (c != a && c != b) sum += c;
        return sum;
    }

    /** luckySum
     * Given 3 int values, a b c, return their sum. However, if one of the values is 13 then it does not count towards
     * the sum and values to its right do not count. So for example, if b is 13, then both b and c do not count.
     */
    public int luckySum(int a, int b, int c) {
        if (a == 13) return 0;
        else if (b == 13) return a;
        else if (c == 13) return a + b;
        else return a + b + c;
    }

    /** noTeenSum
     * Given 3 int values, a b c, return their sum. However, if any of the values is a teen -- in the range 13..19
     * inclusive -- then that value counts as 0, except 15 and 16 do not count as a teens. Write a separate helper
     * "public int fixTeen(int n) {"that takes in an int value and returns that value fixed for the teen rule. In this
     * way, you avoid repeating the teen code 3 times (i.e. "decomposition"). Define the helper below and at the same
     * indent level as the main noTeenSum().
     */
    public int noTeenSum(int a, int b, int c) {
        return fixTeen(a) + fixTeen(b) + fixTeen(c);
    }

    public int fixTeen(int n) {
        return n >= 13 && n <= 19 && n != 15 && n != 16 ? 0 : n;
    }

    /** roundSum
     * For this problem, we'll round an int value up to the next multiple of 10 if its rightmost digit is 5 or more, so
     * 15 rounds up to 20. Alternately, round down to the previous multiple of 10 if its rightmost digit is less than 5,
     * so 12 rounds down to 10. Given 3 ints, a b c, return the sum of their rounded values. To avoid code repetition,
     * write a separate helper "public int round10(int num) {" and call it 3 times. Write the helper entirely below and
     * at the same indent level as roundSum().
     */
    public int roundSum(int a, int b, int c) {
        return round10(a) + round10(b) + round10(c);
    }

    public int round10(int n) {
        int ones = n % 10;
        int tens = n / 10;
        return ones < 5 ? tens * 10 : (tens + 1) * 10;
    }

    /** closeFar
     * Given three ints, a b c, return true if one of b or c is "close" (differing from a by at most 1), while the other
     * is "far", differing from both other values by 2 or more. Note: Math.abs(num) computes the absolute value of a
     * number.
     */
    public boolean closeFar(int a, int b, int c) {
        return (Math.abs(b-a) <= 1 ^ Math.abs(c-a) <= 1)
                && ((Math.abs(b-a) > 1 && Math.abs(b-c) > 1)
                ^ (Math.abs(c-a) > 1 && Math.abs(c-b) > 1));
    }

    /** blackjack
     * Given 2 int values greater than 0, return whichever value is nearest to 21 without going over. Return 0 if they
     * both go over.
     */
    public int blackjack(int a, int b) {
        if (a <= 21) {
            if (b <= 21) return Math.abs(a-21) <= Math.abs(b-21) ? a : b;
            else return a;
        }
        else if (b <= 21) return b;
        else return 0;
    }

    /** evenlySpaced
     * Given three ints, a b c, one of them is small, one is medium and one is large. Return true if the
     * three values are evenly spaced, so the difference between small and medium is the same as the difference between
     * medium and large.
     */
    public boolean evenlySpaced(int a, int b, int c) {
        return a == b && a == c
                || Math.abs(a-b) == Math.abs(b-c) && a != c
                || Math.abs(a-b) == Math.abs(a-c) && b != c
                || Math.abs(c-b) == Math.abs(c-a) && a != b;
    }

    /** makeChocolate
     * We want make a package of goal kilos of chocolate. We have small bars (1 kilo each) and big bars (5 kilos each).
     * Return the number of small bars to use, assuming we always use big bars before small bars. Return -1 if it can't
     * be done.
     */
    public int makeChocolate(int small, int big, int goal) {
        int big_needed = goal / 5;

        if (big_needed > big) goal -= big*5;
        else goal -= big_needed*5;


        return goal > small ? -1 : small-(small-goal);
    }
}
