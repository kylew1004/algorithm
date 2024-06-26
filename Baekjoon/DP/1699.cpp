// https://www.acmicpc.net/problem/1699

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<int> d(n + 1);
    for (int i = 1; i <= n; i++) {
        d[i] = i;
        for (int j = 1; j * j <= i; j++) {
            if (d[i] > d[i - j * j] + 1) {
                d[i] = d[i - j * j] + 1;
            }
        }
    }
    cout << d[n] << '\n';
    return 0;
}