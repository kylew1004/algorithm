// https://www.acmicpc.net/problem/7568

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int n;
    cin >> n;

    vector<vector<int>> arr(n, vector<int>(3));
    for (int i = 0; i < n; i++) {
        cin >> arr[i][0] >> arr[i][1];
        arr[i][2] = 1;
    }

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (arr[i][0] < arr[j][0] && arr[i][1] < arr[j][1]) {
                arr[i][2]++;
            }
        }
    }

    for (int i = 0; i < n; i++) {
        cout << arr[i][2] << ' ';
    }
    cout << '\n';

    return 0;
}