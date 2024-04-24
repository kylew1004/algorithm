// https://www.acmicpc.net/problem/2581

#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

int total = 0;

bool isPrime(int n) {
    if (n < 2) {
        return false;
    }
    for (int i = 2; i <= sqrt(n); i++) {
        if (n % i == 0) {
            return false;
        }
    }
    return true;
}

int main() {
    int M, N;
    cin >> M >> N;
    for (int i = M; i <= N; i++) {
        if (isPrime(i)) {
            total += i;
        }
    }
    if (total == 0) {
        cout << -1 << endl;
    } else {
        cout << total << endl;
        for (int i = M; i <= N; i++) {
            if (isPrime(i)) {
                cout << i << endl;
                break;
            }
        }
    }
    return 0;
}