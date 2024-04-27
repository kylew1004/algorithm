// https://www.acmicpc.net/problem/1110

#include <iostream>
using namespace std;

int main() {
    int N;
    cin >> N;
    int cnt = 0;
    int original = N;
    while (true) {
        int a = N / 10;
        int b = N % 10;
        int c = a + b;
        N = b * 10 + c % 10;
        cnt++;
        if (N == original) break;
    }
    cout << cnt << endl;
    return 0;
}