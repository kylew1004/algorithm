// https://www.acmicpc.net/problem/2178

import java.util.*;
import java.io.*;

public class Main {
    static Scanner sc = new Scanner(System.in);
    static int n, m;
    static boolean[][] map;
    static boolean[] visited;
    static int count = 0;

    public static void main(String[] args) throws IOException {
        n = sc.nextInt();
        m = sc.nextInt();

        map = new boolean[n + 1][n + 1];
        visited = new boolean[n + 1];

        for(int i=0; i < m; i++) {
            int start = sc.nextInt();
            int end = sc.nextInt();
            map[start][end] = true;
            map[end][start] = true;
        }

        dfs(1);
        System.out.println(count);
    }

    public static void dfs(int start) {
        visited[start] = true;
        for(int i=1; i <= n; i++) {
            if(map[start][i] && !visited[i]) {
                count++;
                dfs(i);
            }
        }
    }
}