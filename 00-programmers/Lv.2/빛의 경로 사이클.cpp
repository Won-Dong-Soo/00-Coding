#include <iostream>
#include <vector>
#include <string>
using namespace std;

vector<int> f(vector<int>* state, const vector<vector<char>>& grid) {
    (*state)[0] += (*state)[2];
    (*state)[1] += (*state)[3];

    // x 범위
    if ((*state)[0] >= grid[0].size()) {
        (*state)[0] = 0;
    }
    if ((*state)[0] < 0) {
        (*state)[0] = grid[0].size() - 1;
    }

    // y 범위
    if ((*state)[1] >= grid.size()) {
        (*state)[1] = 0;
    }
    if ((*state)[1] < 0) {
        (*state)[1] = grid.size() - 1;
    }

    // L
    if (grid[(*state)[1]][(*state)[0]] == 'L') {
        if ((*state)[2] != 0) {
            (*state)[3] = (*state)[2];
            (*state)[2] = 0;
        }
        else {
            (*state)[2] = -(*state)[3];
            (*state)[3] = 0;
        }
    }

    // R
    else if (grid[(*state)[1]][(*state)[0]] == 'R') {
        if ((*state)[2] == 0) {
            (*state)[2] = (*state)[3];
            (*state)[3] = 0;
        }
        else {
            (*state)[3] = -(*state)[2];
            (*state)[2] = 0;
        }
    }

    return *state;
}


int getDir(const vector<int>& state) {
    if (state[2] == 1)  return 0;  // →
    if (state[2] == -1) return 1;  // ←
    if (state[3] == 1)  return 2;  // ↓
    return 3;                       // ↑
}


void dfs(
    vector<int>* state,
    const vector<int>& parent_state,
    const vector<vector<char>>& grid,
    vector<vector<vector<bool>>>& visited,
    vector<int>& answer,
    int& cnt
) {
    // 현재 state의 실제 방향
    int dir = getDir(*state);

    // 현재 상태 방문 처리
    visited[dir][(*state)[1]][(*state)[0]] = true;

    // 한 칸 이동 + 방향 전환
    vector<int> next_state = f(state, grid);

    cnt++;

    // 시작 상태로 돌아왔으면 사이클 완성
    if (parent_state == next_state) {
        answer.push_back(cnt);
        return;
    }

    // 다음 상태로 계속
    dfs(
        &next_state,
        parent_state,
        grid,
        visited,
        answer,
        cnt
    );
}


vector<int> solution(vector<string>* grids) {
    // string -> char grid
    vector<vector<char>> grid(
        grids->size(),
        vector<char>((*grids)[0].size(), '.')
    );

    for (int i = 0; i < grids->size(); i++) {
        for (int j = 0; j < (*grids)[0].size(); j++) {
            grid[i][j] = (*grids)[i][j];
        }
    }

    /*
        state = {x, y, dx, dy}

        ways:
        0 = →
        1 = ←
        2 = ↓
        3 = ↑
    */
    vector<vector<int>> ways = {
        {1, 0},
        {-1, 0},
        {0, 1},
        {0, -1}
    };

    // visited[direction][y][x]
    vector<vector<vector<bool>>> visited(
        4,
        vector<vector<bool>>(
            grids->size(),
            vector<bool>((*grids)[0].size(), false)
        )
    );

    vector<int> answer;

    for (int y = 0; y < visited[0].size(); y++) {
        for (int x = 0; x < visited[0][0].size(); x++) {

            for (int i = 0; i < 4; i++) {

                // 이미 방문한 방향 상태면 건너뜀
                if (visited[i][y][x]) {
                    continue;
                }

                vector<int> cur_state = {
                    x,
                    y,
                    ways[i][0],
                    ways[i][1]
                };

                // 시작 상태를 별도의 객체로 복사
                vector<int> parent_state = cur_state;

                int cnt = 0;

                dfs(
                    &cur_state,
                    parent_state,
                    grid,
                    visited,
                    answer,
                    cnt
                );
            }
        }
    }

    return answer;
}


int main(void) {
    int r;
    cin >> r;

    vector<string> grids(r);

    for (int i = 0; i < r; i++) {
        cin >> grids[i];
    }

    vector<int> answer = solution(&grids);

    for (int i = 0; i < answer.size(); i++) {
        cout << answer[i] << " ";
    }

    cout << endl;

    return 0;
}