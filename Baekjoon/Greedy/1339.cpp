// https://www.acmicpc.net/problem/1339

#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
using namespace std;

int main() {
    int N;
    cin >> N;
    vector<string> words(N);
    for (int i = 0; i < N; i++) {
        cin >> words[i];
    }

    vector<int> alpha(26);
    for (int i = 0; i < N; i++) {
        int k = 1;
        for (int j = words[i].size() - 1; j >= 0; j--) {
            alpha[words[i][j] - 'A'] += k;
            k *= 10;
        }
    }

    sort(alpha.begin(), alpha.end(), greater<int>());

    int ans = 0;
    int num = 9;
    for (int i = 0; i < 26; i++) {
        if (alpha[i] == 0) {
            break;
        }
        ans += alpha[i] * num;
        num--;
    }
    cout << ans << '\n';

    return 0;
}