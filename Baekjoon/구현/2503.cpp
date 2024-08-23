// https://www.acmicpc.net/problem/2503

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

bool isPossible(const string& num, const string& guess, int strike, int ball) {
    int s = 0;
    int b = 0;

    for (int i = 0; i < 3; i++) {
        if (num[i] == guess[i]) {
            s++;
        } else if (find(num.begin(), num.end(), guess[i]) != num.end()) {
            b++;
        }
    }

    return s == strike && b == ball;
}

int main() {
    int n;
    cin >> n;

    vector<string> numbers;
    vector<int> strikes;
    vector<int> balls;

    for (int i = 0; i < n; i++) {
        string num;
        int strike, ball;
        cin >> num >> strike >> ball;

        numbers.push_back(num);
        strikes.push_back(strike);
        balls.push_back(ball);
    }

    int answer = 0;
    for (int i = 123; i <= 987; i++) {
        string guess = to_string(i);
        if (guess[0] == guess[1] || guess[1] == guess[2] || guess[0] == guess[2] || guess.find('0') != string::npos) {
            continue;
        }

        bool possible = true;
        for (int j = 0; j < n; j++) {
            if (!isPossible(numbers[j], guess, strikes[j], balls[j])) {
                possible = false;
                break;
            }
        }

        if (possible) {
            answer++;
        }
    }

    cout << answer << endl;

    return 0;
}