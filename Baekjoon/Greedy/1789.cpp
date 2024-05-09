// https://www.acmicpc.net/problem/1789

#include <iostream>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    long long S;
    cin >> S;

    long long sum = 0;
    long long i = 1;
    while (sum + i <= S) {
        sum += i;
        i++;
    }
    cout << i - 1 << '\n';

    return 0;
}