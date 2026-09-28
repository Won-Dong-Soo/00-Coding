#include <iostream>
#include <cmath>
#include <vector>
#include <algorithm>

using namespace std;

bool isPrime(int n) {
    if (n < 2) return false;

    for (int i = 2; i * i <= n; i++) {
        if (n % i == 0) return false;
    }

    return true;
}

bool isSquare(long long n) {
    if (n < 0) return false;

    long long r = sqrtl(n);
    return r * r == n || (r + 1) * (r + 1) == n;
}

int main() {
    int lim;
    cin >> lim;

    vector<int> answer;

    for (int p = 7; p <= lim; p++) {
        for (int q = 7; q <= lim; q++) {
            if (isPrime(p) && isPrime(q) && p < q && q < 2*p+100) {
                long long x = 1LL * p * p
                            + 5LL * (q + 2) * p
                            + 25;

                if (isSquare(x)) {
                    cout << p << " " << q << endl;
                    answer.push_back(p);
                }
            }
        }
    }

    if (!answer.empty()) {
        cout << *max_element(answer.begin(), answer.end()) << endl;
    }

    return 0;
}