import java.util.*;

class Solution
{
    public int solution(String s)
    {
        int answer = 0;
        
        Deque<Character> q = new ArrayDeque<>();
        
        for (char c : s.toCharArray()) {
            if(q.isEmpty()) {
                q.add(c);
            } else {
                if(q.peek() == c) {
                    q.pop();
                } else {
                    q.push(c);
                }
            }
        }
        
        if(q.isEmpty()) {
            answer = 1;
        }
        
        return answer;
    }
}