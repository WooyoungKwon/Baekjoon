import java.util.*;

class Solution {
    public int solution(int bridge_length, int weight, int[] truck_weights) {
        int answer = 0;
        Deque<Integer> past = new ArrayDeque<>();
        Deque<Integer> ing = new ArrayDeque<>();
        for(int i = 0; i < bridge_length; i++) {
            ing.addLast(0);
        }
        
        int number = 0;
        int currWeight = 0;
        while(past.size() != truck_weights.length) {
            int po = ing.poll();
            if (po != 0) {
                currWeight -= po;
                past.add(po);
            }
            
            if (number < truck_weights.length && 
                currWeight + truck_weights[number] <= weight) {
                currWeight += truck_weights[number];
                ing.addLast(truck_weights[number]);
                number++;
            } else {
                ing.addLast(0);
            }
            answer += 1;
        }
        
        return answer;
    }
}