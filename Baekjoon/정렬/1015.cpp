// https://www.acmicpc.net/problem/1015

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int n;
    vector<int> a, sorted_a, answer;

    cin >> n;
    a.resize(n);
    sorted_a.resize(n);
    answer.resize(n);
    for (int i = 0; i < n; i++) {
        cin >> a[i];
        sorted_a[i] = a[i];
    }
    sort(sorted_a.begin(), sorted_a.end());

    for (int i = 0; i < n; i++) {
        int idx = find(sorted_a.begin(), sorted_a.end(), a[i]) - sorted_a.begin();
        answer[i] = idx;
        sorted_a[idx] = -1;
    }

    for (int num : answer) {
        cout << num << " ";
    }
    cout << endl;

    return 0;
}