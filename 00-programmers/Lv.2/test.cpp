#include <iostream>
#include <string>

using namespace std;

void dfs(int length, int& result) {
    if (length == 0 || length == -2) {
        result++;
        cout << length << ' ' << result << endl;
        return;
    }
    if (length == 1 || length == -1) {
        result += 2;
        cout << length << ' ' << result << endl;
        return;
    }

    for (int i = 0; i < 3; i++) {
        if (i == 0 || i == 1) {
            int next_length = length;
            next_length--;
            dfs(next_length, result);
        }
        if (i == 2) {
            int next_length = length;
            next_length -= 2;
            dfs(next_length, result);
        }
    }
}

int main() {
    int length = 8;
    int result = 0;
    dfs(length, result);
    cout << result << endl;

    // vertor<int> dp(length);

    return 0;
}

// A -> B
//