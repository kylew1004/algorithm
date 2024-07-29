// https://www.acmicpc.net/problem/2920

#include <iostream>
#include <vector>
using namespace std;

int main() {
    vector<int> a(8);
    for (int i = 0; i < 8; i++) {
        cin >> a[i];
    }

    bool ascending = true;
    bool descending = true;
    for (int i = 0; i < 8; i++) {
        if (a[i] != i + 1) {
            ascending = false;
        }
        if (a[i] != 8 - i) {
            descending = false;
        }
    }

    if (ascending) {
        cout << "ascending" << '\n';
    } else if (descending) {
        cout << "descending" << '\n';
    } else {
        cout << "mixed" << '\n';
    }

    return 0;
}