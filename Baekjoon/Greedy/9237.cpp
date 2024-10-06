// https://www.acmicpc.net/problem/9237

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int n;
    vector<int> arr;

    cin >> n;
    arr.resize(n);
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    sort(arr.begin(), arr.end(), greater<int>());
    int result = 0;
    for (int i = 0; i < n; i++) {
        result = max(result, arr[i] + i + 2);
    }

    cout << result << '\n';

    return 0;
}