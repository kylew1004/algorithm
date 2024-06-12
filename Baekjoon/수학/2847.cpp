// https://www.acmicpc.net/problem/2847

#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<int> v(n);
    for (int i = 0; i < n; i++) {
        cin >> v[i];
    }
    int ans = 0;
    for (int i = n - 2; i >= 0; i--) {
        if (v[i] >= v[i + 1]) {
            ans += v[i] - v[i + 1] + 1;
            v[i] = v[i + 1] - 1;
        }
    }
    cout << ans << '\n';
    return 0;
}