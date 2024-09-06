// https://www.acmicpc.net/problem/11650

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int n;
    cin >> n;

    vector<pair<int, int>> points(n);
    for (int i = 0; i < n; i++) {
        cin >> points[i].first >> points[i].second;
    }

    sort(points.begin(), points.end());

    for (int i = 0; i < n; i++) {
        cout << points[i].first << " " << points[i].second << "\n";
    }

    return 0;
}