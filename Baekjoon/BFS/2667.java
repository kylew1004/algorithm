// https://www.acmicpc.net/problem/2667

import java.util.*;
import java.io.*;

public class Main {
    static Scanner sc = new Scanner(System.in);
    static int n;
    static int[][] map;
    static int[][] visited;
    static int num = 0;
    static int[] dx = {0,0,-1,1};
    static int[] dy = {-1,1,0,0};

    public static void main(String[] args) throws IOException {
        n = sc.nextInt();
        map = new int[n][n];
        visited = new int[n][n];
        List<Integer> result = new ArrayList<>();

        for(int i=0; i<n; i++) {
            String str = sc.next();
            for(int j=0; j<n; j++) {
                map[i][j] = str.charAt(j) - '0';
                visited[i][j] = 0;
            }
        }

        for(int i=0; i<n; i++) {
            for(int j=0; j<n; j++) {
                if (map[i][j] == 0 || visited[i][j] > 0)
                    continue;
                result.add(bfs(i,j));
            }
        }
        Collections.sort(result);
        System.out.println(num);
        for(int i=0; i<num; i++) {
            System.out.println(result.get(i));
        }
    }

    public static int bfs(int a, int b) {
        Queue<int[]> queue = new LinkedList<>();
        queue.add(new int[]{a,b});
        int cnt = 0;
        ++num;
        visited[a][b] = num;

        while(!queue.isEmpty()) {
            int[] tmp = queue.poll();
            int x = tmp[0];
            int y = tmp[1];

            for(int i=0; i<4; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];

                if(nx < 0 || nx >= n || ny < 0 || ny >= n) continue;
                if(map[nx][ny] == 0 || visited[nx][ny] > 0) continue;

                visited[nx][ny] = num;
                queue.add(new int[]{nx,ny});
            }
            cnt++;
        }
        return cnt;
    }
}