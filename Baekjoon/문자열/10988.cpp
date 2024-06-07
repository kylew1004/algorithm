// https://www.acmicpc.net/problem/10988

#include <iostream>
#include <string>
using namespace std;

int main() {
    string s;
    cin >> s;
    int len = s.length();
    int answer = 1;
    for (int i = 0; i < len / 2; i++) {
        if (s[i] != s[len - i - 1]) {
            answer = 0;
            break;
        }
    }
    cout << answer;
    return 0;
}