// https://www.acmicpc.net/problem/7785

#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
#include <map>
using namespace std;

int main() {
    int n;
    cin >> n;
    map<string, bool> check;
    for (int i = 0; i < n; i++) {
        string name, state;
        cin >> name >> state;
        if (state == "enter") {
            check[name] = true;
        } else {
            check.erase(name);
        }
    }
    vector<string> v;
    for (auto &p : check) {
        v.push_back(p.first);
    }
    sort(v.begin(), v.end(), greater<string>());
    for (auto &name : v) {
        cout << name << '\n';
    }
    return 0;
}