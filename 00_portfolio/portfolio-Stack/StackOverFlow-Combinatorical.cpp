#include <bits/stdc++.h>
using namespace std;

// OS판별
#ifdef _WIN32
const long long STACK_SIZE = 1048576 - 65536;

#else
const long long STACK_SIZE = 8388608 - 65536;

#endif

// 초기 스택 시작 주소 찾기.
char *STACK_BASE;

void init_stack_base()
{
    char x;
    STACK_BASE = &x;
}
// 현재 스택 사용량 추정.
size_t current_stack_usage()
{
    char y;
    return STACK_BASE > &y ? STACK_BASE - &y : &y - STACK_BASE;
}

void check()
{
    size_t cur_usage = current_stack_usage();
    if (cur_usage >= STACK_SIZE)
    {
        cerr << "Stack Overflow detacted\n";
        exit(1);
    }
}

// 테스트 재귀
void recursion(long long x = 0)
{
    cout << x << " ";
    char waste[1024]; // 메모리 빠르게 사용
    check();
    recursion(x + 1);
}

int main(void)
{
    init_stack_base();
    recursion(0);
    return 0;
}