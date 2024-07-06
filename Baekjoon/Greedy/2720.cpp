// https://www.acmicpc.net/problem/2720

#include <iostream>
using namespace std;

int main() {
    int T;
    cin >> T;
    
    while (T--) {
        int C;
        cin >> C;
        int Q = C / 25;
        C %= 25;
        int D = C / 10;
        C %= 10;
        int N = C / 5;
        C %= 5;
        int P = C;
        cout << Q << ' ' << D << ' ' << N << ' ' << P << '\n';
    }

    return 0;
}