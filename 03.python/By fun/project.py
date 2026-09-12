def solution(ma, t):
    psum = 0
    asale = 9/10
    csale = 4/5
    if len(ma) >= 10:
        prices = {
            "Bus": (15000*csale, 40000*asale),
            "Ship": (13000*csale, 30000*asale),
            "Airplane": (45000*csale, 70000*asale)
        }
    else:
        prices = {
            "Bus": ((15000, 40000)),
            "Ship": ((13000, 30000)),
            "Airplane": ((45000, 70000))
        }
    for a in ma:
            psum += prices[t][int(a >= 20)]
    return int(psum)

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
member_age1 = [13, 33, 45, 11, 20]
transportation1 = "Bus"
ret1 = solution(member_age1, transportation1)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret1, "입니다.")

member_age2 = [25, 11, 27, 56, 7, 19, 52, 31, 77, 8]
transportation2 = "Ship"
ret2 = solution(member_age2, transportation2)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret2, "입니다.")