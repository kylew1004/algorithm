// https://www.acmicpc.net/problem/1932

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int n;
    cin >> n;

    vector<vector<int>> arr(n, vector<int>(n));
    for (int i = 0; i < n; i++) {
        for (int j = 0; j <= i; j++) {
            cin >> arr[i][j];
        }
    }

    for (int i = 1; i < n; i++) {
        for (int j = 0; j <= i; j++) {
            if (j == 0) {
                arr[i][j] += arr[i - 1][j];
            } else if (j == i) {
                arr[i][j] += arr[i - 1][j - 1];
            } else {
                arr[i][j] += max(arr[i - 1][j - 1], arr[i - 1][j]);
            }
        }
    }

    cout << *max_element(arr[n - 1].begin(), arr[n - 1].end()) << '\n';

    return 0;
}