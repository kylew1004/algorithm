// https://www.acmicpc.net/problem/2437

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int n;
    vector<int> a;

    cin >> n;
    a.resize(n);
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }
    sort(a.begin(), a.end());

    int sum = 0;
    for (int num : a) {
        if (sum + 1 < num) {
            break;
        }
        sum += num;
    }

    cout << sum + 1 << endl;

    return 0;
}