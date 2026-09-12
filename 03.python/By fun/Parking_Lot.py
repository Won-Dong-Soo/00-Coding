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
        print(f"차량 번호 : {self.car_number}, \n차량 종류 : {self.car_kind}, 차량 색상 : {self.car_color}, 차량 위치 : {self.slot}, 입차 시간 : {self.current_time}, 출차 시간 : {self.out_time}")

class ParkingLot:
    def __init__(self, space):
        self.space = space
        self.cars = []
        self.slots = [i for i in range(1, space + 1)]
        
    def car_in(self, car_number, car_kind, car_color, cur_time):
        if len(self.cars) < self.space:
            print("입차가 가능합니다.")
            car_name = Car(car_number, car_kind, car_color)
            car_name.slot = self.slots[random.randint(0, len(self.slots) - 1)]
            self.cars.append(car_name)
            car_name.current_time = cur_time.copy()
            car_name.out_time = {"H" : cur_time["H"] + random.randint(0,1),
                                 "M" : cur_time["M"] + random.randint(0, 60)}
            if car_name.out_time["M"] >= 60:
                car_name.out_time["H"] += car_name.out_time["M"] // 60
                car_name.out_time["M"] = car_name.out_time["M"] % 60
            print(f"{car_name.car_kind}-{car_name.car_number} 입차 완료")
        else:
            print("만차인 관계로 이용이 불가합니다.")
    
def solution():
    H = "H"
    M = "M"
    p = ParkingLot(50)
    cur_time = {H : 0,
                M : 0,}
    while True:
        intv = 0
        if 6 <= cur_time[H] <= 22:
            intv = random.randint(10,20)
            cur_time[M] += intv
            if cur_time[M] >= 60:
                cur_time[H] += cur_time[M] // 60
                cur_time[M] = cur_time[M] % 60
            car_number = input("차량 번호를 입력하세요(만약 프로그램 종료를 원한다면 quit을 입력해 주세요.) : ")
            print()
            if car_number == "quit":
                print("프로그램을 종료합니다.")
                break
            car_kind = input("차량 종류를 입력하세요 : ")
            print()
            car_color = input("차량 색상을 입력하세요 : ")
            print()
            p.car_in(car_number, car_kind, car_color, cur_time)
            for car in p.cars:
                car.info()
                print()
            print()
        else:
            intv = random.randint(40, 60)
            cur_time[M] += intv
            if cur_time[M] >= 60:
                cur_time[H] += cur_time[M] // 60
                cur_time[M] = cur_time[M] % 60
            car_number = input("차량 번호를 입력하세요(만약 프로그램 종료를 원한다면 quit을 입력해 주세요.) : ")
            print()
            if car_number == "quit":
                print("프로그램을 종료합니다.")
                print()
                break
            car_kind = input("차량 종류를 입력하세요 : ")
            print()
            car_color = input("차량 색상을 입력하세요 : ")
            print()
            p.car_in(car_number, car_kind, car_color, cur_time)
            for car in p.cars:
                car.info()
                print()
            print()
            
        if cur_time[H] >= 24:
                cur_time[H] = cur_time[H] % 24
        for car in p.cars:
            if car.out_time[H] <= cur_time[H] and car.out_time[M] <= cur_time[M]:
                print(f"{car.car_number}-{car.car_kind} 출차 완료")
                print()
                print(f"주차 요금 : {(((car.out_time[H]-car.current_time[H])*60 + (car.out_time[M]-car.current_time[M])//10)) * 1000}원")
                print()
                p.cars.remove(car)
                print(p.cars)
                print()

solution()
        