// https://www.acmicpc.net/problem/20115

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int n;
    vector<double> a;

    cin >> n;
    a.resize(n);
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }

    sort(a.begin(), a.end());
    double sum = a.back();
    for (int i = 0; i < n - 1; i++) {
        sum += a[i] / 2;
    }
    cout << sum << '\n';

    return 0;
}