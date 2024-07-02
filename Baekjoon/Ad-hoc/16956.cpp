// https://www.acmicpc.net/problem/16956

#include <iostream>
#include <vector>
#include <queue>
#include <tuple>
using namespace std;

int main() {
    int R, C;
    cin >> R >> C;
    vector<string> board(R);
    for (int i = 0; i < R; i++) {
        cin >> board[i];
    }

    vector<pair<int, int>> sheep;
    for (int i = 0; i < R; i++) {
        for (int j = 0; j < C; j++) {
            if (board[i][j] == 'S') {
                sheep.push_back({i, j});
            }
        }
    }

    vector<pair<int, int>> wolf;
    for (int i = 0; i < R; i++) {
        for (int j = 0; j < C; j++) {
            if (board[i][j] == 'W') {
                wolf.push_back({i, j});
            }
        }
    }

    vector<pair<int, int>> dir = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
    for (auto [r, c] : sheep) {
        for (auto [dr, dc] : dir) {
            int nr = r + dr;
            int nc = c + dc;
            if (nr < 0 || nr >= R || nc < 0 || nc >= C) {
                continue;
            }
            if (board[nr][nc] == 'W') {
                cout << 0 << endl;
                return 0;
            }
            if (board[nr][nc] == '.') {
                board[nr][nc] = 'D';
            }
        }
    }

    cout << 1 << endl;
    for (int i = 0; i < R; i++) {
        cout << board[i] << endl;
    }

    return 0;
}