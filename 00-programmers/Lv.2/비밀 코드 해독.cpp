#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int solution(int n, vector<vector<int>> q, vector<int> ans) {
    int answer = 0;
    vector<int> code(5, -1);
    for (int i = 1; i < n-3; i++) {
        code[0] = i;
        for (int j = i+1; j < n-2; j++) {
            code[1] = j;

            for (int k = j+1; k < n-1; k++) {
                code[2] = k;

                for (int l = k+1; l < n-0; l++) {
                    code[3] = l;

                    for (int m = l+1; m < n+1; m++) {
                        code[4] = m;
                        // cout << i << ' ' << j << ' ' << k << ' '<< l << ' '<< m << endl;
                        bool flag = true;
                        for (int o = 0; o < q.size(); o++) {
                            int cnt = 0;
                            for (int p = 0; p < 5; p++) {
                                if (count(q[o].begin(),q[o].end(), code[p])) {
                                    cnt += 1;
                                }
                            }
                            if (cnt != ans[o]) {
                                flag = false;
                            }
                        }
                        if (flag) {
                            answer += 1;
                        }
                    }
                }
            }
        }
    }
    return answer;
}

int main() {
    int n, m;
    cin >> n >> m;
    vector<vector<int>> q(m, vector<int>(5, 0));
    vector<int> ans(m, 0);
    for (int i = 0; i < m; i++) {
        cin >> q[i][0] >> q[i][1] >> q[i][2] >> q[i][3] >> q[i][4];
    }
    for (int i = 0; i < m; i++) {
        cin >> ans[i];
    }
    cout << solution(n, q, ans) << endl;
}

// 10 5
// 1 2 3 4 5
// 6 7 8 9 10
// 3 7 8 9 10
// 2 5 7 9 10
// 3 4 5 6 7
// 2
// 3
// 4
// 3
// 3