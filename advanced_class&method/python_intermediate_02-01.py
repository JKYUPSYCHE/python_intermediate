# Chapter 02 - 01
# 객체 지향 프로그래밍 (OOP) ->  장점 : 코드의 재사용, 코드 중복 방지, 유지 보수가 쉽다. 등
# 규모가 큰 프로젝트 > 함수 중심이라면 > 데이터 방대 > 복잡
# 클래스 중심 > 데이터 중심 > 객체로 관리

# 일반적인 코딩
# 차량1
car_company_1 = 'Ferrari'
car_detail_1 = [
    {'color': 'White'},
    {'horsepower': 400},
    {'price': 8000}
]

# 차량2
car_company_2 = 'BMW'
car_detail_2 = [
    {'color': 'Black'},
    {'horsepower': 270},
    {'price': 5000}
]

# 차량3
car_company_3 = 'Audi'
car_detail_3 = [
    {'color': 'Silver'},
    {'horsepower': 300},
    {'price': 6000}
]
# 번거롭다.

# 리스트 구조로 코딩
car_company_list = ['Ferrari', 'BMW', 'Audi']
car_detail_list = [
    {'color': 'White', 'horsepower': 400, 'price': 8000},
    {'color': 'Black', 'horsepower': 270, 'price': 5000},
    {'color': 'Silver', 'horsepower': 300, 'price': 6000}
]
# 관리가 어렵다. 인덱스로 접근해야 하는 불편함. 삭제가 불편하다.
# 인덱스를 관리하는 함수가 따료 필요하다.

del car_company_list[1]
del car_detail_list[1]

print(car_company_list)
print(car_detail_list)

print()
print()


# 딕셔너리 구조  > 중요! 아직까지 많이 사용하는 구조
# 코드 반복 문제 지속, 키(key) 중첩 문제

car_dicts = [
    {'car_company': 'Ferrari', 'car_detail': {'color': 'White', 'horsepower': 400, 'price': 8000}},
    {'car_company': 'BMW', 'car_detail': {'color': 'Black', 'horsepower': 270, 'price': 5000}},
    {'car_company': 'Audi', 'car_detail': {'color': 'Silver', 'horsepower': 300, 'price': 6000}}
]

del car_dicts[1]
print(car_dicts)

print()
print()

# 클래스 구조
# 인스턴스 구조 설계 후 재사용 증가, 코드 반복 최소화, 메소드를 활용한

class Car():
    def __init__(self, company, details):
        self._company = company
        self._details = details

    def __str__(self):  # 파이썬 내에 이미 있는 메소드. 매우 중요
        return 'str : {} - {}'.format(self._company, self._details)

    def __repr__(self): # __str__과 거의 비슷하지만, str은 사용자레벨, repr은 개발자 레벨에서 객체 정보를 인식하기 위한 문자열로 표기하기 위해 사용.
        return 'repr : {} - {}'.format(self._company, self._details)


car1 = Car('Ferrari', {'color': 'White', 'horsepower': 400, 'price': 8000})
car2 = Car('BMW', {'color': 'Black', 'horsepower': 270, 'price': 5000})
car3 = Car('Audi', {'color': 'Silver', 'horsepower': 300, 'price': 6000})

print(car1) # 주소값을 출력. __str__ 메소드를 구현하면 정상적으로 출력
print(car2)
print(car3)

print(car1.__dict__)  # 클래스 안에 어떤 속성이 들어있는지 확인 할 수 있는 메소드
print(car2.__dict__)
print(car3.__dict__)

# print(dir(car1)) 클래스 내의 구현된 메소들를 확인 할 수 있음.

print()
print()

# 리스트 선언
car_list = []

car_list.append(car1)
car_list.append(car2)
car_list.append(car3)

print(car_list)  # 리스트 안의 객체일 경우 repr 메소드를 호출

print()
print()

# 반복(__str__)
for x in car_list:
    print(repr(x))