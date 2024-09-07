// https://www.acmicpc.net/problem/13458

#include <iostream>
#include <vector>

using namespace std;

int main() {
    int n;
    cin >> n;

    vector<int> rooms(n);
    for (int i = 0; i < n; i++) {
        cin >> rooms[i];
    }

    int b, c;
    cin >> b >> c;

    long long answer = 0;
    for (int num : rooms) {
        num -= b;
        answer++;
        if (num > 0) {
            answer += num / c;
            if (num % c != 0) {
                answer++;
            }
        }
    }

    cout << answer << endl;

    return 0;
}