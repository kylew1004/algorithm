// https://www.acmicpc.net/problem/10811

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int n, m;
    cin >> n >> m;
    vector<int> a(n);
    for (int i = 0; i < n; i++) {
        a[i] = i + 1;
    }
    while (m--) {
        int i, j;
        cin >> i >> j;
        reverse(a.begin() + i - 1, a.begin() + j);
    }
    for (int i = 0; i < n; i++) {
        cout << a[i] << ' ';
    }
    return 0;
}