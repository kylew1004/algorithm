// https://www.acmicpc.net/problem/2566

#include <iostream>
#include <vector>
using namespace std;

int main() {
    vector<vector<int>> matrix(9, vector<int>(9));
    int max_value = 0;
    int max_row = 0;
    int max_col = 0;

    for (int i = 0; i < 9; i++) {
        for (int j = 0; j < 9; j++) {
            cin >> matrix[i][j];
            if (matrix[i][j] > max_value) {
                max_value = matrix[i][j];
                max_row = i;
                max_col = j;
            }
        }
    }

    cout << max_value << endl;
    cout << max_row + 1 << " " << max_col + 1 << endl;

    return 0;
}