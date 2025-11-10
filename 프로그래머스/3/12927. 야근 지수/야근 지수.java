import java.util.*;

class Solution {
    public long solution(int n, int[] works) {
        long answer = 0;
        
        if(Arrays.stream(works).sum() <= n) {
            return 0;
        }
        
        PriorityQueue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder());
        for(int work : works) {
            pq.offer(work);
        }
        
        for(int i = 0; i < n; i++) {
            pq.offer(pq.poll() - 1);
        }
        
        for(int v : pq) {
            answer += v * v;
        }
        
        return answer;
    }
}