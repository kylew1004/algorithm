// https://www.acmicpc.net/problem/5635

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

struct Student {
    string name;
    int day, month, year;
};

bool cmp(const Student& u, const Student& v) {
    if (u.year < v.year) {
        return true;
    } else if (u.year == v.year) {
        if (u.month < v.month) {
            return true;
        } else if (u.month == v.month) {
            return u.day < v.day;
        }
    }
    return false;
}

int main() {
    int n;
    cin >> n;
    vector<Student> a(n);
    for (int i = 0; i < n; i++) {
        cin >> a[i].name >> a[i].day >> a[i].month >> a[i].year;
    }

    sort(a.begin(), a.end(), cmp);
    cout << a[n - 1].name << '\n' << a[0].name << '\n';

    return 0;
}