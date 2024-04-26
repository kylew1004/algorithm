// https://www.acmicpc.net/problem/5585

#include <iostream>
using namespace std;

int main() {
    int N;
    cin >> N;
    int cnt = 0;
    int change = 1000 - N;
    int coins[6] = {500, 100, 50, 10, 5, 1};
    for (int i = 0; i < 6; i++) {
        cnt += change / coins[i];
        change %= coins[i];
    }
    cout << cnt << endl;
    return 0;
}