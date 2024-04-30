// https://www.acmicpc.net/problem/9095

#include <iostream>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int T;
    cin >> T;
    int dp[11] = {0, 1, 2, 4};
    for (int i = 4; i < 11; i++) {
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3];
    }
    for (int i = 0; i < T; i++) {
        int n;
        cin >> n;
        cout << dp[n] << '\n';
    }

    return 0;
}