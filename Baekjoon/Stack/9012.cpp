// https://www.acmicpc.net/problem/9012

#include <iostream>
#include <stack>
#include <string>
using namespace std;

int main() {
    int n;
    cin >> n;
    while (n--) {
        string s;
        cin >> s;
        stack<char> st;
        bool flag = true;
        for (int i = 0; i < s.size(); i++) {
            if (s[i] == '(') {
                st.push(s[i]);
            } else {
                if (st.empty()) {
                    flag = false;
                    break;
                }
                st.pop();
            }
        }
        if (!st.empty()) flag = false;
        if (flag) cout << "YES\n";
        else cout << "NO\n";
    }
    return 0;
}