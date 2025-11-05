import java.util.*;

class Solution {
    static void print(Object obj) {
        System.out.println(obj);
    }
    public int solution(int[] players, int m, int k) {
        int answer = 0;
        Deque<Integer> q = new ArrayDeque<>();
    
        for(int player : players) {
            int serverCover = (q.size() + 1) * m;
            if(serverCover <= player) {
                int addServer = (player - serverCover) / m + 1;
                answer += addServer;
                for(int i = 0; i < addServer; i++) {
                    q.addLast(k);
                }
            }
            int qSize = q.size();
            for(int i = 0; i < qSize; i++) {
                int restTime = q.poll() - 1;
                if (restTime != 0) {
                    q.addLast(restTime);
                }
            }
            print(player + " " + answer);
        }
        return answer;
    }
}