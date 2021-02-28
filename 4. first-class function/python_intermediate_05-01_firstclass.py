# Chapter 05 - 01 : python first-class function
# 함수형 프로그래밍의 장점 : 간결한 코드작성, 순수 함수를 지향하기에 여러 스레드에서 문제 없이 동작하는 프로그램을 작성 가능
# 일급 함수(일급 객체)
# 파이썬 함수의 특징
# 1. 런타임 초기화
# 2. 변수 할당 가능
# 3. 다른 함수의 인수로 전달 가능
# 4. 함수를 결과로 반환(return)

# 함수 객체
def factorial(n):
    '''
    Factorial Function
    :param n: int
    :return: n * (n-1) * (n-2) * ... * 1
    '''
    if n == 1: # n < 2
        return 1
    return n * factorial(n-1)  # 재귀함수

class A:
    pass

print(factorial(5))
print(factorial.__doc__)
print(type(factorial), type(A))
print(set(sorted(dir(factorial))) - set(sorted(dir(A))))  # 함수자체의 method만 반환
print(factorial.__name__)
print(factorial.__code__) # 코드의 내용과 파일의 위치를 출력

print()
print()

# 함수 자체를 변수에 할당
var_func = factorial
print(var_func)
print(var_func(10))  # factorial(10) load
print(list(map(var_func, range(1, 11)))) # 1부터 10까지 var_func에 mapping 하여 결과를 리스트화

# 함수 인수 전달 및 함수로 결과 반환 -> 고위 함수(Higher-order function)
# map, filter, reduce
print([var_func(i) for i in range(1, 6) if i % 2]) # 나머지가 있을 경우 True
print(list(map(var_func, filter(lambda x: x % 2, range(1, 6))))) # lambda 함수도 익명 함수의 일종으로 인수로 전달 가능.

print()
print()

# reduce 함수 사용 예제
from functools import reduce
from operator import add
# 1부터 10까지 정수의 합
print(sum(range(1, 11)))
print(reduce(add, range(1, 11))) # 리스트 안의 요소를 줄여가며 함수 실행

# 익명함수(lambda)
# 익명함수 사용시에는 주석 작성을 권장.
# 또한 가급적 직접 함수 작성을 권장.
# 일반 함수 형태로 리팩토링 권장
print(reduce(lambda x, t: x + t, range(1, 11)))

print()
print()

# Callable : 호출 연산자 -> 메소드 형태로 호출 가능한지 확인
# 호출 가능 확인 : True or False
print(callable(str))  # True
print(callable(A))    # True
print(callable(3.14)) # False -> float 형태이기 때문에 호출 불가능

# partial 사용법 : 인수 고정. 주로 콜백 함수에 사용
from operator import mul
from functools import partial

print(mul(10, 10))
# 인수 고정
five = partial(mul, 5)  # mul 함수의 첫번째 인수를 5로 고정.
six = partial(five, 6)  # 고정 추가
print(five(10))         # mul(*5, 10) = 50
print(six())            # mul(*5, *6) = 60
print([five(i) for i in range(1, 11)])
print(list(map(five, range(1, 11))))