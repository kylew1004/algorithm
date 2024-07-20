// https://www.acmicpc.net/problem/1427

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    string s;
    cin >> s;
    sort(s.begin(), s.end(), greater<char>());
    cout << s << '\n';
    return 0;
}