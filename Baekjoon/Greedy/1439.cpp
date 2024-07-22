// https://www.acmicpc.net/problem/1439

#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

int main() {
    string s;
    cin >> s;
    int ans = 0;
    for (int i = 1; i < s.size(); i++) {
        if (s[i] != s[i - 1]) {
            ans += 1;
        }
    }
    cout << (ans + 1) / 2 << '\n';
    return 0;
}