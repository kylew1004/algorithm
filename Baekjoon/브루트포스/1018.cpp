// https://www.acmicpc.net/problem/1018

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int n, m;
    cin >> n >> m;
    vector<string> board(n);
    for (int i = 0; i < n; i++) {
        cin >> board[i];
    }

    int ans = 64;
    for (int i = 0; i < n - 7; i++) {
        for (int j = 0; j < m - 7; j++) {
            int cnt = 0;
            for (int k = i; k < i + 8; k++) {
                for (int l = j; l < j + 8; l++) {
                    if ((k + l) % 2 == 0) {
                        if (board[k][l] != 'W') {
                            cnt += 1;
                        }
                    } else {
                        if (board[k][l] != 'B') {
                            cnt += 1;
                        }
                    }
                }
            }
            ans = min(ans, cnt);
            ans = min(ans, 64 - cnt);
        }
    }

    cout << ans << '\n';

    return 0;
}