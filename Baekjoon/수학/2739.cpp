// https://www.acmicpc.net/problem/2739

#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;
    for (int i = 1; i <= 9; i++) {
        cout << n << " * " << i << " = " << n * i << endl;
    }
    return 0;
}