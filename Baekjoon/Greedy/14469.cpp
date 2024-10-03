// https://www.acmicpc.net/problem/14469

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int n;
    vector<pair<int, int>> a;

    cin >> n;
    a.resize(n);
    for (int i = 0; i < n; i++) {
        cin >> a[i].first >> a[i].second;
    }

    sort(a.begin(), a.end());
    int time = 0;
    for (int i = 0; i < n; i++) {
        if (time < a[i].first) {
            time = a[i].first;
        }
        time += a[i].second;
    }
    cout << time << '\n';

    return 0;
}