import java.util.List;

/**
 * https://codingbat.com/java/Functional-2
 * Functional filtering and mapping operations on lists with lambdas. The main computation for each of these problems
 * can be done with 1 or 2 lines of lambda code.
 */
public class Functional_2 {
    /** noNeg
     * Given a list of integers, return a list of the integers, omitting any that are less than 0.
     */
    public List<Integer> noNeg(List<Integer> nums) {
        nums.removeIf(n -> n < 0);
        return nums;
    }

    /** no9
     * Given a list of non-negative integers, return a list of those numbers except omitting any that end with 9.
     */
    public List<Integer> no9(List<Integer> nums) {
        nums.removeIf(n -> n % 10 == 9);
        return nums;
    }

    /** noTeen
     * Given a list of integers, return a list of those numbers, omitting any that are between 13 and 19 inclusive.
     */
    public List<Integer> noTeen(List<Integer> nums) {
        nums.removeIf(n -> n >= 13 && n <= 19);
        return nums;
    }

    /** noZ
     * Given a list of strings, return a list of the strings, omitting any string that contains a "z".
     */
    public List<String> noZ(List<String> strings) {
        strings.removeIf(s -> s.contains("z"));
        return strings;
    }

    /** noLong
     * Given a list of strings, return a list of the strings, omitting any string length 4 or more.
     */
    public List<String> noLong(List<String> strings) {
        strings.removeIf(s -> s.length() >= 4);
        return strings;
    }

    /** no34
     * Given a list of strings, return a list of the strings, omitting any string length 3 or 4.
     */
    public List<String> no34(List<String> strings) {
        strings.removeIf(s -> s.length() == 3 || s.length() == 4);
        return strings;
    }

    /** noYY
     * Given a list of strings, return a list where each string has "y" added at its end, omitting any resulting strings
     * that contain "yy" as a substring anywhere.
     */
    public List<String> noYY(List<String> strings) {
        strings.replaceAll(s -> s + "y");
        strings.removeIf(s -> s.contains("yy"));
        return strings;
    }

    /** two2
     * Given a list of non-negative integers, return a list of those numbers multiplied by 2, omitting any of the
     * resulting numbers that end in 2.
     */
    public List<Integer> two2(List<Integer> nums) {
        nums.replaceAll(n -> n * 2);
        nums.removeIf(n -> n % 10 == 2);
        return nums;
    }

    /** square56
     * Given a list of integers, return a list of those numbers squared and the product added to 10, omitting any of the
     * resulting numbers that end in 5 or 6.
     */
    public List<Integer> square56(List<Integer> nums) {
        nums.replaceAll(n -> (n*n)+10);
        nums.removeIf(n -> n % 10 == 5 || n % 10 == 6);
        return nums;
    }
}