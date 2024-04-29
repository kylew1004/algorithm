// https://www.acmicpc.net/problem/1920

#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int N, M;
    cin >> N;
    int A[N];
    for (int i = 0; i < N; i++) {
        cin >> A[i];
    }
    sort(A, A + N);

    cin >> M;
    for (int i = 0; i < M; i++) {
        int num;
        cin >> num;
        cout << binary_search(A, A + N, num) << '\n';
    }

    return 0;
}