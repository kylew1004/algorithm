// https://www.acmicpc.net/problem/2480

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    vector<int> dices(3);
    for (int i = 0; i < 3; i++) {
        cin >> dices[i];
    }

    sort(dices.begin(), dices.end());

    if (dices[0] == dices[1] && dices[1] == dices[2]) {
        cout << 10000 + dices[0] * 1000 << endl;
    } else if (dices[0] == dices[1] || dices[1] == dices[2]) {
        cout << 1000 + dices[1] * 100 << endl;
    } else {
        cout << dices[2] * 100 << endl;
    }

    return 0;
}