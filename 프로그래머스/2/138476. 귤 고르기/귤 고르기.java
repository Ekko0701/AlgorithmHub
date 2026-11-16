import java.util.*;

class Solution {
    public int solution(int k, int[] tangerine) {
        int answer = 0;
        
        Map<Integer, Integer> dictionary = new HashMap<>();
        
        for(int i = 0; i < tangerine.length; i++) {
            dictionary.merge(tangerine[i], 1, Integer::sum);
        }
        
        Integer[] count_list = dictionary.values().toArray(new Integer[0]);
        
        Arrays.sort(count_list, Collections.reverseOrder());
        
        for(int i = 0; i < count_list.length; i++) { 
            k -= count_list[i];
            answer += 1;
            if (k <= 0) { 
                break;
            }
        }
        return answer;
    }
}