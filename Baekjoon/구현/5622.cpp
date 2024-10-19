// https://www.acmicpc.net/problem/5622

#include <iostream>
#include <string>
using namespace std;

int main() {
    string s;
    cin >> s;
    int answer = 0;

    for (char c : s) {
        if (c >= 'A' && c <= 'C') {
            answer += 3;
        } else if (c >= 'D' && c <= 'F') {
            answer += 4;
        } else if (c >= 'G' && c <= 'I') {
            answer += 5;
        } else if (c >= 'J' && c <= 'L') {
            answer += 6;
        } else if (c >= 'M' && c <= 'O') {
            answer += 7;
        } else if (c >= 'P' && c <= 'S') {
            answer += 8;
        } else if (c >= 'T' && c <= 'V') {
            answer += 9;
        } else if (c >= 'W' && c <= 'Z') {
            answer += 10;
        }
    }

    cout << answer << '\n';

    return 0;
}