// https://www.acmicpc.net/problem/1065

#include <iostream>
using namespace std;

bool check(int n) {
    if (n < 100) {
        return true;
    } else if (n == 1000) {
        return false;
    } else {
        int a = n / 100;
        int b = (n / 10) % 10;
        int c = n % 10;
        return a - b == b - c;
    }
}

int main() {
    int n;
    cin >> n;
    int ans = 0;
    for (int i = 1; i <= n; i++) {
        if (check(i)) {
            ans += 1;
        }
    }
    cout << ans << '\n';
    return 0;
}