// https://www.acmicpc.net/problem/10870

#include <iostream>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int n;
    cin >> n;
    int dp[21] = {0, 1};
    for (int i = 2; i < 21; i++) {
        dp[i] = dp[i - 1] + dp[i - 2];
    }
    cout << dp[n] << '\n';

    return 0;
}