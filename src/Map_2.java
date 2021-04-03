import java.util.Map;
import java.util.HashMap;

/**
 * https://codingbat.com/java/Map-2
 * Maps with bulk data and loops.
 */
public class Map_2 {
    /** word0
     * Given an array of strings, return a Map<String, Integer> containing a key for every different string in the
     * array, always with the value 0. For example the string "hello" makes the pair "hello":0. We'll do more
     * complicated counting later, but for this problem the value is simply 0.
     */
    public Map<String, Integer> word0(String[] strings) {
        Map<String, Integer> result = new HashMap<String, Integer>();
        for (String s : strings) {
            result.put(s, 0);
        }
        return result;
    }

    /** wordLen
     * Given an array of strings, return a Map<String, Integer> containing a key for every different string in the
     * array, and the value is that string's length.
     */
    public Map<String, Integer> wordLen(String[] strings) {
        Map<String, Integer> result = new HashMap<String, Integer>();
        for (String s : strings) {
            if (!result.containsKey(s))
                result.put(s, s.length());
        }
        return result;
    }

    /** pairs
     * Given an array of non-empty strings, create and return a Map<String, String> as follows: for each string add its
     * first character as a key with its last character as the value.
     */
    public Map<String, String> pairs(String[] strings) {
        Map<String, String> result = new HashMap<String, String>();
        for (String s : strings) {
            int l = s.length() - 1;
            result.put(s.substring(0, 1), s.substring(l));
        }
        return result;
    }

    /** wordCount
     * The classic word-count algorithm: given an array of strings, return a Map<String, Integer> with a key for each
     * different string, with the value the number of times that string appears in the array.
     */
    public Map<String, Integer> wordCount(String[] strings) {
        Map<String, Integer> result = new HashMap<String, Integer>();
        for (String s : strings) {
            if (result.containsKey(s))
                result.put(s, result.get(s) + 1);
            else
                result.put(s, 1);
        }
        return result;
    }

    /** firstChar
     * Given an array of non-empty strings, return a Map<String, String> with a key for every different first character
     * seen, with the value of all the strings starting with that character appended together in the order they appear
     * in the array.
     */
    public Map<String, String> firstChar(String[] strings) {
        Map<String, String> result = new HashMap<String, String>();
        for (String s : strings) {
            String k = s.substring(0, 1);
            if (result.containsKey(k))
                result.put(k, result.get(k) + s);
            else
                result.put(k, s);
        }
        return result;
    }

    /** wordAppend
     * Loop over the given array of strings to build a result string like this: when a string appears the 2nd, 4th, 6th,
     * etc. time in the array, append the string to the result. Return the empty string if no string appears a 2nd time.
     */
    public String wordAppend(String[] strings) {
        Map<String, Integer> map = new HashMap<String, Integer>();
        String result = "";
        for (String s : strings) {
            if (map.containsKey(s))
                map.put(s, map.get(s) + 1);
            else
                map.put(s, 1);
            if (map.get(s) % 2 == 0)
                result += s;
        }
        return result;
    }

    /** wordMultiple
     * Given an array of strings, return a Map<String, Boolean> where each different string is a key and its value is
     * true if that string appears 2 or more times in the array.
     */
    public Map<String, Boolean> wordMultiple(String[] strings) {
        Map<String, Boolean> result = new HashMap<String, Boolean>();
        for (String s : strings) {
            if (result.containsKey(s))
                result.put(s, true);
            else
                result.put(s, false);
        }
        return result;
    }

    /** allSwap
     * We'll say that 2 strings "match" if they are non-empty and their first chars are the same. Loop over and then
     * return the given array of non-empty strings as follows: if a string matches an earlier string in the array, swap
     * the 2 strings in the array. When a position in the array has been swapped, it no longer matches anything. Using a
     * map, this can be solved making just one pass over the array. More difficult than it looks.
     */
    public String[] allSwap(String[] strings) {
        Map<String, Integer> map = new HashMap<String, Integer>();
        for (int i = 0; i < strings.length; i++) {
            String key = strings[i].substring(0, 1);
            if (map.containsKey(key)) {
                String temp = strings[i];
                strings[i] = strings[map.get(key)];
                strings[map.get(key)] = temp;
                map.remove(key);
            } else
                map.put(key, i);
        }
        return strings;
    }

    /** firstSwap
     * We'll say that 2 strings "match" if they are non-empty and their first chars are the same. Loop over and then
     * return the given array of non-empty strings as follows: if a string matches an earlier string in the array, swap
     * the 2 strings in the array. A particular first char can only cause 1 swap, so once a char has caused a swap, its
     * later swaps are disabled. Using a map, this can be solved making just one pass over the array. More difficult
     * than it looks.
     */
    public String[] firstSwap(String[] strings) {
        Map<String, Integer> map = new HashMap<String, Integer>();
        for (int i = 0; i < strings.length; i++) {
            String key = strings[i].substring(0, 1);
            if (map.containsKey(key)) {
                if (map.get(key) != -1) {
                    String temp = strings[i];
                    strings[i] = strings[map.get(key)];
                    strings[map.get(key)] = temp;
                    map.put(key, -1);
                }
            } else
                map.put(key, i);
        }
        return strings;
    }
}