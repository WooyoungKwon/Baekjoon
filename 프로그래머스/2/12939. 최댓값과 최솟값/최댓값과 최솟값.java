import java.util.*;
import java.util.stream.*;

class Solution {
    public String solution(String s) {
        String answer = "";
        String[] arr = s.split(" ");
        List<Integer> intArr = Arrays.stream(arr)
            .map(Integer::parseInt)
            .collect(Collectors.toList()); 
        int max = Collections.max(intArr);
        int min = Collections.min(intArr);
        
        return min + " " + max;
    }
}