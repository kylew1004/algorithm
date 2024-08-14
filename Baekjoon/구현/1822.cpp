// https://www.acmicpc.net/problem/1822

#include <iostream>
#include <set>
using namespace std;

int main() {
    int a, b;
    cin >> a >> b;

    set<int> s;
    for (int i = 0; i < a; i++) {
        int x;
        cin >> x;
        s.insert(x);
    }

    for (int i = 0; i < b; i++) {
        int x;
        cin >> x;
        s.erase(x);
    }

    if (s.empty()) {
        cout << 0 << endl;
    } else {
        cout << s.size() << endl;
        for (int x : s) {
            cout << x << ' ';
        }
        cout << endl;
    }

    return 0;
}