// https://www.acmicpc.net/problem/11047

#include <iostream>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int N, K;
    cin >> N >> K;

    int coins[10];
    for (int i = 0; i < N; i++) {
        cin >> coins[i];
    }

    int cnt = 0;
    for (int i = N - 1; i >= 0; i--) {
        cnt += K / coins[i];
        K %= coins[i];
    }
    cout << cnt << '\n';

    return 0;
}