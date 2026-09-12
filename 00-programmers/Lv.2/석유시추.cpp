#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

const vector<int> dx = {0, 1, 0, -1};
const vector<int> dy = {1, 0, -1, 0};

int bfs(const vector<vector<int>>& land, int sy, int sx, vector<vector<bool>>& visited, vector<int>& oil) {
    queue<pair<int, int>> q;
    q.push({sy, sx});
    visited[sy][sx] = true;

    int size = 0;

    while (!q.empty()) {
        auto [y, x] = q.front();
        q.pop();

        size++;
        oil[x] = 1;

        for (int k = 0; k < 4; k++) {
            int ny = y + dy[k];
            int nx = x + dx[k];

            if (ny >= 0 && ny < land.size() &&
                nx >= 0 && nx < land[0].size() &&
                land[ny][nx] == 1 &&
                !visited[ny][nx]) {

                visited[ny][nx] = true;
                q.push({ny, nx});
                }
        }
    }

    return size;
}

int solution(vector<vector<int>> land) {
    int answer = 0;

    int rows = land.size();
    int cols = land[0].size();

    vector<vector<bool>> visited(
        rows,
        vector<bool>(cols, false)
    );

    vector<int> oil(cols, 0);

    for (int y = 0; y < rows; y++) {
        for (int x = 0; x < cols; x++) {

            if (land[y][x] == 1 && !visited[y][x]) {

                vector<int> columns(cols, 0);

                int size = bfs(
                    land,
                    y,
                    x,
                    visited,
                    columns
                );

                for (int x = 0; x < cols; x++) {
                    if (columns[x]) {
                        oil[x] += size;
                    }
                }
            }
        }
    }

    answer = *max_element(oil.begin(), oil.end());

    return answer;
}