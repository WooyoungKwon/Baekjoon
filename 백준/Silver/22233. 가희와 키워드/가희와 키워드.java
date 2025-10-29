import java.util.*;
import java.lang.*;
import java.io.*;

// The main method must be in a class named "Main".
class Main {
    public static void main(String[] args) throws Exception {
        // 2. BufferedReader 생성
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        Map<String, Integer> memo = new HashMap<>();
        for(int i = 0; i < N; i++) {
            String keyword = br.readLine();
            memo.put(keyword, memo.getOrDefault(keyword, 0) + 1);
        }
        int answer = N;
        for(int i = 0; i < M; i++) {
            String[] keywords = br.readLine().split(",");
            for(String keyword : keywords) {
                if (memo.containsKey(keyword)) {
                    if(memo.get(keyword) == 1) {
                        memo.put(keyword, 0);
                        answer -= 1;
                    }
                }
            }
            bw.write(String.valueOf(answer + "\n"));
        }
        bw.close();
    }
}