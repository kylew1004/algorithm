// https://www.acmicpc.net/problem/1021

#include <iostream>
#include <deque>
#include <algorithm>
using namespace std;

int main() {
    int N, M;
    cin >> N >> M;
    deque<int> dq;
    for (int i = 1; i <= N; i++) {
        dq.push_back(i);
    }

    int ans = 0;
    while (M--) {
        int x;
        cin >> x;
        int idx = 0;
        for (int i = 0; i < dq.size(); i++) {
            if (dq[i] == x) {
                idx = i;
                break;
            }
        }
        int left = idx;
        int right = dq.size() - idx;
        if (left < right) {
            while (left--) {
                int front = dq.front();
                dq.pop_front();
                dq.push_back(front);
                ans++;
            }
            dq.pop_front();
        } else {
            while (right--) {
                int back = dq.back();
                dq.pop_back();
                dq.push_front(back);
                ans++;
            }
            dq.pop_front();
        }
    }
    cout << ans << '\n';

    return 0;
}