// https://www.acmicpc.net/problem/10162

#include <iostream>
using namespace std;

int main() {
    int t;
    cin >> t;

    if (t % 10 != 0) {
        cout << -1 << '\n';
    } else {
        cout << t / 300 << ' ';
        t %= 300;
        cout << t / 60 << ' ';
        t %= 60;
        cout << t / 10 << '\n';
    }

    return 0;
}