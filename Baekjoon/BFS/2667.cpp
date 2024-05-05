// https://www.acmicpc.net/problem/2667

#include <iostream>
#include <queue>
#include <vector>
#include <algorithm>
using namespace std;

int N;
int map[25][25];
bool visited[25][25];
int dx[] = {0, 0, -1, 1};
int dy[] = {-1, 1, 0, 0};

int bfs(int x, int y) {
    queue<pair<int, int>> q;
    q.push({x, y});
    visited[x][y] = true;
    int cnt = 1;
    while (!q.empty()) {
        int x = q.front().first;
        int y = q.front().second;
        q.pop();
        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];
            if (nx < 0 || nx >= N || ny < 0 || ny >= N) {
                continue;
            }
            if (map[nx][ny] == 0 || visited[nx][ny]) {
                continue;
            }
            q.push({nx, ny});
            visited[nx][ny] = true;
            cnt++;
        }
    }
    return cnt;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> N;
    for (int i = 0; i < N; i++) {
        string row;
        cin >> row;
        for (int j = 0; j < N; j++) {
            map[i][j] = row[j] - '0';
        }
    }

    vector<int> v;
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            if (map[i][j] == 1 && !visited[i][j]) {
                v.push_back(bfs(i, j));
            }
        }
    }
    sort(v.begin(), v.end());

    cout << v.size() << '\n';
    for (int i = 0; i < v.size(); i++) {
        cout << v[i] << '\n';
    }

    return 0;
}