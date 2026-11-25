import java.util.Arrays;

class Solution {
    public int[] solution(int n, String[] words) {
        int[] answer = new int[2];
        
        int number = 0;
        int turn = 0;
        
        String[] past_words = new String[words.length];
        past_words[0] = words[0];
        
        for(int index = 1; index < words.length; index ++) { 
            // 이전 단어의 마지막 문자
            char last_char = words[index - 1].charAt(words[index - 1].length() - 1);
            // 현재 단어의 첫번째 문자
            char first_char = words[index].charAt(0);
            
            if(Arrays.asList(past_words).contains(words[index])) { 
                turn = index % n + 1;
                number = index / n + 1;
                break;
            } else if (first_char != last_char) { 
                turn = index % n + 1;
                number = index / n + 1;
                break;
            }
            
            past_words[index] = words[index];
        }
    
        answer[0] = turn;
        answer[1] = number;
        
        return answer;
    }
}