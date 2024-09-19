// https://www.acmicpc.net/problem/1041

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<long long> nums(6);
    for (int i = 0; i < 6; i++) {
        cin >> nums[i];
    }

    if (n == 1) {
        long long sum = 0;
        long long max = 0;
        for (int i = 0; i < 6; i++) {
            sum += nums[i];
            if (max < nums[i]) {
                max = nums[i];
            }
        }
        cout << sum - max << '\n';
    } else {
        vector<long long> arr(3);
        arr[0] = min(nums[0], nums[5]);
        arr[1] = min(nums[1], nums[4]);
        arr[2] = min(nums[2], nums[3]);
        sort(arr.begin(), arr.end());
        long long total0 = (arr[0] + arr[1]) * (n - 1) * 4;
        long long total1 = (arr[0] + arr[1]) * (n - 2) * 4;
        long long total2 = (arr[0] + arr[1] + arr[2]) * 4;
        long long total3 = arr[0] * (n - 2) * 4;
        long long total4 = arr[0] * (n - 2) * (n - 2) * 5;
        cout << total0 + total1 + total2 + total3 + total4 << '\n';
    }

    return 0;
}