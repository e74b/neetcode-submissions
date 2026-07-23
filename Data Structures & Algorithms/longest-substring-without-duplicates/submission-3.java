class Solution {
    public int lengthOfLongestSubstring(String s) {
        int left = 0;
        int right = 0;
        int longestWindow = 0;

        for (; right < s.length(); right++) {
            String currentWindow = s.substring(left, right);
            char nextChar = s.charAt(right);

            int location = currentWindow.indexOf(nextChar);
            if (location > -1 ) {
                left += location + 1;
            } else {
                currentWindow = currentWindow + nextChar;
            }

            if (currentWindow.length() > longestWindow) {
                longestWindow = currentWindow.length();
            }
        }

        return longestWindow;
    }
}
