// https://www.acmicpc.net/problem/1874

#include <iostream>
#include <vector>
#include <stack>
#include <string>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<int> a(n);
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }
    stack<int> s;
    vector<char> result;
    int i = 0;
    for (int x = 1; x <= n; x++) {
        s.push(x);
        result.push_back('+');
        while (!s.empty() && s.top() == a[i]) {
            s.pop();
            result.push_back('-');
            i++;
        }
    }
    if (!s.empty()) {
        cout << "NO\n";
    } else {
        for (char c : result) {
            cout << c << '\n';
        }
    }
    return 0;
}