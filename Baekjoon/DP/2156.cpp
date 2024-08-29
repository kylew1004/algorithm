// https://www.acmicpc.net/problem/2156

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int n;
    cin >> n;

    vector<int> wines(n);
    for (int i = 0; i < n; i++) {
        cin >> wines[i];
    }

    vector<vector<int>> dp(n, vector<int>(3, 0));
    dp[0][1] = wines[0];

    for (int i = 1; i < n; i++) {
        dp[i][0] = max({dp[i - 1][0], dp[i - 1][1], dp[i - 1][2]});
        dp[i][1] = dp[i - 1][0] + wines[i];
        dp[i][2] = dp[i - 1][1] + wines[i];
    }

    cout << max({dp[n - 1][0], dp[n - 1][1], dp[n - 1][2]}) << endl;

    return 0;
}