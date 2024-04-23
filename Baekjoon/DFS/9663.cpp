// https://www.acmicpc.net/problem/9663

#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

int N;
int cnt = 0;
vector<int> col;

bool isPossible(int level) {
    for (int i = 0; i < level; i++) {
        if (col[i] == col[level] || abs(col[level] - col[i]) == level - i) {
            return false;
        }
    }
    return true;
}

void dfs(int level) {
    if (level == N) {
        cnt++;
        return;
    }
    for (int i = 0; i < N; i++) {
        col[level] = i;
        if (isPossible(level)) {
            dfs(level + 1);
        }
    }
}

int main() {
    cin >> N;
    col.resize(N);
    dfs(0);
    cout << cnt << endl;
    return 0;
}