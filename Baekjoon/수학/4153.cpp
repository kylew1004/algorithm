// https://www.acmicpc.net/problem/4153

#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    while (true) {
        int a, b, c;
        cin >> a >> b >> c;
        if (a == 0 && b == 0 && c == 0) break;
        if (a > b) swap(a, b);
        if (b > c) swap(b, c);
        if (a * a + b * b == c * c) {
            cout << "right\n";
        } else {
            cout << "wrong\n";
        }
    }
    return 0;
}
