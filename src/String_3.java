/**
 * codingbat.com/java/String-3
 * Harder String problems
 */
public class String_3 {
    /** countYZ
     * Given a string, count the number of words ending in 'y' or 'z' -- so the 'y' in "heavy" and the 'z' in "fez"
     * count, but not the 'y' in "yellow" (not case sensitive). We'll say that a y or z is at the end of a word if there
     * is not an alphabetic letter immediately following it. (Note: Character.isLetter(char) tests if a char is an
     * alphabetic letter.)
    **/
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
}
