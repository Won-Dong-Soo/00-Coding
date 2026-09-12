#include <iostream>

int main(void)
{
    // unique_ptr
	// •	“소유권 하나”
	// •	가장 빠르고 가장 안전함
	// •	절대 중복 소유 불가
    auto unq_ptr = std::make_unique<int>(10);//기본값 : 10
    std::cout << "Default value : " << *unq_ptr << std::endl;
    std::cout << "Enter a new value: ";
    std::cin >> *unq_ptr;
    std::cout << "New value : " << *unq_ptr << std::endl;
    // shared_ptr
	// •	“참조 카운트 기반 공동 소유”
	// •	여러 객체가 같은 포인터 소유
	// •	무거움(참조 카운트 때문에)
    auto shr_ptr = std::make_shared<int>(10);//기본값 : 10
    auto shr_ptr2 = shr_ptr; //참조 카운트 증가
    std::cout << "Default value : " << *shr_ptr << std::endl;
    std::cout << "Enter a new value: ";
    std::cin >> *shr_ptr;
    std::cout << "New value from shr_ptr : " << *shr_ptr << std::endl;
    std::cout << "New value from shr_ptr2 : " << *shr_ptr2 << std::endl;//둘 다 바뀜.
    // weak_ptr
	// •	shared_ptr의 순환 참조 막기 위한 보조 도구
	// •	소유 X, 감시만
    // auto wk_ptr = std::make_weak_ptr<int>(10); //에러. weak_ptr는 단독 생성 불가.
    std::weak_ptr<int> wk_ptr = shr_ptr; //shared_ptr로부터 생성
    // auto A = std::make_shared<int>(20);
    // auto B = A; -> 순환 참조 발생 -> 참조 카운트가 0이 안되어 메모리 누수 발생
    // 해결책: weak_ptr 사용
    // 활용 예제 - shared_ptr가 가리키는 객체에 접근 -> 죽었는지 확인과정 필요 
    if (auto tmp_ptr = wk_ptr.lock())
    {
        std::cout << "Value from weak_ptr: " << *tmp_ptr << std::endl;
    }
    else
    {
        std::cout << "The managed object has been deleted." << std::endl;
    }
}