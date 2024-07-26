// https://www.acmicpc.net/problem/10798

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    vector<string> a(5);
    for (int i = 0; i < 5; i++) {
        cin >> a[i];
    }

    for (int i = 0; i < 15; i++) {
        for (int j = 0; j < 5; j++) {
            if (i < a[j].size()) {
                cout << a[j][i];
            }
        }
    }
    cout << '\n';

    return 0;
}