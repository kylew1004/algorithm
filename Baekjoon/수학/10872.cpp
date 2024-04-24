// https://www.acmicpc.net/problem/10872

#include <iostream>
using namespace std;

int factorial(int n) {
    if (n == 0) {
        return 1;
    }
    return n * factorial(n - 1);
}

int main() {
    int N;
    cin >> N;
    cout << factorial(N) << endl;
    return 0;
}