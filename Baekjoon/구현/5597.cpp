// https://www.acmicpc.net/problem/5597

#include <iostream>
#include <vector>
using namespace std;

int main() {
    vector<int> v(30);
    for (int i = 0; i < 28; i++) {
        int n;
        cin >> n;
        v[n - 1] = 1;
    }
    for (int i = 0; i < 30; i++) {
        if (v[i] == 0) {
            cout << i + 1 << '\n';
        }
    }
    return 0;
}