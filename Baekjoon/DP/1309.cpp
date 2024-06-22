// https://www.acmicpc.net/problem/1309

#include <iostream>
using namespace std;

int main() {
    int N;
    cin >> N;

    int dp[100001][3] = {0, };
    dp[1][0] = 1;
    dp[1][1] = 1;
    dp[1][2] = 1;

    for (int i = 2; i <= N; i++) {
        dp[i][0] = (dp[i-1][0] + dp[i-1][1] + dp[i-1][2]) % 9901;
        dp[i][1] = (dp[i-1][0] + dp[i-1][2]) % 9901;
        dp[i][2] = (dp[i-1][0] + dp[i-1][1]) % 9901;
    }

    cout << (dp[N][0] + dp[N][1] + dp[N][2]) % 9901 << '\n';
    return 0;
}