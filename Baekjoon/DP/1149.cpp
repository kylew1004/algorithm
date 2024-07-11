// https://www.acmicpc.net/problem/1149

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int N;
    cin >> N;
    vector<vector<int>> cost(N, vector<int>(3));
    for (int i = 0; i < N; i++) {
        cin >> cost[i][0] >> cost[i][1] >> cost[i][2];
    }

    for (int i = 1; i < N; i++) {
        cost[i][0] += min(cost[i - 1][1], cost[i - 1][2]);
        cost[i][1] += min(cost[i - 1][0], cost[i - 1][2]);
        cost[i][2] += min(cost[i - 1][0], cost[i - 1][1]);
    }

    cout << min({cost[N - 1][0], cost[N - 1][1], cost[N - 1][2]}) << '\n';

    return 0;
}