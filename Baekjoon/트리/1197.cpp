// https://www.acmicpc.net/problem/1197

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int V, E;
int parent[10001];
vector<pair<int, pair<int, int>>> edges;

int find(int x) {
    if (x == parent[x]) {
        return x;
    }
    return parent[x] = find(parent[x]);
}

void merge(int x, int y) {
    x = find(x);
    y = find(y);
    if (x != y) {
        parent[x] = y;
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> V >> E;
    for (int i = 1; i <= V; i++) {
        parent[i] = i;
    }

    for (int i = 0; i < E; i++) {
        int a, b, c;
        cin >> a >> b >> c;
        edges.push_back({c, {a, b}});
    }

    sort(edges.begin(), edges.end());

    int ans = 0;
    for (int i = 0; i < E; i++) {
        int a = edges[i].second.first;
        int b = edges[i].second.second;
        if (find(a) != find(b)) {
            merge(a, b);
            ans += edges[i].first;
        }
    }

    cout << ans << '\n';
    return 0;
}