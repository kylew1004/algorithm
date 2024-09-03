// https://www.acmicpc.net/problem/10973

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

    int i = n - 1;
    while (i > 0 && arr[i - 1] <= arr[i]) {
        i--;
    }

    if (i == 0) {
        cout << -1 << endl;
        return 0;
    }

    int j = n - 1;
    while (arr[i - 1] <= arr[j]) {
        j--;
    }

    swap(arr[i - 1], arr[j]);
    j = n - 1;
    while (i < j) {
        swap(arr[i], arr[j]);
        i++;
        j--;
    }

    for (int num : arr) {
        cout << num << " ";
    }
    cout << endl;

    return 0;
}