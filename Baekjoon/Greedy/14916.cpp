// https://www.acmicpc.net/problem/14916

#include <iostream>
using namespace std;

int main() {
    int n, answer = 0;

    cin >> n;
    while (n > 0) {
        if (n % 5 == 0) {
            answer += n / 5;
            n = 0;
        } else {
            n -= 2;
            answer++;
        }
    }

    if (n < 0) {
        cout << -1 << '\n';
    } else {
        cout << answer << '\n';
    }

    return 0;
}