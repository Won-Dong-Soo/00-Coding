#include <bits/stdc++.h>
using namespace std;

int main(void)
{
    cout << "select odd num : " << flush;
    long long n;
    cin >> n;
    int i = 1;
    while (true)
    {
        if (i % n == 0)
        {
            cout << "the number of 1 : " << i;
            break;
        }
    }
    return 0;
}