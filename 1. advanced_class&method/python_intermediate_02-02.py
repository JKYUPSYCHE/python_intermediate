# Chapter 02 - 02
# 객체 지향 프로그래밍 (OOP) ->  장점 : 코드의 재사용, 코드 중복 방지, 유지 보수가 쉽다. 등
# 규모가 큰 프로젝트 > 함수 중심이라면 > 데이터 방대 > 복잡
# 클래스 중심 > 데이터 중심 > 객체로 관리


class Car():
    '''
    Car class
    Author : Yoo
    Date : 2021.02.22
    '''

    # 클래스 변수 (실행 코드 : line 70) - 모든 인스턴스가 공유하는 변수
    car_count = 0


    def __init__(self, company, details):
        self._company = company
        self._details = details
        Car.car_count += 1  # 객체가 생성될 때마다 클래스변수가 하나씩 증가할 것.

    def __str__(self):  # 파이썬 내에 이미 있는 메소드. 매우 중요
        return 'str : {} - {}'.format(self._company, self._details)

    def __repr__(self): # __str__과 거의 비슷하지만, str은 사용자레벨, repr은 개발자 레벨에서 객체 정보를 인식하기 위한 문자열로 표기하기 위해 사용.
        return 'repr : {} - {}'.format(self._company, self._details)

    def __del__(self):
        Car.car_count -= 1

    def detail_info(self):
        print('Current ID : {}'.format(id(self)))
        print('Car Detail Info : {} {}'.format(self._company, self._details.get('price')))

car1 = Car('Ferrari', {'color': 'White', 'horsepower': 400, 'price': 8000})
car2 = Car('BMW', {'color': 'Black', 'horsepower': 270, 'price': 5000})
car3 = Car('Audi', {'color': 'Silver', 'horsepower': 300, 'price': 6000})

# ID 확인
print(id(car1))  # self가 갖는 고유의 값
print(id(car2))
print(id(car3))

print(car1._company == car2._company) # False
print(car1 is car2) # False : ID 값이 다르므로
# self 의 의미 : 클래스를 기반으로 생성된 인스턴스 내부의 자신을 나타내는 값을 저장하기 위한 예약어.

# dir & __dict__ 확인
print(dir(car1)) # 리스트 형식으로 모든 메소드들을 반환 (상위로부터 상속받는 것 까지)
print(dir(car2))

print()
print()

print(car1.__dict__)  # 인스턴스 안의 값들을 dict 형태로 보여줌
print(car2.__dict__)

# Doctring
print(Car.__doc__)
print()

# detail_info 메소드 실행
car1.detail_info()
car2.detail_info()
# 에러
# Car.detail_info() 이 경우 에러 : TypeError: detail_info() missing 1 required positional argument: 'self'
Car.detail_info(car1) # 이 경우 에러가 나지 않는다. self 인자를 직접 전달하여 호출하는 방법

# 비교
print(car1.__class__, car2.__class__)
print(id(car1.__class__), id(car2.__class__))  # Car class의 id를 출력한 것이므로 개별 객체의 id와 다르다.

# 클래스 변수 실행 (car_count)
print(car1.car_count)
print(car2.car_count)
print(car1.__dict__)
print(car2.__dict__)
print(dir(car1))

# 접근
print(car1.car_count)
print(Car.car_count)  # 모든 인스턴스가 공유하기 때문에 어떻게 접근하든 상관없지만, 클래스네임으로 접근하는 것이 일반적.

# 삭제
del car2
print(Car.car_count)

# 인스턴스 네임스페이스에 없으면 상위에서 자동으로 검색
# 즉, 동일한 이름으로 변수 생성 가능 - 인스턴스 검색 후 없다면, 상위(클래스 변수, 부모클래스 변수) 검색