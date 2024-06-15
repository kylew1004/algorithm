// https://www.acmicpc.net/problem/3003

#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

int main() {
    vector<int> pieces = {1, 1, 2, 2, 2, 8};
    for (int i = 0; i < 6; i++) {
        int n;
        cin >> n;
        cout << pieces[i] - n << ' ';
    }
    return 0;
}