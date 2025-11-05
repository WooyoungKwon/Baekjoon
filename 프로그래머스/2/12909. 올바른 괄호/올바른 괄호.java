import java.util.*;
import java.util.stream.*;

class Solution {
    boolean solution(String s) {
        boolean answer = true;
        
        Deque<Character> stack = new ArrayDeque<>();
        
        for (char c : s.toCharArray()) {
            if (c == '(') {
                stack.push(c);
            } else {
                if (stack.size() <= 0) {
                    return false;
                }
                stack.pop();
            }
        }
        return stack.size() == 0 ? true : false;
    }
}