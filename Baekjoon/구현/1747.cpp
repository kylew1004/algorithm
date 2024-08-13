// https://www.acmicpc.net/problem/1747

#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
using namespace std;

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
    int n;
    cin >> n;

    for (int i = n; ; i++) {
        if (isPrime(i)) {
            string s = to_string(i);
            string reversedS = s;
            reverse(reversedS.begin(), reversedS.end());

            if (s == reversedS) {
                cout << i << endl;
                break;
            }
        }
    }

    return 0;
}