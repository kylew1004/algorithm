// https://www.acmicpc.net/problem/2525

#include <iostream>
using namespace std;

int main() {
    int h, m, t;
    cin >> h >> m >> t;
    m += t;
    h += m / 60;
    m %= 60;
    h %= 24;
    cout << h << ' ' << m;
    
    return 0;
}