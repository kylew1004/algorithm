// https://www.acmicpc.net/problem/23505

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    vector<int> a(10), b(10);
    for (int i = 0; i < 10; i++) {
        cin >> a[i];
    }
    for (int i = 0; i < 10; i++) {
        cin >> b[i];
    }

    sort(a.begin(), a.end());
    sort(b.begin(), b.end());

    cout << a[7] + a[8] + a[9] << ' ' << b[7] + b[8] + b[9] << '\n';

    return 0;
}