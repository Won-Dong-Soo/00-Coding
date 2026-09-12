#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    // 구조체 (struct)
    // •	관련 데이터들을 하나로 묶어서 관리하는 사용자 정의 자료형.(파이썬 의 클래스와 유사, 메서드 없는 클래스.)
    // •	구조체 정의
    // struct Student
    // {
    //     int id;
    //     char name[20];
    //     float score;
    // };
    // •	구조체 변수 선언 및 초기화
    // struct Student student1 = {1, "Alice", 95.5};
    // struct Student student2; -> 이러면 계속 앞에 struct 붙여야함.
    // •	typedef를 사용하여 구조체 별칭 정의
    typedef struct Student
    {
        int id;
        char *name;
        float score;
    }Student;//여기서 별칭 정의
    Student student1; // typedef로 별칭 정의 후 구조체 변수 선언
    student1.id = 1;
    student1.name = "Dongsoo";
    student1.score = 100.0;
    printf("ID:%d, Name:%s, Score:%.2f\n", student1.id, student1.name, student1.score);
    // •	구조체 포인터
    Student *pStudent1 = &student1;
    // pStudent1->id = 2; <=> (*pStudent1).id = 2;
    printf("ID:%d, Name:%s, Score:%.2f\n", pStudent1->id, pStudent1->name, pStudent1->score);

    return 0;
}