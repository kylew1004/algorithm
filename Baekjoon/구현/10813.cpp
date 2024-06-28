// https://www.acmicpc.net/problem/10813

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int N, M;
int ball[101];

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> N >> M;
    for (int i = 1; i <= N; i++) {
        ball[i] = i;
    }

    for (int i = 0; i < M; i++) {
        int a, b;
        cin >> a >> b;
        swap(ball[a], ball[b]);
    }

    for (int i = 1; i <= N; i++) {
        cout << ball[i] << ' ';
    }
    cout << '\n';
    return 0;
}