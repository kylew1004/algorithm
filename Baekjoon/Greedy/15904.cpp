// https://www.acmicpc.net/problem/15904

#include <iostream>
#include <string>
using namespace std;

int main() {
    string s, ucpc = "UCPC";
    getline(cin, s);

    int idx = 0;
    for (char c : s) {
        if (c == ucpc[idx]) {
            idx++;
        }
        if (idx == 4) {
            break;
        }
    }

    if (idx == 4) {
        cout << "I love UCPC" << '\n';
    } else {
        cout << "I hate UCPC" << '\n';
    }

    return 0;
}