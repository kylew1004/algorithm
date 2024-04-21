// # https://www.acmicpc.net/problem/11003

#include <iostream>
#include <deque>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int N, L;
    cin >> N >> L;

    vector<int> A(N);
    for (int i = 0; i < N; i++) {
        cin >> A[i];
    }

    deque<pair<int, int>> dq;
    for (int i = 0; i < N; i++) {
        while (!dq.empty() && dq.front().second <= i - L) {
            dq.pop_front();
        }

        while (!dq.empty() && dq.back().first > A[i]) {
            dq.pop_back();
        }

        dq.push_back({A[i], i});
        cout << dq.front().first << ' ';
    }

    return 0;
}