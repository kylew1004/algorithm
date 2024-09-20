// https://www.acmicpc.net/problem/1541

#include <iostream>
#include <string>
using namespace std;

int main() {
    string s;
    cin >> s;

    int ans = 0;
    string num = "";
    bool minus = false;
    for (int i = 0; i <= s.size(); i++) {
        if (s[i] == '+' || s[i] == '-' || s[i] == '\0') {
            if (minus) {
                ans -= stoi(num);
            } else {
                ans += stoi(num);
            }
            num = "";
            if (s[i] == '-') {
                minus = true;
            }
        } else {
            num += s[i];
        }
    }

    cout << ans << '\n';

    return 0;
}