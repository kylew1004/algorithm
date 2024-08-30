// https://www.acmicpc.net/problem/10807

#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n;
    cin >> n;

    vector<int> count(201, 0);
    for (int i = 0; i < n; i++) {
        int num;
        cin >> num;
        count[num + 100]++;
    }

    int v;
    cin >> v;

    cout << count[v + 100] << endl;

    return 0;
}