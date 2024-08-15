// https://www.acmicpc.net/problem/2012

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int n;
    cin >> n;

    vector<int> v(n);
    for (int i = 0; i < n; i++) {
        cin >> v[i];
    }

    sort(v.begin(), v.end());

    long long answer = 0;
    for (int i = 0; i < n; i++) {
        answer += abs(v[i] - (i + 1));
    }

    cout << answer << endl;

    return 0;
}