// https://www.acmicpc.net/problem/14487

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
    for (int i = 0; i < n; i++) {
        result += arr[i];
    }
    result -= *max_element(arr.begin(), arr.end());

    cout << result << '\n';

    return 0;
}