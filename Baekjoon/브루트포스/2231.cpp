// https://www.acmicpc.net/problem/2231

#include <iostream>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int N;
    cin >> N;
    for (int i = 1; i < N; i++) {
        int sum = i;
        int num = i;
        while (num) {
            sum += num % 10;
            num /= 10;
        }
        if (sum == N) {
            cout << i << '\n';
            return 0;
        }
    }
    cout << 0 << '\n';

    return 0;
}