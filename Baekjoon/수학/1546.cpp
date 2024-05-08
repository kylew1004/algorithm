// https://www.acmicpc.net/problem/1546

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int N;
    cin >> N;
    vector<int> v(N);
    for (int i = 0; i < N; i++) {
        cin >> v[i];
    }

    int num = *max_element(v.begin(), v.end());
    int total = 0;
    double avg = 0;
    for (int i = 0; i < N; i++) {
        total += v[i];
    }

    avg = (double)total / num * 100 / N;
    cout << avg << '\n';

    return 0;
}