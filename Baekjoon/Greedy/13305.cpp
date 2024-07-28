// https://www.acmicpc.net/problem/13305

#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n;
    cin >> n;

    vector<long long> dist(n - 1);
    for (int i = 0; i < n - 1; i++) {
        cin >> dist[i];
    }

    vector<long long> cost(n);
    for (int i = 0; i < n; i++) {
        cin >> cost[i];
    }

    long long ans = 0;
    long long minCost = cost[0];
    for (int i = 0; i < n - 1; i++) {
        if (cost[i] < minCost) {
            minCost = cost[i];
        }
        ans += minCost * dist[i];
    }

    cout << ans << '\n';

    return 0;
}