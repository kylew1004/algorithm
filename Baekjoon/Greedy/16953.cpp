// https://www.acmicpc.net/problem/16953

#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;

int main() {
    long long a, b;
    cin >> a >> b;

    queue<pair<long long, long long>> q;
    q.push(make_pair(a, 1));
    while (!q.empty()) {
        long long x = q.front().first;
        long long cnt = q.front().second;
        q.pop();
        if (x == b) {
            cout << cnt << '\n';
            return 0;
        }
        if (x * 2 <= b) {
            q.push(make_pair(x * 2, cnt + 1));
        }
        if (x * 10 + 1 <= b) {
            q.push(make_pair(x * 10 + 1, cnt + 1));
        }
    }
    cout << -1 << '\n';
    return 0;
}