import java.util.*;

class Solution {
    public int solution(int k, int[] tangerine) {
        int answer = 0;
        List<List<Integer>> info = new ArrayList<>();
        Map<Integer, Integer> map = new HashMap<>();
        for(int i = 0; i < tangerine.length; i++) {
            map.put(tangerine[i], map.getOrDefault(tangerine[i], 0) + 1);
        }
        for(int key : map.keySet()) {
            info.add(List.of(key, map.get(key)));
        }
        info.sort((o1, o2) -> o2.get(1) - o1.get(1));
        
        int limit = 0;
        for(List<Integer> in : info) {
            limit += in.get(1);
            answer += 1;
            if (limit >= k) {
                break;
            }
        }
        return answer;
    }
}