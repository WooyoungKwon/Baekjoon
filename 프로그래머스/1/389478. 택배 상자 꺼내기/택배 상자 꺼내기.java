class Solution {
    public int solution(int n, int w, int num) {
        int answer = 0;
        int[][] boxes = new int[101][101];
        int number = 1;
        int row = 0;
        int col = 0;
        for(int i = 0; i < n; i++) {
            boxes[row][col] = number;
            number++;
            if(row % 2 == 0) {
                if(col == w - 1) {
                    row++;
                } else {
                    col++;
                }
            }
            else if(row % 2 == 1) {
                if(col == 0) {
                    row++;
                } else {
                    col--;
                }
            }
        }
        for(int i = 0; i <= row; i++) {
            for(int j = 0; j < w; j++) {
                System.out.print(boxes[i][j] + " ");
                if(boxes[i][j] == num) {
                    // System.out.print(i + " " + j);
                    if(i == row) {
                        return 1;
                    }
                    answer = row - i;
                    return boxes[row][j] == 0 ? answer : answer + 1;
                }
            }
            System.out.println();
        }
        return 0;
    }
}