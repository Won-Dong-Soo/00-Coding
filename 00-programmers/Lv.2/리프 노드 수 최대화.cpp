#include <iostream>
#include <vector>
using namespace std;

long long D, S;
long long answer = 1;

void simulate(vector<int>& seq)
{
    long long frontier = 1;
    long long used = 0;

    // 아무것도 안 하고 현재 노드를 리프로 만드는 경우
    answer = max(answer, frontier);

    for (int k : seq)
    {
        // 현재 상태에서 종료
        answer = max(answer, frontier);

        // 완전 분배 가능
        if (used + frontier <= D)
        {
            used += frontier;
            frontier *= k;

            // 이 깊이에서 멈추기
            answer = max(answer, frontier);
        }
        else
        {
            // 부분 분배
            long long canSplit = D - used;

            // canSplit개의 분배 노드만 k분배
            // 나머지는 바로 리프
            long long leaves =
                (frontier - canSplit) + canSplit * k;

            answer = max(answer, leaves);
            return;
        }
    }

    answer = max(answer, frontier);
}


int solution(int dist_limit, int split_limit)
{
    D = dist_limit;
    S = split_limit;

    answer = 1;

    vector<int> seq;

    // 2의 개수
    for (int a = 0; a <= 31; a++)
    {
        long long p2 = 1;

        bool ok = true;
        for (int i = 0; i < a; i++)
        {
            p2 *= 2;
            if (p2 > S)
            {
                ok = false;
                break;
            }
        }

        if (!ok)
            break;


        // 3의 개수
        long long p = p2;

        for (int b = 0; b <= 20; b++)
        {
            if (p > S)
                break;

            seq.clear();

            for (int i = 0; i < a; i++)
                seq.push_back(2);

            for (int i = 0; i < b; i++)
                seq.push_back(3);


            simulate(seq);


            if (p > S / 3)
                break;

            p *= 3;
        }
    }

    return answer;
}
int main() {
    int dist_limit, split_limit;
    cin >> dist_limit >> split_limit;
    cout << solution(dist_limit, split_limit) << endl;
    return 0;
}