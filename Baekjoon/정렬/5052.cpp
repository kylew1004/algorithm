// https://www.acmicpc.net/problem/5052

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

bool is_consistent(vector<string>& a) {
    for (int i = 0; i < a.size() - 1; i++) {
        if (a[i] == a[i + 1].substr(0, a[i].size())) {
            return false;
        }
    }
    return true;
}

int main() {
    int t;
    cin >> t;
    while (t--) {
        int n;
        vector<string> a;

        cin >> n;
        a.resize(n);
        for (int i = 0; i < n; i++) {
            cin >> a[i];
        }

        sort(a.begin(), a.end());
        if (is_consistent(a)) {
            cout << "YES" << endl;
        } else {
            cout << "NO" << endl;
        }
    }

    return 0;
}