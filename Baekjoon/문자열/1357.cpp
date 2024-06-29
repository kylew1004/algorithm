// https://www.acmicpc.net/problem/1357

#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int main() {
    string x, y;
    cin >> x >> y;

    reverse(x.begin(), x.end());
    reverse(y.begin(), y.end());

    int sum = stoi(x) + stoi(y);
    string result = to_string(sum);

    reverse(result.begin(), result.end());
    cout << stoi(result) << endl;

    return 0;
}