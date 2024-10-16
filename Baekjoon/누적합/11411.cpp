// https://www.acmicpc.net/problem/11441

#include <iostream>
#include <vector>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int n;
    cin >> n;
    vector<int> arr(n + 1);
    for (int i = 1; i <= n; i++) {
        cin >> arr[i];
        arr[i] += arr[i - 1];
    }

    int m;
    cin >> m;
    while (m--) {
        int a, b;
        cin >> a >> b;
        cout << arr[b] - arr[a - 1] << '\n';
    }

    return 0;
}