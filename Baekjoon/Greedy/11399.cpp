// https://www.acmicpc.net/problem/11399

#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    int N;
    int arr[1000];
    int total = 0;

    cin >> N;
    for (int i = 0; i < N; i++) {
        cin >> arr[i];
    }

    sort(arr, arr + N);
    for (int i = 0; i < N; i++) {
        total += arr[i] * (N - i);
    }

    cout << total << endl;

    return 0;
}