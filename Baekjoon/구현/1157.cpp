// https://www.acmicpc.net/problem/1157

#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    string s;
    cin >> s;

    vector<int> count(26);
    for (int i = 0; i < s.size(); i++) {
        if ('a' <= s[i] && s[i] <= 'z') {
            count[s[i] - 'a']++;
        } else {
            count[s[i] - 'A']++;
        }
    }

    int max_count = *max_element(count.begin(), count.end());
    int max_index = max_element(count.begin(), count.end()) - count.begin();

    int max_count_count = 0;
    for (int i = 0; i < 26; i++) {
        if (count[i] == max_count) {
            max_count_count++;
        }
    }

    if (max_count_count == 1) {
        cout << (char)('A' + max_index) << '\n';
    } else {
        cout << '?' << '\n';
    }

    return 0;
}