// https://www.acmicpc.net/problem/2178

import java.util.*;
import java.io.*;

public class Main {

    static int[][] graph;
    static boolean[][] visited;
    static int[] dx = {0, 0, -1, 1};
    static int[] dy = {1, -1, 0 ,0};

    static int answer = 0;

    static int n, m;
    static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) throws IOException {
        n = sc.nextInt();
        m = sc.nextInt();

        graph = new int[n][m];
        visited = new boolean[n][m];

        for(int i = 0; i < n; i++) {
            String str = sc.next();
            for(int j = 0; j < m; j++) {
                graph[i][j] = str.charAt(j) - '0';
            }
        }

        visited[0][0] = true;
        bfs(0, 0);
        System.out.println(graph[n-1][m-1]);
    }

    public static void bfs(int x, int y) {
        Queue<int[]> q = new LinkedList<>();
        q.add(new int[] {x, y});

        while(!q.isEmpty()) {
            int now[] = q.poll();
            int nx = now[0];
            int ny = now[1];

            for (int i = 0; i < 4; i++) {
                int nextX = nx + dx[i];
                int nextY = ny + dy[i];

                if(nextX < 0 || nextY < 0 || nextX >= n || nextY >= m) continue;
                if(visited[nextX][nextY] || graph[nextX][nextY] == 0) continue;

                q.add(new int[] {nextX, nextY});
                visited[nextX][nextY] = true;
                graph[nextX][nextY] = graph[nx][ny] + 1;
            }
        }
    }
}