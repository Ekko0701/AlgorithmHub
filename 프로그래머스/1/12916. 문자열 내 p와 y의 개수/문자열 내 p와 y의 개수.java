class Solution {
    boolean solution(String s) {
        boolean answer = true;
        int p = 0;
        int y = 0;
        // [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
        System.out.println("Hello Java");
        
        for(int i = 0; i < s.length(); i++) { 
            char x = s.charAt(i);
            if (x == 'p' || x == 'P') { 
                p++;
            } else if (x == 'y' || x == 'Y') { 
                y++;
            }
            
            if (p == y) {
                answer = true;
            } else { 
                answer = false;
            }
        }
        
        return answer;
    }
}