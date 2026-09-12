# %%
# 주차장 구현(클래스 사용)
import random

class Car:
    def __init__(self, car_number, car_kind, car_color):
        self.car_number = car_number
        self.car_kind = car_kind
        self.car_color = car_color
        self.slot = None
        self.current_time = 0
        self.out_time = 0
    
    def info(self):
        print(f"차량 번호 : {self.car_number}, \n차량 종류 : {self.car_kind}, \n차량 색상 : {self.car_color}, \n차량 위치 : {self.slot}, \n입차 시간 : {self.current_time['H']%24}시 {self.current_time['M']}분, \n출차 시간 : {self.out_time['H']%24}시 {self.out_time['M']}분")

class ParkingLot:
    def __init__(self, row, col):
        self.col = col # 세로 개수
        self.row = row # 가로 개수
        self.space = col * row
        self.cars = {"class" : [], "number" : []}
        self.slots = []
        nums = 1
        for i in range(row):
            tmp = []
            for j in range(col):
                tmp.append([False, nums])
                nums += 1
            self.slots.append(tmp)
        print(self.slots)
                
                
        
    def car_in(self, car_number, car_kind, car_color, cur_time):
        tmp = 0
        flag = False
        for j in range(self.col):
            for i in range(self.row):
                if self.slots[i][j][0] == False:
                    tmp = self.slots[i][j][1]
                    self.slots[i][j][0] = True
                    flag = True
                    break
            if flag:
                print("입차가 가능합니다.")
                car_name = Car(car_number, car_kind, car_color)
                break
        if not flag:
            print("만차인 관계로 이용이 불가합니다.")
            
        if flag:
            car_name.slot = tmp
            self.cars["class"].append(car_name)
            self.cars["number"].append(car_name.car_number)
            car_name.current_time = cur_time.copy()
            car_name.out_time = {"H" : cur_time["H"] + random.randint(0,1),
                                    "M" : cur_time["M"] + random.randint(0, 60)}
            if car_name.out_time["M"] >= 60:
                car_name.out_time["H"] += car_name.out_time["M"] // 60
                car_name.out_time["M"] = car_name.out_time["M"] % 60
            print(f"{car_name.car_number} : {car_name.car_kind} 입차 완료")

def make_number(parkinglot):
    hangul = ["가", "나", "다", "라", "마", "거", "너", "더", "러", "머", "버", "서", "어", "저", "고", "노", "도", "로", "모", "보", "소", "오", "조", "구", "누", "두", "루", "무", "부", "수", "우", "주", "바", "사", "아", "자", "배", "허", "하", "호"]
    number = ""
    number1 = ''
    for _ in range(3):
        number1 += str(random.randint(0,9))
    number2 = ''
    for _ in range(4):
        number2 += str(random.randint(0,9)) 
    number = number1 + hangul[random.randint(0, len(hangul)-1)] + number2
    while number in parkinglot.cars["number"]:
        number1 = ''
        for _ in range(3):
            number1 += str(random.randint(0,9))
        number2 = ''
        for _ in range(4):
            number2 += str(random.randint(0,9))
        number = number1 + hangul[random.randint(0, len(hangul)-1)] + number2
    return number
       
