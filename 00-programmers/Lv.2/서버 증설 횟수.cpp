#include <iostream>
#include <cmath>
#include <queue>


using namespace std;

int solution(vector<int> players, int m, int k) {
    queue<int> servers;
    int count = 0;
    int dcount = 0;
    for (int t = 0; t < 24; t++) {
        while (!servers.empty()) {
            if (servers.front() <= t) {
                servers.pop();
            }
            else {
                break;
            }
        }
        if (players[t] > servers.size()*m) {
            dcount = ceil((players[t] - servers.size()*m)/m);
            for (int i = 0; i < dcount; i++) {
                servers.push(t+k);
            }
            count += dcount;
            dcount = 0;
        }

    }
    return count;
}

int main() {
    int m ,k;
    cin >> m >> k;
    vector<int> players(24, 0);
    for (int i = 0; i < 24; i++) {
        cin >> players[i];
    }
    cout << solution(players, m, k) << endl;
    return 0;
}