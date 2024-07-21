// https://www.acmicpc.net/problem/8979

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int n, k;
    cin >> n >> k;

    vector<vector<int>> arr(n, vector<int>(4));
    for (int i = 0; i < n; i++) {
        cin >> arr[i][0] >> arr[i][1] >> arr[i][2] >> arr[i][3];
    }

    sort(arr.begin(), arr.end(), [](const vector<int> &a, const vector<int> &b) {
        if (a[1] != b[1]) return a[1] > b[1];
        if (a[2] != b[2]) return a[2] > b[2];
        return a[3] > b[3];
    });

    int idx;
    for (int i = 0; i < n; i++) {
        if (arr[i][0] == k) {
            idx = i;
            break;
        }
    }

    for (int i = 0; i < n; i++) {
        if (arr[idx][1] == arr[i][1] && arr[idx][2] == arr[i][2] && arr[idx][3] == arr[i][3]) {
            cout << i + 1 << endl;
            break;
        }
    }

    return 0;
}
