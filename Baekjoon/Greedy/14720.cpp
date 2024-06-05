// https://www.acmicpc.net/problem/14720

#include <iostream>
using namespace std;

int main() {

	int n;
	cin >> n;
	int m[1000];
	int answer = 0;
	int c = 0;

	for (int i = 0; i < n; i++) {
		cin >> m[i];
	}
	for (int j = 0; j < n; j++) {
		if (m[j] == 0 && c == 0) {
			answer++;
			c = 1;
		}
		if (m[j] == 1 && c == 1) {
			answer++;
			c = 2;
		}
		if (m[j] == 2 && c == 2) {
			answer++;
			c = 0;
		}
	}

	cout << answer;
	return 0;
}