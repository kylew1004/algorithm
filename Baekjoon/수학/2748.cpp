// https://www.acmicpc.net/problem/2748

#include <iostream>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int n;
    cin >> n;
    long long dp[91] = {0, 1};
    for (int i = 2; i < 91; i++) {
        dp[i] = dp[i - 1] + dp[i - 2];
    }
    cout << dp[n] << '\n';

    return 0;
}