class Solution {
    public int solution(int[] schedules, int[][] timelogs, int startday) {
        int answer = 0;
        // 0->일, 1->월, 2->화, 3->수, 4->목, 5->금, 6->토
        for(int i = 0; i < schedules.length; i++) {
            boolean flag = false;
            int fixHour = schedules[i] / 100;
            int fixMinute = (schedules[i] % 100) + 10;
            if (fixMinute >= 60) {
                fixMinute = fixMinute % 60;
                fixHour += 1;
            }
            for(int j = 0; j < 7; j++) {
                int day = (j + startday) % 7;
                if (day == 6 || day == 0) {
                    continue;
                }
                int hour = timelogs[i][j] / 100;
                int minute = timelogs[i][j] % 100;
                if (hour > fixHour) {
                    flag = true;
                } else if (hour == fixHour && minute > fixMinute) {
                    System.out.println(fixMinute);
                    System.out.println("pre= " + hour + " " + minute);
                    flag = true;
                }
            }
            if(flag == false) {
                System.out.println(i);
                answer += 1;
            }
        }
        return answer;
    }
}