// https://www.acmicpc.net/problem/1145

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int gcd(int a, int b) {
    while (b != 0) {
        int temp = a % b;
        a = b;
        b = temp;
    }
    return a;
}

int lcm(int a, int b) {
    return a / gcd(a, b) * b;
}

int main() {
    vector<int> numbers(5);
    for (int i = 0; i < 5; ++i) {
        cin >> numbers[i];
    }

    int result = 1;
    for (int i = 0; i < 5; ++i) {
        for (int j = i + 1; j < 5; ++j) {
            for (int k = j + 1; k < 5; ++k) {
                int current_lcm = lcm(lcm(numbers[i], numbers[j]), numbers[k]);
                if (result == 1 || current_lcm < result) {
                    result = current_lcm;
                }
            }
        }
    }

    cout << result << endl;

    return 0;
}
