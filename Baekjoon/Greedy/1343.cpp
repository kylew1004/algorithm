// https://www.acmicpc.net/problem/1343

#include <iostream>
#include <string>
using namespace std;

int main() {
    string board;
    cin >> board;

    string result = "";
    int n = board.length();

    for (int i = 0; i < n; ) {
        if (board[i] == 'X') {
            int count = 0;
            while (i + count < n && board[i + count] == 'X') {
                count++;
            }

            if (count % 2 != 0) {
                cout << "-1" << "\n";
                return 0;
            }

            int aCount = count / 4;
            int bCount = (count % 4) / 2;

            result += string(aCount * 4, 'A') + string(bCount * 2, 'B');
            i += count;
        } else {
            result += board[i];
            i++;
        }
    }

    cout << result << "\n";
    return 0;
}
