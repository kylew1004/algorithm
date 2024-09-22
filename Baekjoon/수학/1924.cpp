// https://www.acmicpc.net/problem/1924

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    vector<int> days = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
    vector<string> days_of_week = {"SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"};
    int x, y;
    cin >> x >> y;

    int total = 0;
    for (int i = 0; i < x - 1; i++) {
        total += days[i];
    }
    total += y;

    cout << days_of_week[total % 7] << '\n';

    return 0;
}