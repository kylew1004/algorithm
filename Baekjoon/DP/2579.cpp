// https://www.acmicpc.net/problem/2579

#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    int N;
    cin >> N;

    int arr[301] = {0, };
    int dp[301] = {0, };
    for (int i = 1; i <= N; i++) {
        cin >> arr[i];
    }

    dp[1] = arr[1];
    dp[2] = arr[1] + arr[2];
    for (int i = 3; i <= N; i++) {
        dp[i] = max(dp[i-2] + arr[i], dp[i-3] + arr[i-1] + arr[i]);
    }

    cout << dp[N] << '\n';
    return 0;
}