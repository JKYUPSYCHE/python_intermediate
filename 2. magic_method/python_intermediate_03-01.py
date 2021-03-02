# Chapter 03 - 01 : Magic method(Special Method)
# 파이썬의 핵심!! 1. 시퀀스(Sequence) 2. 반복(Iterator) 3. 함수(Function) 4. 클래스(Class)
# Magic method : 클래스안에 정의할 수 있는 특별한(bult - in) 메소드

# 기본형
print('기본형')
print(int)
print(float)

# 모든 속성 및 메소드 출력
print('모든 메소드 출력')
print(dir(int))
print(dir(float))

n = 10
print(type(n))

print(n + 100)   # __add__ 을 호출하는 방식
print(n.__add__(100)) # 위의 코드와 같은 호출 방식
# print(n.__doc__)
print(n.__bool__(), bool(n)) # 같은 결과를 출력
print(n * 100, n.__mul__(100))

print()
print()

# 클래스 예제 1
class Fruit:
    def __init__(self, name, price):
        self._name = name
        self._price = price

    def __str__(self):
        return 'Fruit Class info : {}, {}'.format(self._name, self._price)


    # 덧셈 연산을 하는 magic method
    def __add__(self, other):
        print('__add__ has been called')
        return self._price + other._price

    # 뺄셈 연산을 하는 magice method
    def __sub__(self, other):
        print('__sub__ has been called')
        return self._price - other._price

    # 대소비교를 하는 magic method1 (self가 더 작을 때)
    def __le__(self, other):
        print('__le__ has been called')
        if self._price <= other._price:
            return True
        else:
            return False

    # 대소비교를 하는 magic method2 (self가 더 클 때)
    def __ge__(self, other):
        print('__ge__ has been called')
        if self._price >= other._price:
            return True
        else:
            return False

# 인스턴스 생성
s1 = Fruit('Orange', 7500)
s2 = Fruit('Banana', 3000)

# magic method를 모를 때 덧셈 연산
# print(s1._price + s2._price)  >> 코드가 복잡하고 비효율적인 코딩.
# 우리는 이미 클래스 내부에 magice method를 구현해 두었다.
print(s1 + s2) # __add__ method를 호출.

# 구현한 magic method 호출
print(s1 >= s2)  # ge
print(s1 <= s2)  # le
print(s1 - s2)   # sub
print(s2 - s1)   # sub
print(s1)        # str