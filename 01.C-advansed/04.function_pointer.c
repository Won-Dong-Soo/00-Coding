#include <stdio.h>
#include <stdlib.h>

int add(int a, int b)
{
    return a + b;
}

int main(void)
{
    int (*funcPtr)(int, int) = add; // 함수 포인터 선언 및 초기화 -> 동적으로 함수 호출. 
    int result = funcPtr(3, 5); // 함수 포인터를 사용하여 함수 호출
    printf("Result of addition: %d\n", result);
    return 0;
}