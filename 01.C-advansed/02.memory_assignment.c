#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    // 동적 메모리 할당
    // •	왜 필요한가?
	//    •	배열 크기 미리 모를 때.
	//    •	큰 데이터를 스택이 아닌 힙에 저장.
    //      1.malloc
    int *p3 = (int *)malloc(5 * sizeof(int)); // int 5개 크기만큼 힙에 할식, malloc(형식 크기)형식
    for (int i = 0; i < 5; i++)
    {
        scanf("%d", &p3[i]);
        printf("p3[%d] : %d\n", i, *(p3+i));
    }
    free(p3); // 동적 메모리 해제
    //     2.calloc : 모두 0으로 초기화 상태에서 메모리 할당
    int *p4 = (int *)calloc(5, sizeof(int)); // int 5개 크기만큼 힙에 할당(모두 0으로 초기화), calloc(개수, 형식 크기)형식
    printf("%d\n", *p4); // 0 출력
    for (int i = 0; i < 5; i++)
    {
        scanf("%d", &p4[i]);
        printf("p4[%d] : %d\n", i, *(p3+i));
    }
    free(p4); // 동적 메모리 해제
    //    3.realloc : 이미 할당된 메모리 크기 변경
    int *p5 = (int *)malloc(3 * sizeof(int)); // int 3개 크기만큼 힙에 할당 
    for (int i = 0; i < 3; i++)
    {
        scanf("%d", &p5[i]);
        printf("p5[%d] : %d\n", i, *(p5+i));
    }
    p5 = (int *)realloc(p5, 5 * sizeof(int)); // 크기를 int 5개 크기로 변경, 기존 데이터 유지, realloc(포인터, 새로운 형식 크기)형식
    for (int i = 3; i < 5; i++)
    {
        scanf("%d", &p5[i]);
        printf("p5[%d] : %d\n", i, *(p5+i));//에러 없음
    }
    free(p5); // 동적 메모리 해제
}