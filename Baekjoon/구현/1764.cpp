// https://www.acmicpc.net/problem/1764

#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
using namespace std;

int main() {
    int n, m;
    cin >> n >> m;
    map<string, bool> check;
    for (int i = 0; i < n; i++) {
        string name;
        cin >> name;
        check[name] = true;
    }
    vector<string> v;
    for (int i = 0; i < m; i++) {
        string name;
        cin >> name;
        if (check[name]) {
            v.push_back(name);
        }
    }
    sort(v.begin(), v.end());
    cout << v.size() << '\n';
    for (auto &name : v) {
        cout << name << '\n';
    }
    return 0;
}