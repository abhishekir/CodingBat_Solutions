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
}
