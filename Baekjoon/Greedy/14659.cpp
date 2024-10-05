// https://www.acmicpc.net/problem/14659

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

    int result = 0;
    int max_height = 0;
    int cnt = 0;
    for (int i = 0; i < n; i++) {
        if (max_height < arr[i]) {
            max_height = arr[i];
            cnt = 0;
        } else {
            cnt++;
        }
        result = max(result, cnt);
    }

    cout << result << '\n';

    return 0;
}