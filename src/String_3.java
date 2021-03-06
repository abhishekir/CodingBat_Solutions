/**
 * https://codingbat.com/java/String-3
 * Harder String problems
 *
 * Expected to be solved with 2 loops, but I solved all with 1 loop.
 */
public class String_3 {
    /** countYZ
     * Given a string, count the number of words ending in 'y' or 'z' -- so the 'y' in "heavy" and the 'z' in "fez"
     * count, but not the 'y' in "yellow" (not case sensitive). We'll say that a y or z is at the end of a word if there
     * is not an alphabetic letter immediately following it. (Note: Character.isLetter(char) tests if a char is an
     * alphabetic letter.)
     */
    public int countYZ(String str) {
        str = str.toLowerCase();

        String newstr = "";

        for (int i = 0; i < str.length(); i++) {
            if (Character.isLetter(str.charAt(i))) newstr += str.substring(i, i+1);
            else newstr += " ";
        }

        String[] arr = newstr.split(" ");
        int count = 0;

        for (String s : arr) {
            if (!s.isEmpty() && (s.substring(s.length()-1).equals("y")
                    || s.substring(s.length()-1).equals("z")))
                count++;
        }

        return count;
    }

    /** withoutString
     * Given two strings, base and remove, return a version of the base string where all instances of the remove string
     * have been removed (not case sensitive). You may assume that the remove string is length 1 or more. Remove only
     * non-overlapping instances, so with "xxx" removing "xx" leaves "x".
     */
    public String withoutString(String base, String remove) {
        String result = "";
        int baselen = base.length();
        int remlen = remove.length();
        int end = 0;

        if (remlen > baselen) return result;
        else if (base.equals(remove)) return result;

        for (int i = 0; i < baselen-remlen; i++) {
            if (base.substring(i, i+remlen).equalsIgnoreCase(remove)) {
                i+=remlen-1;
                end = i;
            } else {
                result += base.substring(i, i+1);
            }
        }

        if (baselen-(end+1) < remlen) {
            result += base.substring(end+1, baselen);
        }
        else if (!base.substring(baselen-remlen).equalsIgnoreCase(remove))
            result += base.substring(baselen-remlen);

        return result;
    }

    /** equalIsNot
     * Given a string, return true if the number of appearances of "is" anywhere in the string is equal to the number
     * of appearances of "not" anywhere in the string (case sensitive).
     */
    public boolean equalIsNot(String str) {
        int iscount = 0;
        int notcount = 0;
        for(int i = 0; i < str.length()-2; i++) {
            if (str.substring(i, i+2).equals("is")) iscount++;
        }
        for (int i = 0; i < str.length()-3; i++) {
            if (str.substring(i, i+3).equals("not")) notcount++;
        }
        if (str.length()>2 && str.substring(str.length()-3).equals("not")) notcount++;
        if (str.length()>1 && str.substring(str.length()-2).equals("is")) iscount++;
        return iscount == notcount;
    }

    /** gHappy
     * We'll say that a lowercase 'g' in a string is "happy" if there is another 'g' immediately to its left or right.
     * Return true if all the g's in the given string are happy.
     */
    public boolean gHappy(String str) {
        int strlen = str.length();
        boolean happy = true;

        if (strlen == 0) return happy;
        else if (strlen == 1) {
            if (str.equals("g")) return !happy;
            else return happy;
        }

        for (int i = 1; i < strlen-1; i++) {
            if (str.substring(i, i+1).equals("g")) {
                if (!(str.substring(i-1, i).equals("g") || str.substring(i+1, i+2).equals("g")))
                    happy = false;
            }
        }

        if (str.substring(strlen-1).equals("g")) {
            if (!str.substring(strlen-2, strlen-1).equals("g"))
                happy = false;
        }

        return happy;
    }

    /** countTriple
     * We'll say that a "triple" in a string is a char appearing three times in a row. Return the number of triples in
     * the given string. The triples may overlap.
     */
    public int countTriple(String str) {
        int tcount = 0;
        int strlen = str.length();

        if (strlen < 3) return tcount;
        String two_previous = str.substring(0, 1);
        String previous = str.substring(1, 2);

        for (int i = 2; i < strlen; i++) {
            String current = str.substring(i, i+1);
            if (current.equals(previous) && previous.equals(two_previous))
                tcount++;
            two_previous = previous;
            previous = current;
        }
        return tcount;
    }

