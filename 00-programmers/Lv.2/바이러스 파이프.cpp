#include <iostream>
#include <vector>
#include <unordered_set>

using namespace std;

int pow(int x, int y) {
    int size = 1;
    for(int i=0;i<y;i++)
        size *= x;

    return size;
}

int base3to10(const vector<int>& a) {
    int sum = 0;
    for (int j = 0; j < a.size(); j++) {
        sum += a[j] * pow(3, j);
    }
    return sum;
}

void cal(unordered_set<int> infectionlist, const vector<vector<int>>& edges, const int& k, int count, vector<int> countlist, vector<int>& result) {
    if (count == k) {
        result[base3to10(countlist)] = infectionlist.size();
        return;
    }

    int next_count = count;
    next_count++;


    for (int i = 1; i < 4; i++) {
        vector<int> next_countlist = countlist;
        next_countlist[count] = i-1;
        unordered_set<int> next_infectionlist = infectionlist;
        bool changed = true;

        while(changed) {
            changed = false;

            for(auto& e : edges) {
                if(e[2] == i &&
                   (next_infectionlist.count(e[0]) || next_infectionlist.count(e[1]))) {

                    int before = next_infectionlist.size();

                    next_infectionlist.insert(e[0]);
                    next_infectionlist.insert(e[1]);

                    if(before != next_infectionlist.size())
                        changed = true;
                   }
            }
        }
        cal(next_infectionlist, edges, k, next_count, next_countlist, result);

    }
    return;
}

int solution(int n, int infection, vector<vector<int>> edges, int k) {
    int answer = 0;
    vector<int> result(pow(3, k), 0);
    vector<int> countlist(k, 0);
    cal(unordered_set<int> {infection}, edges, k, 0, countlist, result);
    for (int i = 0; i < result.size(); i++) {
        answer = max(answer, result[i]);
        cout << result[i] << endl;
    }

    return answer;
}

int main() {
    int n, infection, k;
    cin >> n >> infection >> k;
    vector<vector<int>> edges(n-1, vector<int>(3, -1));
    for (int i = 0; i < n-1; i++) {
        for (int j = 0; j < 3; j++) {
            cin >> edges[i][j];
        }
    }
    cout << "input end" << "\n" << endl;
    cout << solution(n, infection, edges, k) << endl;
    return 0;
}