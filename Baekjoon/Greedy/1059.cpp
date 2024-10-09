// https://www.acmicpc.net/problem/1059

#include <iostream>
#include <vector>
#include <algorithm>

int main() {
    int L, n;
    std::cin >> L;
    std::vector<int> S(L);
    for (int i = 0; i < L; ++i) {
        std::cin >> S[i];
    }
    std::cin >> n;

    if (std::find(S.begin(), S.end(), n) != S.end()) {
        std::cout << 0 << std::endl;
        return 0;
    }

    std::sort(S.begin(), S.end());

    int s_left = 0;
    int s_right = 1001;

    for (int i = 0; i < L; ++i) {
        if (S[i] < n) {
            s_left = S[i];
        } else if (S[i] > n) {
            s_right = S[i];
            break;
        }
    }

    int count = 0;
    for (int A = s_left + 1; A <= n; ++A) {
        for (int B = n; B <= s_right - 1; ++B) {
            if (A < B) {
                count++;
            }
        }
    }

    std::cout << count << std::endl;

    return 0;
}