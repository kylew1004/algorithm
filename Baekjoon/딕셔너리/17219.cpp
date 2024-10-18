// https://www.acmicpc.net/problem/17219

#include <iostream>
#include <unordered_map>
#include <string>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int n, m;
    cin >> n >> m;
    unordered_map<string, string> um;

    for (int i = 0; i < n; i++) {
        string a, b;
        cin >> a >> b;
        um[a] = b;
    }

    for (int i = 0; i < m; i++) {
        string a;
        cin >> a;
        cout << um[a] << '\n';
    }

    return 0;
}