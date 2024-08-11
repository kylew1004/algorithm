#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    long long x, y, w, s;
    cin >> x >> y >> w >> s;

    // 대각선 이동이 가로/세로 이동의 두 배보다 비쌀 때
    if (2 * w < s) {
        cout << (x + y) * w << endl;
    } else {
        long long minXY = min(x, y);
        long long absDiff = abs(x - y);

        // 대각선 이동으로 최소 이동
        long long cost;
        if (absDiff % 2 == 0) {
            cost = s * minXY + min(w, s) * absDiff;
        } else {
            cost = s * minXY + (min(w, s) * (absDiff - 1) + w);
        }

        cout << cost << endl;
    }

    return 0;
}