#include <iostream>
#include <vector>
#include <deque>

using namespace std;

vector<int> solution(int m, int n, int h, int w, vector<vector<int>> drops) {
    vector<int> answer(2, 0);

    int INF = m * n + 1;

    vector<vector<int>> first_drops(
        m-h+1,
        vector<int>(n-w+1, INF)
    );

    vector<vector<int>> current_drops(
        m,
        vector<int>(n, INF)
    );

    for (int i = 0; i < drops.size(); i++) {
        current_drops[drops[i][0]][drops[i][1]] = i;
    }

    // 1. 가로 방향으로 길이 w의 최소값
    vector<vector<int>> row_min(m,vector<int>(n - w + 1));

    for (int r = 0; r < m; r++) {
        deque<int> dq;
        // dq에는 인덱스 저장되어 있음.

        for (int c = 0; c < n; c++) {

            // 현재 윈도우에서 벗어난 원소 제거
            if (!dq.empty() && dq.front() <= c-w) {
                dq.pop_front();
            }
            // 현재 값보다 큰 값은 앞으로 최소가 될 수 없음
            while (!dq.empty() && current_drops[r][dq.back()] >= current_drops[r][c]) {
                dq.pop_back();
            }

            dq.push_back(c);

            if (c >= w-1) {
                row_min[r][c-w+1] = current_drops[r][dq.front()];
            }
        }
    }


    // 2. 세로 방향으로 길이 h의 최소값
    for (int c = 0; c < n - w + 1; c++) {
        deque<int> dq;

        for (int r = 0; r < m; r++) {

            while (!dq.empty() && dq.front() <= r - h) {
                dq.pop_front();
            }

            while (!dq.empty() &&
                   row_min[dq.back()][c] >= row_min[r][c]) {
                dq.pop_back();
                   }

            dq.push_back(r);

            if (r >= h - 1) {
                first_drops[r - h + 1][c] =
                    row_min[dq.front()][c];
            }
        }
    }

    int maxi = -1;

    for (int i = 0; i <= m-h; i++) {
        for (int j = 0; j <= n-w; j++) {
            if (first_drops[i][j] > maxi) {
                maxi = first_drops[i][j];
                answer = {i, j};
            }
        }
    }

    return answer;
}
int main() {
    int m, n, h, w, length;
    cin >> m >> n >> h >> w >> length;
    vector<vector<int>> drops(length,vector<int>(2,0));
    for (int i = 0; i < length; i++) {
        for (int j = 0; j < 2; j++) {
            cin >> drops[i][j];
        }
    }
    cout << "input all done." << endl;
    vector<int> answer = solution(m, n, h, w, drops);
    cout << answer[0] << ' ' << answer[1] << endl;
}