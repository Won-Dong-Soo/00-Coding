#include <stdio.h>
#include <stdlib.h>

int main()
{
    int a = 10;
    int *p = &a;// p안에 a의 주소값 들어감.
    // int b = &a; -> 에러 발생 : 주소값 번수에는 항상 *앞에 붙임.
    printf("Value of a: %d\n", *p);
    int arr[3] = {1,2,3};
    int *p2 = arr;
    printf("Value of arr[0] : %d\n", *p2);
    printf("Value of arr[1] : %d\n", *(p2 + 1));// 주소값에 n더함 -> arr의 n번째 값.
    return 0;
}