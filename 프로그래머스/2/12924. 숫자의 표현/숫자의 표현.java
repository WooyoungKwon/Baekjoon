class Solution {
    public int solution(int n) {
        int answer = 0;
        int[] arr = new int[n];
        for(int i = 0; i < n; i++) {
            arr[i] = i + 1;
        }
        int left = 0;
        int right = 0;
        int currVal = 0;
        while (true) {
            if (currVal == n) {
                answer += 1;
            }
            if (right < n) {
                 if (currVal <= n) {
                    currVal += arr[right];
                    right += 1;
                } else if (currVal > n) {
                    currVal -= arr[left];
                    left += 1;
                }
            } else {
                currVal -= arr[left];
                left += 1;
            }
            if(left == n) {
                break;
            }
        }
        return answer;
    }
}