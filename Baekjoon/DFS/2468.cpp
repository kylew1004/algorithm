// https://www.acmicpc.net/problem/2468

#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;

int dfs(vector<vector<int>>& a, vector<vector<bool>>& check, int x, int y, int h) {
    int n = a.size();
    int dx[] = {0, 0, 1, -1};
    int dy[] = {1, -1, 0, 0};
    check[x][y] = true;
    int ans = 1;
    
    for (int k = 0; k < 4; k++) {
        int nx = x + dx[k];
        int ny = y + dy[k];
        if (0 <= nx && nx < n && 0 <= ny && ny < n) {
            if (a[nx][ny] > h && check[nx][ny] == false) {
                ans += dfs(a, check, nx, ny, h);
            }
        }
    }
    return ans;
}

int main() {
    int n;
    cin >> n;
    vector<vector<int>> a(n, vector<int>(n));
    int min_h = 100;
    int max_h = 0;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> a[i][j];
            min_h = min(min_h, a[i][j]);
            max_h = max(max_h, a[i][j]);
        }
    }
    int ans = 1;
    for (int h = min_h; h < max_h; h++) {
        vector<vector<bool>> check(n, vector<bool>(n));
        int cnt = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (a[i][j] > h && check[i][j] == false) {
                    cnt += (dfs(a, check, i, j, h) > 0);
                }
            }
        }
        ans = max(ans, cnt);
    }
    cout << ans << '\n';
    return 0;
}