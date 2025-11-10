import java.util.*;

class Solution {
    public String[] solution(String[] files) {
        String[] answer = new String[files.length];
        List<List<String>> info = new ArrayList<>();
        for(String file : files) {
            String head = "";
            String number = "";
            String tail = "";
            int choose = 1;
            for(char c : file.toCharArray()) {
                if (choose == 1) {
                    if (Character.isDigit(c)) {
                        choose = 2;
                        number += c;
                    } else {
                        head += c;
                    }
                } else if (choose == 2) {
                    if (Character.isDigit(c)) {
                        number += c;
                    } else {
                        choose = 3;
                        tail += c;
                    }
                } else {
                    tail += c;
                }
            }
            info.add(List.of(head, number, tail));
        }
        info.sort((o1, o2) -> {
            // 1. HEAD 비교 (대소문자 무시)
            String head1 = o1.get(0).toLowerCase();
            String head2 = o2.get(0).toLowerCase();
            int headCompare = head1.compareTo(head2);

            if (headCompare != 0) {
                return headCompare;
            }

            // 2. NUMBER 비교 (숫자로 변환)
            int num1 = Integer.parseInt(o1.get(1));
            int num2 = Integer.parseInt(o2.get(1));
            return num1 - num2;
        });
        
        for(int i = 0; i < files.length; i++) {
            String tmp = "";
            for(String in : info.get(i)) {
                tmp += in;
            }
            answer[i] = tmp;
        }
            
        return answer;
    }
}