// https://www.acmicpc.net/problem/10818

#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int N;
    cin >> N;
    int A[N];
    for (int i = 0; i < N; i++) {
        cin >> A[i];
    }
    sort(A, A + N);
    cout << A[0] << ' ' << A[N - 1] << '\n';

    return 0;
}