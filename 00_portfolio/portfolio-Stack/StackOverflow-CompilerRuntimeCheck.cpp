#include <bits/stdc++.h>
using namespace std;

#ifdef _WIN32
#include <windows.h>
#else
#include <sys/mman.h>
#include <unistd.h>
#endif
// 컴파일러 런타임 체크 시뮬레이션

// 기준점
char *runtime_stack_base = nullptr;
size_t STACK_LIMIT_RUNTIME = STACK_SIZE_GUARD - 65536; // 64KB 여유

void init_runtime_stack()
{
    char x;
    runtime_stack_base = &x;
}

size_t current_stack_usage()
{
    char y;
    return runtime_stack_base > &y ? runtime_stack_base - &y : &y - runtime_stack_base;
}

void check_stack_runtime()
{
    if (current_stack_usage() >= STACK_LIMIT_RUNTIME)
    {
        cerr << "[Runtime Check] Stack overflow detected! Usage: "
             << current_stack_usage() << " bytes\n";
        exit(1);
    }
}

// 테스트 재귀

void recursion_guard(long long x = 0)
{
    char waste[1024];      // 스택 사용 증가
    check_stack_runtime(); // 런타임 체크 시뮬레이션
    cout << x << "\n";     // 출력 원하면 활성화
    recursion_guard(x + 1);
}

int main()
{
    cout << "Initializing Runtime Check...\n";
    init_runtime_stack();

    cout << "Starting recursion test...\n";
    recursion_guard();

    return 0;
}