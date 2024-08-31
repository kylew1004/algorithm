// https://www.acmicpc.net/problem/10810

#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n, m;
    cin >> n >> m;

    vector<int> baskets(n, 0);
    for (int i = 0; i < m; i++) {
        int a, b, c;
        cin >> a >> b >> c;

        for (int idx = a - 1; idx < b; idx++) {
            baskets[idx] = c;
        }
    }

    for (int num : baskets) {
        cout << num << " ";
    }
    cout << endl;

    return 0;
}