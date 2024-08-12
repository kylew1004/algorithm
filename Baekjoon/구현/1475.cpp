// https://www.acmicpc.net/problem/1475

#include <iostream>
#include <algorithm>
#include <string>
using namespace std;

int main() {
    string n;
    cin >> n;

    int count[10] = {0, };
    for (char c : n) {
        count[c - '0']++;
    }

    int maxCount = 0;
    for (int i = 0; i < 10; i++) {
        if (i == 6 || i == 9) {
            continue;
        }

        maxCount = max(maxCount, count[i]);
    }

    int sixNineCount = (count[6] + count[9] + 1) / 2;
    cout << max(maxCount, sixNineCount) << endl;

    return 0;
}