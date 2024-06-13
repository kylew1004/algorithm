// https://www.acmicpc.net/problem/2292

#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;
    int ans = 1;
    int num = 1;
    while (num < n) {
        num += 6 * ans;
        ans++;
    }
    cout << ans << '\n';
    return 0;
}