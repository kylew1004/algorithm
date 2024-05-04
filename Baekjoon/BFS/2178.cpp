// https://www.acmicpc.net/problem/2178

#include <iostream>
#include <queue>
#include <tuple>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int N, M;
    cin >> N >> M;
    int maze[N][M];
    for (int i = 0; i < N; i++) {
        string row;
        cin >> row;
        for (int j = 0; j < M; j++) {
            maze[i][j] = row[j] - '0';
        }
    }

    int dx[] = {0, 0, -1, 1};
    int dy[] = {-1, 1, 0, 0};
    queue<tuple<int, int, int>> q;
    q.push({0, 0, 1});
    while (!q.empty()) {
        int x, y, z;
        tie(x, y, z) = q.front();
        q.pop();
        if (x == N - 1 && y == M - 1) {
            cout << z << '\n';
            break;
        }
        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];
            if (nx < 0 || nx >= N || ny < 0 || ny >= M) {
                continue;
            }
            if (maze[nx][ny] == 0) {
                continue;
            }
            maze[nx][ny] = 0;
            q.push({nx, ny, z + 1});
        }
    }

    return 0;
}