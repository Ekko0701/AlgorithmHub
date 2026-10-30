class Solution {
    public long solution(long n) {
        int[] count = new int[10];
        while (n > 0) {
            count[(int) (n % 10)]++;
            n /= 10;
        }
        long answer = 0;
        for (int d = 9; d >= 0; d--) {
            while (count[d]-- > 0) answer = answer * 10 + d;
        }
        return answer;
    }
}