// https://www.acmicpc.net/problem/1977

#include <iostream>
#include <cmath>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int m, n;
    cin >> m >> n;
    int sum = 0, min = 10001;
    for (int i = m; i <= n; i++) {
        if (sqrt(i) == (int)sqrt(i)) {
            sum += i;
            min = i < min ? i : min;
        }
    }
    if (sum == 0) cout << -1 << '\n';
    else cout << sum << '\n' << min << '\n';
    return 0;
}