/**
 * https://codingbat.com/java/String-2
 * Medium String problems -- 1 loop.
 */
public class String_2 {
    /** doubleChar
     * Given a string, return a string where for every char in the original, there are two chars.
     */
    public String doubleChar(String str) {
        String result = "";
        for (int i = 0; i < str.length(); i++) {
            result += str.charAt(i);
            result += str.charAt(i);
        }
        return result;
    }

    /** countHi
     * Return the number of times that the string "hi" appears anywhere in the given string.
     */
    public int countHi(String str) {
        int count = 0;
        for (int i = 0; i < str.length() - 1; i++) {
            if (str.substring(i, i+2).equals("hi")) count++;
        }
        return count;
    }

    /** catDog
     * Return true if the string "cat" and "dog" appear the same number of times in the given string.
     */
    public boolean catDog(String str) {
        int cat_count = 0;
        int dog_count = 0;
        for (int i = 0; i < str.length()-2; i++) {
            String temp = str.substring(i, i+3);
            if (temp.equals("cat")) cat_count++;
            else if (temp.equals("dog")) dog_count++;
        }
        return cat_count == dog_count;
    }

    /** countCode
     * Return the number of times that the string "code" appears anywhere in the given string, except we'll accept any
     * letter for the 'd', so "cope" and "cooe" count.
     */
    public int countCode(String str) {
        int count = 0;
        for (int i = 0; i < str.length()-3; i++) {
            boolean match = str.substring(i, i+2).equals("co") && str.substring(i+3, i+4).equals("e");
            if (match) count++;
        }
        return count;
    }

    /** endOther
     * Given two strings, return true if either of the strings appears at the very end of the other string, ignoring
     * upper/lower case differences (in other words, the computation should not be "case sensitive").
     */
    public boolean endOther(String a, String b) {
        a = a.toLowerCase();
        b = b.toLowerCase();
        boolean a_smaller = a.length() <= b.length();
        if (a_smaller) {
            int start = b.length() - a.length();
            return b.substring(start, b.length()).equals(a);
        } else {
            int start = a.length() - b.length();
            return a.substring(start, a.length()).equals(b);
        }
    }

    /** xyzThere
     * Return true if the given string contains an appearance of "xyz" where the xyz is not directly preceeded by a
     * period (.). So "xxyz" counts but "x.xyz" does not.
     */
    public boolean xyzThere(String str) {
        boolean result = false;
        if (str.length() >= 3) {
            if (str.substring(0, 3).equals("xyz")) return true;
        }
        for (int i = 0; i < str.length()-3; i++) {
            if (!str.substring(i, i+1).equals(".") && str.substring(i+1, i+4).equals("xyz")) {
                result = true;
                continue;
            }
        }
        return result;
    }

    /** bobThere
     * Return true if the given string contains a "bob" string, but where the middle 'o' char can be any char.
     */
    public boolean bobThere(String str) {
        for (int i = 0; i < str.length()-2; i++) {
            if (str.substring(i, i+1).equals("b") && str.substring(i+2, i+3).equals("b")) {
                return true;
            }
        }
        return false;
    }

    /** xyBalance
     * We'll say that a String is xy-balanced if for all the 'x' chars in the string, there exists a 'y' char somewhere
     * later in the string. So "xxy" is balanced, but "xyx" is not. One 'y' can balance multiple 'x's. Return true if
     * the given string is xy-balanced.
     */
    public boolean xyBalance(String str) {
        boolean balanced = true;
        for (int i = 0; i < str.length(); i++) {
            if (str.substring(i, i+1).equals("x")) balanced = false;
            else if (!balanced && str.substring(i, i+1).equals("y")) balanced = true;
        }
        return balanced;
    }

