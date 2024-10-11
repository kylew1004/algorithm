// https://www.acmicpc.net/problem/1806

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int n, s;
    cin >> n >> s;
    vector<int> arr(n);
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    int left = 0, right = 0, sum = arr[0], len = n + 1;

    while (left <= right && right < n) {
        if (sum < s) {
            right++;
            sum += arr[right];
        } else if (sum == s) {
            len = min(len, right - left + 1);
            right++;
            sum += arr[right];
        } else if (sum > s) {
            len = min(len, right - left + 1);
            sum -= arr[left];
            left++;
        }
    }

    if (len == n + 1) {
        cout << 0 << '\n';
    } else {
        cout << len << '\n';
    }

    return 0;
}