// https://www.acmicpc.net/problem/10867

#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n;
    vector<int> a(2001);
    vector<int> answer;

    cin >> n;
    for (int i = 0; i < n; i++) {
        int num;
        cin >> num;
        a[num + 1000] = 1;
    }

    for (int i = 0; i < 2001; i++) {
        if (a[i] == 1) {
            answer.push_back(i - 1000);
        }
    }

    for (int num : answer) {
        cout << num << " ";
    }
    cout << '\n';

    return 0;
}