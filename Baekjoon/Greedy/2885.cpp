// https://www.acmicpc.net/problem/2885

#include <iostream>
using namespace std;

int main() {
    int k;
    cin >> k;
    int n = 1;
    int cnt = 0;

    while (n < k) {
        n *= 2;
    }

    int answer = n;

    while (k > 0) {
        if (k >= n) {
            k -= n;
        } else {
            n /= 2;
            cnt++;
        }
    }

    cout << answer << ' ' << cnt << '\n';

    return 0;
}