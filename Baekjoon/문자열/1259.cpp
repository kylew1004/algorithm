// https://www.acmicpc.net/problem/1259

#include <iostream>
#include <string>
using namespace std;

bool isPalindrome(string s) {
    int len = s.length();
    for (int i = 0; i < len / 2; i++) {
        if (s[i] != s[len - i - 1]) {
            return false;
        }
    }
    return true;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    while (true) {
        string s;
        cin >> s;
        if (s == "0") {
            break;
        }
        if (isPalindrome(s)) {
            cout << "yes\n";
        } else {
            cout << "no\n";
        }
    }

    return 0;
}