    /** sumDigits
     * Given a string, return the sum of the digits 0-9 that appear in the string, ignoring all other characters.
     * Return 0 if there are no digits in the string. (Note: Character.isDigit(char) tests if a char is one of the
     * chars '0', '1', .. '9'. Integer.parseInt(string) converts a string to an int.)
     */
    public int sumDigits(String str) {
        int sum = 0;
        for (int i = 0; i < str.length(); i++) {
            if (Character.isDigit(str.charAt(i))) {
                sum += Integer.parseInt(str.substring(i, i+1));
            }
        }
        return sum;
    }

    /** sameEnds
     * Given a string, return the longest substring that appears at both the beginning and end of the string without
     * overlapping. For example, sameEnds("abXab") is "ab".
     */
    public String sameEnds(String str) {
        int len = str.length();
        if (len < 2) return "";

        int i = len/2;

        while(i >= 0 && !str.substring(0, i).equals(str.substring(len-i))) {
            i--;
        }
        return str.substring(0, i);
    }

    /** mirrorEnds
     * Given a string, look for a mirror image (backwards) string at both the beginning and end of the given string. In
     * other words, zero or more characters at the very begining of the given string, and at the very end of the string
     * in reverse order (possibly overlapping). For example, the string "abXYZba" has the mirror end "ab".
     */
    public String mirrorEnds(String str) {
        int len = str.length();
        String rev;

        if (len <= 1) return str;
        else {
            rev = str.substring(len-1);
        }

        int i = 0;
        while (i < len && str.substring(0, i+1).equals(rev)) {
            i++;
            if (i < len)
                rev += str.substring(len-i-1, len-i);
        }

        return str.substring(0, i);
    }

    /** maxBlock
     * Given a string, return the length of the largest "block" in the string. A block is a run of adjacent chars that
     * are the same.
     */
    public int maxBlock(String str) {
        int count = 0;
        int biggest_count = 0;
        int len = str.length();
        String previous;
        String current;

        if (len == 0) return count;
        else if (len == 1) return 1;
        else previous = str.substring(0, 1);

        for (int i = 1; i < len; i++) {
            current = str.substring(i, i+1);
            if (current.equals(previous)) {
                count++;
                if (biggest_count < count) biggest_count = count;
            }
            else
                count = 0;
            previous = current;
        }

        return biggest_count + 1;
    }

    /** sumNumbers
     * Given a string, return the sum of the numbers appearing in the string, ignoring all other characters. A number is
     * a series of 1 or more digit chars in a row.
     */
    public int sumNumbers(String str) {
        int sum = 0;
        int len = str.length();
        String num_str = "";
        int num;

        for (int i = 0; i < len; i++) {
            char c = str.charAt(i);
            boolean b = Character.isDigit(c);
            if (b) {
                num_str += c;
            }
            else if (!num_str.isEmpty()) {
                num = Integer.parseInt(num_str);
                num_str = "";
                sum += num;
            }
        }

        if (!num_str.isEmpty()) {
            num = Integer.parseInt(num_str);
            sum += num;
        }

        return sum;
    }

    /** notReplace
     * Given a string, return a string where every appearance of the lowercase word "is" has been replaced with "is
     * not". The word "is" should not be immediately preceeded or followed by a letter -- so for example the "is" in
     * "this" does not count.
     */
    public String notReplace(String str) {
        String result = "";
        int len = str.length();

        if (len < 2) return result;
        boolean last_char = false;

        for (int i = 0; i < len-1; i++) {
            if (i+2 == len) last_char = true;
            if (str.substring(i, i+2).equals("is")
                    && (i == 0 || !Character.isLetter(str.charAt(i-1)))
                    && (last_char || i+2 < len && !Character.isLetter(str.charAt(i+2)))) {
                result += "is not";
                i++;
                last_char = false;
            } else {
                result += str.substring(i, i+1);
            }
        }

        if (last_char) result += str.substring(len-1);

        return result;
    }
}