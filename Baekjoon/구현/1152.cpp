// https://www.acmicpc.net/problem/1152

#include <iostream>
#include <string>
using namespace std;

int main() {
    string s;
    getline(cin, s);

    int count = 0;
    for (int i = 0; i < s.size(); i++) {
        if (s[i] == ' ') {
            count++;
        }
    }

    if (s[0] == ' ') {
        count--;
    }
    if (s[s.size() - 1] == ' ') {
        count--;
    }

    cout << count + 1 << '\n';

    return 0;
}