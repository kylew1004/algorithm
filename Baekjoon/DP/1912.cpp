// https://www.acmicpc.net/problem/1912

#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int n;
    cin >> n;
    int arr[n];
    for (int i = 0; i < n; i++) cin >> arr[i];
    int dp[n];
    dp[0] = arr[0];
    int max_sum = dp[0];
    for (int i = 1; i < n; i++) {
        dp[i] = max(dp[i - 1] + arr[i], arr[i]);
        max_sum = max(max_sum, dp[i]);
    }
    cout << max_sum << '\n';
    return 0;
}