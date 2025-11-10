    import java.util.*;

    class Solution {
        public String solution(String number, int k) {
            String answer = "";
            Deque<Character> stack = new ArrayDeque<>();
            int removeCnt = 0;
            for(char c : number.toCharArray()) {
                while(!stack.isEmpty() && stack.peekLast() < c && removeCnt < k) {
                    stack.removeLast();
                    removeCnt++;
                }
                stack.addLast(c);
            }
            while(removeCnt < k) {
                stack.removeLast();
                removeCnt++;
            }
            for(Character c : stack) {
                answer += c;
            }
            return answer;
        }
    }
