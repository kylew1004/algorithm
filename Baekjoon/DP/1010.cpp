// https://www.acmicpc.net/problem/1010

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int t;
    cin >> t;

    while (t--) {
        int n, m;
        cin >> n >> m;

        vector<vector<int>> dp(n + 1, vector<int>(m + 1, 0));
        for (int i = 1; i <= m; i++) {
            dp[1][i] = i;
        }

        for (int i = 2; i <= n; i++) {
            for (int j = i; j <= m; j++) {
                for (int k = j; k >= i; k--) {
                    dp[i][j] += dp[i - 1][k - 1];
                }
            }
        }

        cout << dp[n][m] << endl;
    }

    return 0;
}