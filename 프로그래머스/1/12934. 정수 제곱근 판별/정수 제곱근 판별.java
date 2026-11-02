class Solution {
    public long solution(long n) {
        long answer = (long) Math.sqrt(n);

        if (answer * answer == n) {
            long next = answer + 1;
            return next * next;
        } else {
            return -1;
        }
    }
}