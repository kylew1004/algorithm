// https://www.acmicpc.net/problem/1712

#include <iostream>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int a, b, c;
    cin >> a >> b >> c;
    if (b >= c) cout << -1 << '\n';
    else cout << a / (c - b) + 1 << '\n';
    return 0;
}