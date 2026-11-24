class Solution {
    public int[] solution(int[] prices) {
        int [] answer = new int[prices.length];
        int [] stack = new int[prices.length];
        int top = -1;
        
        for (int i = 0; i < prices.length; i++) {
            while (top >= 0 && prices[stack[top]] > prices[i]) {
                int idx = stack[top--];
                answer[idx] = i - idx;
            }
            stack[++top] = i;
        }
        
        while (top >= 0) {
            int idx = stack[top--];
            answer[idx] = prices.length - 1 - idx;
        }
        return answer;
    }
}