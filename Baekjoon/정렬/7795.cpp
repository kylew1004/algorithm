// https://www.acmicpc.net/problem/7795

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int t;
    cin >> t;
    while (t--) {
        int n, m;
        vector<int> a, b;

        cin >> n >> m;
        a.resize(n);
        b.resize(m);
        for (int i = 0; i < n; i++) {
            cin >> a[i];
        }
        for (int i = 0; i < m; i++) {
            cin >> b[i];
        }

        sort(a.begin(), a.end());
        sort(b.begin(), b.end());

        int ans = 0;
        for (int i = 0; i < n; i++) {
            int left = 0, right = m;
            while (left < right) {
                int mid = (left + right) / 2;
                if (a[i] > b[mid]) {
                    left = mid + 1;
                } else {
                    right = mid;
                }
            }
            ans += left;
        }

        cout << ans << '\n';
    }

    return 0;
}