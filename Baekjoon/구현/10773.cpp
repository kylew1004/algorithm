// https://www.acmicpc.net/problem/10773

#include <iostream>
#include <stack>
using namespace std;

int main() {
    int k;
    cin >> k;

    stack<int> s;
    for (int i = 0; i < k; i++) {
        int n;
        cin >> n;

        if (n == 0) {
            s.pop();
        } else {
            s.push(n);
        }
    }

    int sum = 0;
    while (!s.empty()) {
        sum += s.top();
        s.pop();
    }

    cout << sum << '\n';

    return 0;
}