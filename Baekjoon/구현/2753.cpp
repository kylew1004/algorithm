// https://www.acmicpc.net/problem/2753

#include <iostream>
using namespace std;

int main() {
    int year;
    cin >> year;
    if (year % 4 == 0 && (year % 100 != 0 || year % 400 == 0)) {
        cout << 1;
    } else {
        cout << 0;
    }
    return 0;
}