// https://www.acmicpc.net/problem/10610

#include <iostream>
#include <algorithm>
#include <string>
using namespace std;

int main() {
    string N;
    cin >> N;

    int sum = 0;
    bool hasZero = false;
    for (char c : N) {
        sum += c - '0';
        if (c == '0') {
            hasZero = true;
        }
    }

    if (sum % 3 == 0 && hasZero) {
        sort(N.begin(), N.end(), greater<char>());
        cout << N << '\n';
    } else {
        cout << -1 << '\n';
    }

    return 0;
}