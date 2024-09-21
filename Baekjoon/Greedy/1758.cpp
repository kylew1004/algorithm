// https://www.acmicpc.net/problem/1758

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<int> a(n);
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }

    sort(a.begin(), a.end(), greater<int>());

    long long ans = 0;
    for (int i = 0; i < n; i++) {
        if (a[i] - i > 0) {
            ans += a[i] - i;
        }
    }

    cout << ans << '\n';

    return 0;
}