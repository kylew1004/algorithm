// https://www.acmicpc.net/problem/25304

#include <iostream>
using namespace std;

int main() {
    int x, n, total;
    total = 0;
    cin >> x >> n;

    for (int i = 0; i < n; i++) {
        int a, b;
        cin >> a >> b;
        total += a * b;
    }

    if (total == x) cout << "Yes" << "\n";
    else cout << "No" << "\n";

    return 0;
}