    /** mixString
     * Given two strings, a and b, create a bigger string made of the first char of a, the first char of b, the second
     * char of a, the second char of b, and so on. Any leftover chars go at the end of the result.
     */
    public String mixString(String a, String b) {
        String result = "";
        int count = 0;
        while(count < a.length() && count < b.length()) {
            result += a.substring(count, count+1);
            result += b.substring(count, count+1);
            count++;
        }

        if (count == a.length()) result += b.substring(count, b.length());
        else result += a.substring(count, a.length());
        return result;
    }

    /** repeatEnd
     * Given a string and an int n, return a string made of n repetitions of the last n characters of the string. You
     * may assume that n is between 0 and the length of the string, inclusive.
     */
    public String repeatEnd(String str, int n) {
        String result = "";
        String sub = str.substring(str.length()-n);
        for (int i = 0; i < n; i++) {
            result += sub;
        }
        return result;
    }

    /** repeatFront
     * Given a string and an int n, return a string made of the first n characters of the string, followed by the first
     * n-1 characters of the string, and so on. You may assume that n is between 0 and the length of the string,
     * inclusive (i.e. n >= 0 and n <= str.length()).
     */
    public String repeatFront(String str, int n) {
        String result = "";
        while (n > 0) {
            result += str.substring(0, n);
            n--;
        }
        return result;
    }

    /** repeatSeparator
     * Given two strings, word and a separator sep, return a big string made of count occurrences of the word, separated
     * by the separator string.
     */
    public String repeatSeparator(String word, String sep, int count) {
        if (count == 0) return "";
        String result = word;
        for (int i = 0; i < count-1; i++) {
            result += sep;
            result += word;
        }
        return result;
    }

    /** prefixAgain
     * Given a string, consider the prefix string made of the first N chars of the string. Does that prefix string
     * appear somewhere else in the string? Assume that the string is not empty and that N is in the range
     * 1..str.length().
     */
    public boolean prefixAgain(String str, int n) {
        String pref = str.substring(0, n);
        if (str.length() == 2 && str.substring(0, 1).equals(str.substring(1))) return true;
        for (int i = n; i < str.length()-n; i++) {
            if (str.substring(i, i+n).equals(pref)) return true;
        }
        return false;
    }

    /** xyzMiddle
     * Given a string, does "xyz" appear in the middle of the string? To define middle, we'll say that the number of
     * chars to the left and right of the "xyz" must differ by at most one. This problem is harder than it looks.
     */
    public boolean xyzMiddle(String str) {
        if (str.length() < 3) return false;

        int mid = str.length() / 2;
        boolean even = str.length() % 2 == 0;

        if (even) {
            return str.substring(mid-2, mid+1).equals("xyz")
                    || str.substring(mid-1, mid+2).equals("xyz");
        } else {
            return str.substring(mid-1, mid+2).equals("xyz");
        }
    }

    /** getSandwich
     * A sandwich is two pieces of bread with something in between. Return the string that is between the first and last
     * appearance of "bread" in the given string, or return the empty string "" if there are not two pieces of bread.
     */
    public String getSandwich(String str) {
        if (str.length() < 10) return "";
        boolean first_bread = false;
        int end_first_bread = 0;
        int start_second_bread = 0;
        for (int i = 0; i < str.length()-4; i++) {
            if (str.substring(i, i+5).equals("bread")) {
                if (!first_bread) {
                    end_first_bread = i+5;
                    first_bread = true;
                }
                else {
                    start_second_bread = i;
                }
            }
        }
        return str.substring(end_first_bread, start_second_bread);
    }

    /** sameStarChar
     * Returns true if for every '*' (star) in the string, if there are chars both immediately before and after the
     * star, they are the same.
     */
    public boolean sameStarChar(String str) {
        boolean match = true;
        for (int i = 1; i < str.length()-1; i++) {
            if (str.substring(i, i+1).equals("*")) {
                match = str.substring(i-1, i).equals(str.substring(i+1, i+2));
            }
        }
        return match;
    }

