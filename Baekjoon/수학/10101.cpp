// https://www.acmicpc.net/problem/10101

#include <iostream>
using namespace std;

int main() {
    int a, b, c;
    cin >> a >> b >> c;
    if (a + b + c != 180) {
        cout << "Error" << '\n';
    } else if (a == b && b == c) {
        cout << "Equilateral" << '\n';
    } else if (a == b || b == c || c == a) {
        cout << "Isosceles" << '\n';
    } else {
        cout << "Scalene" << '\n';
    }
    return 0;
}