import java.util.*;

public class Solution {
    public int solution(int n) {
        int answer = 0;
        char[] char_numbers = String.valueOf(n).toCharArray();
        int[] int_numbers = new int[char_numbers.length];
        
        for (int i = 0 ; i < int_numbers.length ; i++) { 
            int_numbers[i] = Integer.parseInt(String.valueOf(char_numbers[i]));
        }
        
        for (int i: int_numbers) { 
            answer += i;
        }

        return answer;
    }
}