// https://www.acmicpc.net/problem/1946

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int t;
    cin >> t;

    while (t--) {
        int n;
        cin >> n;
        vector<pair<int, int>> a(n);
        for (int i = 0; i < n; i++) {
            cin >> a[i].first >> a[i].second;
        }
        sort(a.begin(), a.end());
        int ans = 1;
        int min = a[0].second;
        for (int i = 1; i < n; i++) {
            if (a[i].second < min) {
                min = a[i].second;
                ans += 1;
            }
        }
        cout << ans << '\n';
    }

    return 0;
}