// https://www.acmicpc.net/problem/1620

#include <iostream>
#include <map>
#include <string>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int N, M;
    cin >> N >> M;

    map<string, int> nameToIndex;
    map<int, string> indexToName;
    for (int i = 1; i <= N; i++) {
        string name;
        cin >> name;
        nameToIndex[name] = i;
        indexToName[i] = name;
    }

    for (int i = 0; i < M; i++) {
        string query;
        cin >> query;
        if (query[0] >= '0' && query[0] <= '9') {
            cout << indexToName[stoi(query)] << '\n';
        } else {
            cout << nameToIndex[query] << '\n';
        }
    }

    return 0;
}