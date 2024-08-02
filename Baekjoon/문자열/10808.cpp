// https://www.acmicpc.net/problem/10808

#include <iostream>
#include <string>
using namespace std;

int main() {
    string s;
    cin >> s;

    int cnt[26] = {0, };
    for (char c : s) {
        cnt[c - 'a']++;
    }

    for (int i = 0; i < 26; i++) {
        cout << cnt[i] << ' ';
    }
    cout << '\n';

    return 0;
}