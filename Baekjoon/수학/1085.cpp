// https://www.acmicpc.net/problem/1085

#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    int x, y, w, h;
    cin >> x >> y >> w >> h;
    cout << min({x, y, w - x, h - y});
    return 0;
}