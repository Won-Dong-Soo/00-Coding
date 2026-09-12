#include <vector>

using namespace std;

int n, m;
int answer;

int dx[4] = {-1, 0, 1, 0};
int dy[4] = {0, 1, 0, -1};

int visited[8][8];

vector<int> setTracks(int d) {
    switch (d) {
        case 0: return {2, 3, 6, 7};
        case 1: return {1, 3, 4, 7};
        case 2: return {2, 3, 4, 5};
        case 3: return {1, 3, 5, 6};
    }

    return {};
}

int turn(int track, int d) {
    switch (track) {
        case 1:
            if (d == 1 || d == 3)
                return d;
            break;

        case 2:
            if (d == 0 || d == 2)
                return d;
            break;

        case 3:
            return d;

        case 4:
            if (d == 1) return 0;
            if (d == 2) return 3;
            break;

        case 5:
            if (d == 2) return 1;
            if (d == 3) return 0;
            break;

        case 6:
            if (d == 0) return 1;
            if (d == 3) return 2;
            break;

        case 7:
            if (d == 0) return 3;
            if (d == 1) return 2;
            break;
    }

    return -1;
}

bool validate(vector<vector<int>>& grid) {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (grid[i][j] > 0 && visited[i][j] == 0)
                return false;

            if (grid[i][j] == 3 && visited[i][j] != 2)
                return false;
        }
    }

    return true;
}

void dfs(int x, int y, int d, vector<vector<int>>& grid) {
    if (x == n - 1 && y == m - 1) {
        if (validate(grid))
            answer++;
        return;
    }

    int nx = x + dx[d];
    int ny = y + dy[d];

    if (nx < 0 || ny < 0 || nx >= n || ny >= m)
        return;

    if (grid[nx][ny] == -1)
        return;

    if (visited[nx][ny] >= 2)
        return;

    vector<int> tracks;

    if (grid[nx][ny] != 0) {
        tracks.push_back(grid[nx][ny]);
    } else {
        tracks = setTracks(d);
    }

    for (int track : tracks) {
        int nd = turn(track, d);

        if (nd == -1)
            continue;

        int original = grid[nx][ny];

        grid[nx][ny] = track;
        visited[nx][ny]++;

        dfs(nx, ny, nd, grid);

        visited[nx][ny]--;
        grid[nx][ny] = original;
    }
}

int solution(vector<vector<int>> grid) {
    n = grid.size();
    m = grid[0].size();

    answer = 0;

    for (int i = 0; i < 8; i++)
        for (int j = 0; j < 8; j++)
            visited[i][j] = 0;

    visited[0][0] = 1;

    dfs(0, 0, 1, grid);

    return answer;
}