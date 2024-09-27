// https://www.acmicpc.net/problem/16435

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int n, l;
    vector<int> a;

    cin >> n >> l;
    a.resize(n);
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }

    sort(a.begin(), a.end());
    for (int num : a) {
        if (l >= num) {
            l++;
        } else {
            break;
        }
    }
    cout << l << '\n';

    return 0;
}