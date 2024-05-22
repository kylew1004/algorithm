// https://www.acmicpc.net/problem/11050

#include <iostream>
using namespace std;

int factorial(int n) {
    if (n == 0) return 1;
    return n * factorial(n - 1);
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int n, k;
    cin >> n >> k;
    cout << factorial(n) / (factorial(k) * factorial(n - k)) << '\n';
    return 0;
}