    /** oneTwo
     * Given a string, compute a new string by moving the first char to come after the next two chars, so "abc" yields
     * "bca". Repeat this process for each subsequent group of 3 chars, so "abcdef" yields "bcaefd". Ignore any group of
     * fewer than 3 chars at the end.
     */
    public String oneTwo(String str) {
        if (str.length() < 3) return "";
        String result = "";
        for (int i = 0; i < str.length()-2; i+=3) {
            result += str.substring(i+1, i+3);
            result += str.substring(i, i+1);
        }
        return result;
    }

    /** zipZap
     * Look for patterns like "zip" and "zap" in the string -- length-3, starting with 'z' and ending with 'p'. Return
     * a string where for all such words, the middle letter is gone, so "zipXzap" yields "zpXzp".
     */
    public String zipZap(String str) {
        if (str.length() < 3) return str;
        String result = "";

        for (int i = 0; i < str.length()-2; i++) {
            String first = str.substring(i, i+1);
            String third = str.substring(i+2, i+3);
            if (first.equals("z") && third.equals("p")) {
                result += first + third;
                i+=2;
            } else {
                result += first;
            }
        }
        String first = str.substring(str.length()-3, str.length()-2);
        String third = str.substring(str.length()-1);
        if (!(first.equals("z") && third.equals("p"))) result += str.substring(str.length()-2);

        return result;
    }

    /** starOut
     * Return a version of the given string, where for every star (*) in the string the star and the chars immediately
     * to its left and right are gone. So "ab*cd" yields "ad" and "ab**cd" also yields "ad".
     */
    public String starOut(String str) {
        String result = "";
        String two_previous = "";
        String previous = "";
        String current;

        if (str.length() == 0) return result;

        for (int i = 0; i < str.length(); i++) {
            current = str.substring(i, i+1);
            if (two_previous.equals("*")) {}
            else if (previous.equals("*")) {
            }
            else if (current.equals("*")) {
            }
            else {
                result += previous;
            }
            two_previous = previous;
            previous = current;

        }

        current = str.substring(str.length()-1);
        previous = two_previous;
        if (!previous.equals("*") && !current.equals("*")) {
            result += current;
        }

        return result;
    }

    /** plusOut
     * Given a string and a non-empty word string, return a version of the original String where all chars have been
     * replaced by pluses ("+"), except for appearances of the word string which are preserved unchanged.
     */
    public String plusOut(String str, String word) {
        String result = "";
        int i = 0;
        int last_word_idx = 0;
        while (i < str.length() - word.length()) {
            if (str.substring(i, i+word.length()).equals(word)) {
                result += word;
                i += word.length();
                last_word_idx = i-1;
            }
            else {
                result += "+";
                i++;
            }
        }
        if (str.substring(str.length()-word.length()).equals(word)) {
            result += word;
        } else {
            int rem = str.length() - result.length();
            for (int j = 0; j < rem; j++) {
                result += "+";
            }
        }

        return result;
    }

    /** wordEnds
     * Given a string and a non-empty word string, return a string made of each char just before and just after every
     * appearance of the word in the string. Ignore cases where there is no char before or after the word, and a char
     * may be included twice if it is between two words.
     */
    public String wordEnds(String str, String word) {
        String result = "";

        int strlen = str.length();
        int wrdlen = word.length();

        if (strlen <= wrdlen) return result;

        String before = "";
        String after = "";

        for (int i = 0; i < strlen-wrdlen; i++) {
            if (i+wrdlen < strlen) after = str.substring(i+wrdlen, i+wrdlen+1);
            else after = "";
            if (i > 0 && i < strlen) before = str.substring(i-1, i);
            else before = "";

            if (str.substring(i, i+wrdlen).equals(word)) {
                result += before;
                result += after;
                i += wrdlen-1;
            }
        }

        if (str.substring(strlen-wrdlen).equals(word)) {
            before = str.substring(strlen-wrdlen-1, strlen-wrdlen);
            result += before;
        }

        return result;
    }
}