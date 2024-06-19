// https://www.acmicpc.net/problem/28278

#include <iostream>
#include <stack>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    cin >> N;

    stack<int> stk;
    int command, x;
    for (int i = 0; i < N; i++) {
        cin >> command;
        switch (command) {
            case 1:
                cin >> x;
                stk.push(x);
                break;
            case 2:
                if (stk.empty()) {
                    cout << "-1\n";
                } else {
                    cout << stk.top() << "\n";
                    stk.pop();
                }
                break;
            case 3:
                cout << stk.size() << "\n";
                break;
            case 4:
                cout << (stk.empty() ? 1 : 0) << "\n";
                break;
            case 5:
                if (stk.empty()) {
                    cout << "-1\n";
                } else {
                    cout << stk.top() << "\n";
                }
                break;
            default:
                break;
        }
    }

    return 0;
}