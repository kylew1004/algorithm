// https://www.acmicpc.net/problem/11659

#include <iostream>
#include <vector>
using namespace std;

int N, M;
int arr[100001];

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> N >> M;
    for (int i = 1; i <= N; i++) {
        cin >> arr[i];
        arr[i] += arr[i - 1];
    }

    while (M--) {
        int i, j;
        cin >> i >> j;
        cout << arr[j] - arr[i - 1] << '\n';
    }

    return 0;
}