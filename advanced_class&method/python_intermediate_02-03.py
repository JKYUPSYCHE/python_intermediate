# Chapter 02 - 03 Class method & static method
# 객체 지향 프로그래밍 (OOP) ->  장점 : 코드의 재사용, 코드 중복 방지, 유지 보수가 쉽다. 등
# 규모가 큰 프로젝트 > 함수 중심이라면 > 데이터 방대 > 복잡
# 클래스 중심 > 데이터 중심 > 객체로 관리

class Car():
    '''
    Car class
    Author : Yoo
    Date : 2021.02.22-2
    Description : Class, Static, Instance Method
    '''

    # 클래스 변수 (실행 코드 : line 70) - 모든 인스턴스가 공유하는 변수
    price_per_raise = 1.0

    def __init__(self, company, details):
        self._company = company
        self._details = details

    def __str__(self):  # 파이썬 내에 이미 있는 메소드. 매우 중요
        return 'str : {} - {}'.format(self._company, self._details)

    def __repr__(self): # __str__과 거의 비슷하지만, str은 사용자레벨, repr은 개발자 레벨에서 객체 정보를 인식하기 위한 문자열로 표기하기 위해 사용.
        return 'repr : {} - {}'.format(self._company, self._details)

    # Instance Method (Self 인자를 사용하는 Method)
    # Self : 객체의 고유한 속성 값을 사용한다.

    def detail_info(self):
        print('Current ID : {}'.format(id(self)))
        print('Car Detail Info : {} {}'.format(self._company, self._details.get('price')))

    # Instance Method
    def get_price(self):
        return 'Before Car Price -> company : {}, price : {}'.format(self._company, self._details.get('price'))

    def get_price_culc(self):
        return 'After Car Price -> company : {}, price : {}'.format(self._company, self._details.get('price') * Car.price_per_raise)

    # class method
    @classmethod  # class method의 첫번째 인자는 cls (클래스 버전의 self (class -> cls))
    def raise_price(cls, per):
        if per <= 1:
            print('Please Enter 1 or More')
            return
        cls.price_per_raise = per
        print('Succeded! price has been raised')

    # static method
    @staticmethod
    def is_bmw(inst):
        if inst._company == 'BMW':
            return 'OK! This car is {}'.format(inst._company)
        return 'Sorry.. This car is not BMW'


car1 = Car('Ferrari', {'color': 'White', 'horsepower': 400, 'price': 8000})
car2 = Car('BMW', {'color': 'Black', 'horsepower': 270, 'price': 5000})

# 전체정보
car1.detail_info()
car2.detail_info()

# 가격정보 (직접접근)
print(car1._details.get('price'))
print(car2._details.get('price'))  # 이 방법은 별로 좋지 못한 접근 방법이다. Method를 만들어 접근하는 것이 좋음

# Instance Method를 통해 가격정보 접근
print(car1.get_price())
print(car2.get_price())

# 가격 인상(클래스 메소드 미사용) 후 가격 출력
Car.price_per_raise = 1.4  # 클래스 변수를 직접 접근하는 것도 좋은 방법은 아니다.
print(car1.get_price_culc())
print(car2.get_price_culc())

# class method를 통해 접근하여 가격 인상
Car.raise_price(1.86)
print(car1.get_price_culc())
print(car2.get_price_culc())


print()
print()

# 인스턴스로 static method 호출
print(car1.is_bmw(car1))
print(car2.is_bmw(car2))

# 클래스로 static method 호출
print(Car.is_bmw(car2)) # 호출이 유연함