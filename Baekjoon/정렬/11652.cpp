// https://www.acmicpc.net/problem/11652

#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<long long> a(n);
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }
    sort(a.begin(), a.end());
    long long ans = a[0];
    int ans_cnt = 1;
    int cnt = 1;
    for (int i = 1; i < n; i++) {
        if (a[i] == a[i - 1]) {
            cnt += 1;
        } else {
            cnt = 1;
        }
        if (ans_cnt < cnt) {
            ans_cnt = cnt;
            ans = a[i];
        }
    }
    cout << ans << '\n';
    return 0;
}