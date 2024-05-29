// https://www.acmicpc.net/problem/3053

#include <iostream>
#include <cmath>
using namespace std;

int main() {
    double r;
    cin >> r;
    cout << fixed;
    cout.precision(6);
    cout << M_PI * r * r << '\n';
    cout << 2 * r * r << '\n';
    return 0;
}