def solution():
    H = "H"
    M = "M"
    p = ParkingLot(4, 12)
    cur_time = {H : 0,
                M : 0,}
    kind_list = ["ST1", "그랜저", "아이오닉5/5N/6/9", "넥쏘", "팰리세이드", "베뉴", "스타리아", "싼타페", "쏘나타/디엣지", "쏠라티", "아반떼/N", "캐스퍼/EV", "코나/EV", "투싼", "포터2/EV", "K3(포르테)", "K5", "K8", "K9", "니로", "스포티지", "쏘렌토", "카니발", "EV3/5/6/9", "봉고", "셀토스", "스팅어", "모하비", "G70", "G80", "G90", "GV60", "GV70/EV", "GV80", "GV90", "봉고3", "마스터", "무쏘", "티볼리", "코란도", "익스토리", "XM3", "아르카나", "마스터", "컬리", "라노스", "트랙스", "트레일블레이저", "토스타", "콜로라도", "스파크", "A클래스", "B클래스", "C클래스", "E클래스", "S클래스", "CLA클래스", "GLA클래스", "GLB클래스", "GLC클래스", "GLE클래스", "GLS클래스", "EQS클래스", "EQE클래스", "G클래스", "V클래스", "2시리즈", "3시리즈", "5시리즈", "7시리즈", "8시리즈", "X1", "X2", "X3", "X4", "X5", "X6", "X7", "i4", "i5", "i7", "Z4", "미니쿠퍼", "미니클럽맨", "미니컨트리맨", "모델3", "모델Y", "모델S", "모델X", "사이버트럭", "고Golf", "ID.3", "ID.4", "ID.7", "티구안", "파사트", "아테온", "캠리", "RAV4", "하이랜더", "프리우스", "GR86", "랜드크루저" , 	"ES" , 	"NX" , 	"RX" , 	"LS" , 	"GX" , 	"LX" , 	"911" , "카이엔", "맥칸", "타이칸" , "파나메라" , "A3" , "A4" , "A6" , "A8" , "Q3" , "Q5" , "Q7" , "Q8"]
    color_list = ["White", "Black", "Silver", "Gray", "Blue", "Red", "Pearl White", "Navy Blue", "Green", "Orange", "Yellow", "Beige", "Brown", "Purple", "Teal", "Gold", "Ivory", "Olive", "Rose Gold", "Navy"]
    while True:
        intv = 0
        print(f"____________________현재 시간 : {cur_time[H]%24}시 {cur_time[M]}분____________________")
        will_out = []
        p.cars["class"].sort(key=lambda x: (x.out_time[H]*60 + x.out_time[M]))
        for car in p.cars["class"]:
            if car.out_time[H] < cur_time[H]:# if car.out_time[H] <= cur_time[H] and car.out_time[M] <= cur_time[M]:
                print(f"{car.car_number} : {car.car_kind} 출차 완료")
                print()
                print(f"주차 요금 : {(((car.out_time[H]-car.current_time[H])*60 + (car.out_time[M]-car.current_time[M])//10)) * 1000}원")
                print()
                p.slots.append(car.slot)
                will_out.append(car)
                print("_____내 차 정보_____")
                car.info()
                print()
                print("_____현재 주차장 상태_____")
                for car1 in p.cars["class"]:
                    if car1 in will_out:
                        continue
                    car1.info()
                    print()
                print()
            elif car.out_time[H] == cur_time[H] and car.out_time[M] <= cur_time[M]:
                print(f"{car.car_number} : {car.car_kind} 출차 완료")
                print()
                print(f"주차 요금 : {((((car.out_time[H]-car.current_time[H])*60 + (car.out_time[M]-car.current_time[M]))//10) * 1000) + 1000}원")
                print()
                p.slots.append(car.slot)
                will_out.append(car)
                print("_____내 차 정보_____")
                car.info()
                print()
                print("_____현재 주차장 상태_____")
                for car1 in p.cars["class"]:
                    if car1 in will_out:
                        continue
                    car1.info()
                    print()
                print()
        for car in will_out:
            p.cars["class"].remove(car)
            p.cars["number"].remove(car.car_number)
            
        if 6 <= cur_time[H] <= 22:
            intv = random.randint(10,20)
            cur_time[M] += intv
            if cur_time[M] >= 60:
                cur_time[H] += cur_time[M] // 60
                cur_time[M] = cur_time[M] % 60
            car_number = make_number(p)
            car_kind = kind_list[random.randint(0, len(kind_list)-1)]
            car_color = color_list[random.randint(0, len(color_list)-1)]
            p.car_in(car_number, car_kind, car_color, cur_time)
            print("_____현재 주차장 상태_____")
            for car in p.cars["class"]:
                car.info()
                print()
            print()
        else:
            intv = random.randint(40, 60)
            cur_time[M] += intv
            if cur_time[M] >= 60:
                cur_time[H] += cur_time[M] // 60
                cur_time[M] = cur_time[M] % 60
            car_number = make_number(p)
            car_kind = kind_list[random.randint(0, len(kind_list)-1)]
            car_color = color_list[random.randint(0, len(color_list)-1)]
            p.car_in(car_number, car_kind, car_color, cur_time)
            print("_____현재 주차장 상태_____")
            for car in p.cars["class"]:
                car.info()
                print()
            print()
        flag = input("프로그램 종료를 원하시면 quit을 입력해 주세요. 계속 진행하시려면 아무 키나 눌러주세요. : ")
        print()
        if flag == "quit":
                print("프로그램을 종료합니다.")
                break
solution()
        
# %%
