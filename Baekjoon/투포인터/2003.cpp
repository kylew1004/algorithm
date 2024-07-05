// https://www.acmicpc.net/problem/2003

#include <iostream>
#include <vector>
using namespace std;

int main() {
    int N, M;
    cin >> N >> M;
    vector<int> A(N);
    for (int i = 0; i < N; i++) {
        cin >> A[i];
    }

    int ans = 0;
    for (int i = 0; i < N; i++) {
        int sum = 0;
        for (int j = i; j < N; j++) {
            sum += A[j];
            if (sum == M) {
                ans++;
                break;
            }
        }
    }
    cout << ans << endl;

    return 0;
}