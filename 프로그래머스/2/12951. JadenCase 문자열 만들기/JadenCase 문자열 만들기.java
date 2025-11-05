class Solution {
    public String solution(String s) {
        String answer = "";
        boolean wordStart = true;
        
        for(char c : s.toCharArray()) {
            if(c == ' ') {
                wordStart = true;
                answer += c;
            } else {
                if(wordStart) {
                    wordStart = false;
                    answer += Character.toUpperCase(c);
                } else {
                    answer += Character.toLowerCase(c);
                }
            }
        }
        
        return answer;
    }
}