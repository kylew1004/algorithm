// https://www.acmicpc.net/problem/2217

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int N;
    cin >> N;
    vector<int> A(N);
    for (int i = 0; i < N; i++) {
        cin >> A[i];
    }
    sort(A.begin(), A.end());
    int ans = 0;
    for (int i = 0; i < N; i++) {
        ans = max(ans, A[i] * (N - i));
    }
    cout << ans << '\n';

    return 0;
}