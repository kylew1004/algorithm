// https://www.acmicpc.net/problem/1966

#include <iostream>
#include <queue>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int T;
    cin >> T;

    while (T--) {
        int N, M;
        cin >> N >> M;

        queue<pair<int, int>> q;
        priority_queue<int> pq;
        for (int i = 0; i < N; i++) {
            int x;
            cin >> x;
            q.push({x, i});
            pq.push(x);
        }

        int cnt = 0;
        while (!q.empty()) {
            int x = q.front().first;
            int idx = q.front().second;
            q.pop();
            if (pq.top() == x) {
                pq.pop();
                cnt++;
                if (idx == M) {
                    cout << cnt << '\n';
                    break;
                }
            } else {
                q.push({x, idx});
            }
        }
    }

    return 0;
}