// https://www.acmicpc.net/problem/9020

#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

int main() {
    vector<bool> prime(10001, true);
    prime[0] = prime[1] = false;
    for (int i = 2; i <= sqrt(10000); i++) {
        if (prime[i]) {
            for (int j = i * i; j <= 10000; j += i) {
                prime[j] = false;
            }
        }
    }
    int t;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;
        for (int i = n / 2; i >= 2; i--) {
            if (prime[i] && prime[n - i]) {
                cout << i << ' ' << n - i << '\n';
                break;
            }
        }
    }
    return 0;
}