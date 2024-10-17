// https://www.acmicpc.net/problem/11652

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<long long> v(n);

    for (int i = 0; i < n; i++) {
        cin >> v[i];
    }

    sort(v.begin(), v.end());

    long long answer = v[0];
    int cnt = 1;
    int max_cnt = 1;

    for (int i = 1; i < n; i++) {
        if (v[i] == v[i - 1]) {
            cnt++;
        } else {
            cnt = 1;
        }

        if (cnt > max_cnt) {
            max_cnt = cnt;
            answer = v[i];
        }
    }

    cout << answer << '\n';

    return 0;
}