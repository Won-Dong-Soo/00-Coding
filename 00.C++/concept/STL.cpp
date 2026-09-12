#include <iostream>
#include <vector>
#include <map>
#include <unordered_map>
#include <string>
#include <algorithm>

int main(void)
{
    // STL이란?
    // 자료구조 + 알고리즘을 최적화된 상태로 미리 구현해둔 표준 라이브러리.

    // ✅ 1) vector — 동적 배열 (압도적 사용 빈도 1위)

    // 거의 모든 상황에서 리스트나 배열 대신 이걸 쓰면 된다.

    // ✅ 특징
    // 	•	메모리 연속적
    // 	•	끝에서 push_back O(1)
	//     •	중간 삽입은 느림 (배열이라 이동 필요)
	//     •	인덱스 접근 O(1)
	//     •	내부적으로 resizing 자동 처리
    std::vector<int> v = {3,2,1,0,-1,-2};
    std::cout << "Default:" << std::endl;
    for (auto x : v)
    {
        std::cout << x << ",";
    }
    std::cout << "\n";
    std::sort(v.begin(), v.end());
    std::cout << "Sorted : " << std::endl;
    for (auto& x : v)
    {
        std::cout << x << ",";
    }

    // ✅ 2) map — 레드-블랙 트리 기반 정렬 연관 컨테이너

    // ✅ 특징
    //     •	키가 항상 정렬된 상태
    //     •	탐색/삽입/삭제: O(log N)
    //     •	순회하면 정렬된 순서
    //     •	lower_bound 가능
    std::map<std::string, int> m;
    m["banana"] = 3;
    m["apple"] = 1;
    std::cout << "\n";
    for (auto& [key, value] : m)
    {
        std::cout << key << " : " << value << "\n";//정렬됨  
    }
    // ✅ unordered_map — 해시 기반 연관 컨테이너

    // std::unordered_map은 해시 테이블 기반이다.
    // map이 레드-블랙 트리인 것과 완전히 다르다.

    // ⸻---------------------------------------------------

    // ✅ 1) 시간복잡도 (이게 가장 중요)
    //     •	탐색 / 삽입 / 삭제: 평균 O(1)
    //     •	최악은 O(N)인데 거의 안 터짐.

    // → 빠른 키 조회가 필요하면 무조건 unordered_map.

    // ⸻---------------------------------------------------

    // ✅ 2) 키 순서 없음

    // map처럼 정렬된 순서 유지 안 함.

    // 즉, 순회할 때 순서가 뒤죽박죽이다.
    // ✅ 3) 내부 구조
	// •	버킷(bucket) 배열 + 해시 함수
	// •	충돌: 체이닝 방식 (linked list or small array 형태)
	// •	재해싱(rehash) 자동

    // ⸻--------------------------------------------------

    // ✅ 4) 특징 요약

    // ✅ 장점
    //     •	압도적으로 빠른 조회 속도 (O(1))
    //     •	대규모 데이터 처리에서 유리
    //     •	string 키를 엄청 빨리 처리

    // ✅ 단점
    //     •	키 정렬 없음
    //     •	메모리 더 많이 씀
    //     •	반복 순서 비결정적
    //     •	커스텀 타입 쓰려면 해시 함수 직접 정의 필요
    std::unordered_map<std::string, int> uom;
    uom["apple"] = 1;
    uom["banana"] = 2;
    uom["zoo"] = 3;
    uom["app"] = 2023;

    std::cout << "=== Key : Bucket ===\n";
    for (auto& [key, value] : uom) {
        std::cout << key << " : " 
                  << uom.bucket(key)  // key가 들어있는 버킷 번호
                  << " (value=" << value << ")\n";
    }

    std::cout << "\nTotal buckets: " << uom.bucket_count() << "\n";

    // 각 버킷별로 어떤 키가 들어있는지 확인
    for (size_t i = 0; i < uom.bucket_count(); ++i) {
        std::cout << "Bucket " << i << " : ";
        for (auto it = uom.begin(i); it != uom.end(i); ++it) {
            std::cout << it->first << " ";
        }
        std::cout << "\n";
    }

    return 0;
}