// https://www.acmicpc.net/problem/2941

#include <iostream>
#include <string>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    string s;
    cin >> s;

    int cnt = 0;
    for (int i = 0; i < s.size(); i++) {
        if (s[i] == 'c' && (s[i + 1] == '=' || s[i + 1] == '-')) {
            i++;
        } else if (s[i] == 'd' && s[i + 1] == 'z' && s[i + 2] == '=') {
            i += 2;
        } else if ((s[i] == 'd' && s[i + 1] == '-') || (s[i] == 'l' && s[i + 1] == 'j') || (s[i] == 'n' && s[i + 1] == 'j') || (s[i] == 's' && s[i + 1] == '=') || (s[i] == 'z' && s[i + 1] == '=')) {
            i++;
        }
        cnt++;
    }

    cout << cnt << "\n";

    return 0;
}