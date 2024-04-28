// https://www.acmicpc.net/problem/2839

#include <iostream>
using namespace std;

int main() {
    int N;
    cin >> N;

    int cnt = 0;
    while (N > 0) {
        if (N % 5 == 0) {
            N -= 5;
            cnt++;
        } else if (N % 3 == 0) {
            N -= 3;
            cnt++;
        } else if (N > 5) {
            N -= 5;
            cnt++;
        } else {
            cnt = -1;
            break;
        }
    }

    cout << cnt << endl;

    return 0;
}