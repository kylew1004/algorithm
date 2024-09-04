// https://www.acmicpc.net/problem/11047

#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n, k;
    cin >> n >> k;

    vector<int> coins(n);
    for (int i = 0; i < n; i++) {
        cin >> coins[i];
    }

    int count = 0;
    for (int i = n - 1; i >= 0; i--) {
        count += k / coins[i];
        k %= coins[i];
    }

    cout << count << endl;

    return 0;
}