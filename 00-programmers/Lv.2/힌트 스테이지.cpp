#include <iostream>
#include <vector>
#include <climits>

using namespace std;

void s(const int stage, int mask, vector<int>& result, int n_stage, int score, vector<int> n_hint, const vector<vector<int>>& hint, const vector<vector<int>>& cost) {
    if (stage == n_stage-1) {
        result[mask] = score + cost[stage][min(n_hint[stage], static_cast<int>(cost.size()) - 1)];
        return;
    }
    for (int i = 0; i < 2; i++) {
        if (i == 0) {
            int next_mask = mask;
            int next_score = score;
            next_score += cost[stage][min(n_hint[stage], static_cast<int>(cost.size()) - 1)];
            s(stage + 1, next_mask, result, n_stage, next_score, n_hint, hint, cost);

        }
        if (i == 1) {
            int next_mask = mask;
            next_mask |= 1 << stage;
            int next_score = score;
            next_score += cost[stage][min(n_hint[stage], static_cast<int>(cost.size()) - 1)] + hint[stage][0];
            for (int j = 1; j < hint[stage].size(); j++) {
                n_hint[hint[stage][j]-1] += 1;
            }
            s(stage + 1, next_mask, result, n_stage, next_score, n_hint, hint, cost);
        }
    }
    return;
}

int solution(vector<vector<int>> cost, vector<vector<int>> hint) {
    vector<int> answer(1 << (cost.size() - 1), INT_MAX);
    s(0, 0, answer, cost.size(), 0, vector<int>(cost.size(), 0), hint, cost);
    int ans = INT_MAX;
    for (int i = 0; i < answer.size(); i++) {
        ans = min(ans, answer[i]);
    }
    return ans;
}

int main() {
    int n_stage, k;
    cin >> n_stage >> k;
    vector<vector<int>> cost(n_stage, vector<int>(n_stage, 0));
    for (int i = 0; i < n_stage; i++) {
        for (int j = 0; j < n_stage; j++) {
            cin >> cost[i][j];
        }
    }
    vector<vector<int>> hint(n_stage-1, vector<int>(k, -1));
    for (int i = 0; i < n_stage-1; i++) {
        for (int j = 0; j < k; j++) {
            cin >> hint[i][j];
        }
    }

    cout << solution(cost, hint) << endl;

}

//[[160, 140, 120, 110, 60], [290, 270, 260, 120, 10], [160, 130, 120, 60, 20], [160, 120, 80, 70, 20], [110, 70, 60, 30, 20]]
// [[40, 2, 3], [40, 5, 3], [20, 5, 4], [50, 5, 5]]