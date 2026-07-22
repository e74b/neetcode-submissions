class Solution {
    public int[] getConcatenation(int[] nums) {
        int length = nums.length;
        int[] newArr = new int[length * 2];

        for (int i = 0, j = length; i < length; i++, j++) {
            newArr[i] = nums[i];
            newArr[j] = nums[i];
        }

        return newArr;
    }
}