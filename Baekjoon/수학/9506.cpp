// https://www.acmicpc.net/problem/9506

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    while (true) {
        int n;
        cin >> n;
        if (n == -1) break;
        vector<int> divisors;
        int sum = 0;
        for (int i = 1; i < n; i++) {
            if (n % i == 0) {
                divisors.push_back(i);
                sum += i;
            }
        }
        if (sum == n) {
            cout << n << " = ";
            for (int i = 0; i < divisors.size(); i++) {
                cout << divisors[i];
                if (i != divisors.size() - 1) cout << " + ";
            }
            cout << '\n';
        } else {
            cout << n << " is NOT perfect.\n";
        }
    }
    return 0;
}