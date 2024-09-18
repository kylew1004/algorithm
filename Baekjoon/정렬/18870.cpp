// https://www.acmicpc.net/problem/18870

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<int> a(n), b(n);
    vector<int> c;
    for (int i = 0; i < n; i++) {
        cin >> a[i];
        b[i] = a[i];
    }

    sort(b.begin(), b.end());
    b.erase(unique(b.begin(), b.end()), b.end());

    for (int i = 0; i < n; i++) {
        cout << lower_bound(b.begin(), b.end(), a[i]) - b.begin() << ' ';
    }
    cout << '\n';

    return 0;
}