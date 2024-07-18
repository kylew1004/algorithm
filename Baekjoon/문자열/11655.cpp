// https://www.acmicpc.net/problem/11655

#include <iostream>
#include <string>
using namespace std;

int main() {
    string s;
    getline(cin, s);
    for (auto &c : s) {
        if ('a' <= c && c <= 'z') {
            c = (c - 'a' + 13) % 26 + 'a';
        } else if ('A' <= c && c <= 'Z') {
            c = (c - 'A' + 13) % 26 + 'A';
        }
    }
    cout << s << '\n';
    return 0;
}