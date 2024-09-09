// https://www.acmicpc.net/problem/1431

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int get_sum_of_digits(string s) {
    int sum = 0;
    for (char c : s) {
        if ('0' <= c && c <= '9') {
            sum += c - '0';
        }
    }
    return sum;
}

bool compare(string a, string b) {
    if (a.size() != b.size()) {
        return a.size() < b.size();
    }

    int sum_a = get_sum_of_digits(a);
    int sum_b = get_sum_of_digits(b);
    if (sum_a != sum_b) {
        return sum_a < sum_b;
    }

    return a < b;
}

int main() {
    int n;
    vector<string> a;

    cin >> n;
    a.resize(n);
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }

    sort(a.begin(), a.end(), compare);

    for (string s : a) {
        cout << s << endl;
    }

    return 0;
}