// https://www.acmicpc.net/problem/1182

#include <iostream>
#include <vector>
using namespace std;

int n, s, cnt = 0;
vector<int> v;

void dfs(int idx, int sum) {
    if (idx == n) {
        if (sum == s) cnt++;
        return;
    }
    dfs(idx + 1, sum + v[idx]);
    dfs(idx + 1, sum);
}

int main() {
    cin >> n >> s;
    v.resize(n);
    for (int i = 0; i < n; i++) cin >> v[i];
    dfs(0, 0);
    if (s == 0) cnt--;
    cout << cnt;
    return 0;
}