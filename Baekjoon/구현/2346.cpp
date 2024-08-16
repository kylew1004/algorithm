// https://www.acmicpc.net/problem/2346

#include <iostream>
#include <vector>

using namespace std;

int main() {
    int n;
    cin >> n;

    vector<int> balloons(n);
    vector<int> idx(n);
    vector<int> answer;

    for (int i = 0; i < n; i++) {
        cin >> balloons[i];
        idx[i] = i + 1;
    }

    int target = 0;
    int tmp = balloons[target];
    answer.push_back(idx[target]);
    balloons.erase(balloons.begin() + target);
    idx.erase(idx.begin() + target);

    while (!balloons.empty()) {
        if (tmp < 0) {
            target = (target + tmp) % static_cast<int>(balloons.size());
            if (target < 0) {
                target += balloons.size();
            }
        } else {
            target = (target + tmp - 1) % static_cast<int>(balloons.size());
        }

        tmp = balloons[target];
        answer.push_back(idx[target]);
        balloons.erase(balloons.begin() + target);
        idx.erase(idx.begin() + target);
    }

    for (int num : answer) {
        cout << num << " ";
    }
    cout << endl;

    return 0;
}