// https://www.acmicpc.net/problem/1748

#include <iostream>
#include <cmath>
using namespace std;

int main() {
    int n;
    cin >> n;

    int digits = 0;
    for (int i = 1; i <= n; i *= 10) {
        digits += n - i + 1;
    }

    cout << digits << endl;

    return 0;
}