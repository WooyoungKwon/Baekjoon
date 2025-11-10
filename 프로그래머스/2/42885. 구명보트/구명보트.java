import java.util.*;

class Solution {
    public int solution(int[] people, int limit) {
        int answer = 0;
        
        Arrays.sort(people);
        int left = 0;
        int right = people.length - 1;
        
        while(left <= right) {
            if (left == right) {
                answer += 1;
                break;
            }
            if (people[left] + people[right] <= limit) {
                left++;
                right--;
            } else {
                right--;
            }
            answer += 1;
        }
        
        return answer;
    }
}