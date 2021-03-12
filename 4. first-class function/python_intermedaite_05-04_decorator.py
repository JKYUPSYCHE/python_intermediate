# Chapter 05 - 04 : decorator

# 데코레이터(decorator)
# 장점
# 1. 중복 제거, 코드 간결, 공통 함수 작성
# 2. 로깅, 프레임워크, 유효성 체크 -> 공통 함수
# 3. 조합해서 사용하기 용이하다.

# 단점
# 1. 가독성이 떨어짐 (지나친 사용은 디버깅 과정이 힘들어질 수 있음)
# 2. 특정 기능에 한정된 함수는 단일 함수로 작성하는 편이 유리

# 예시
# @classmethod
# @staticmethod

# 데코레이터 실습 : 시간을 측정하는 데코레이터
import time

def perf_clock(func):
    def perf_clocked(*args):
        # 함수 시작 시간
        st = time.perf_counter()
        # 핵심! 함수 실행
        result = func(*args)
        # 함수 종료 시간
        et = time.perf_counter() - st
        # 실행 함수명
        name = func.__name__
        # 함수 매개변수 출력
        arg_str = ', '.join(repr(arg) for arg in args)
        # 결과 출력
        print('[%0.5fs] %s(%s) -> %r' % (et, name, arg_str, result))
        return result
    return perf_clocked

# 테스트용 함수 구현
@perf_clock  # 데코레이터 선언
def time_func(seconds):
    time.sleep(seconds)
@perf_clock
def sum_func(*numbers):
    return sum(numbers)

# 데코레이터 미사용시 프로세스
none_deco1 = perf_clock(time_func)
none_deco2 = perf_clock(sum_func)

print(none_deco1, none_deco1.__code__.co_freevars)
print(none_deco2, none_deco2.__code__.co_freevars)

print('-' * 40, 'Called None Decorator -> time_func')
print()
none_deco1(1.5)
print('-' * 40, 'Called None Decorator -> sum_func')
print()
none_deco2(100, 200, 300, 400, 500)

print()
print()

# 데코레이터 사용 - 데코레이터로 사용하고자 하는 함수 위에 @function
print('-' * 40, 'Called Decorator -> time_func')
print()
time_func(1.5)
print('-' * 40, 'Called Decorator -> sum_func')
print()
sum_func(100, 200, 300, 400, 500)

# 실행 결과
#<function perf_clock.<locals>.perf_clocked at 0x0170B2B0> ('func',)
#<function perf_clock.<locals>.perf_clocked at 0x0170B4A8> ('func',)
#---------------------------------------- Called None Decorator -> time_func
#
#[1.50105s] time_func(1.5) -> None
#[1.50137s] perf_clocked(1.5) -> None
#---------------------------------------- Called None Decorator -> sum_func
#
#[0.00002s] sum_func(100, 200, 300, 400, 500) -> 1500
#[0.00017s] perf_clocked(100, 200, 300, 400, 500) -> 1500
#
#
#---------------------------------------- Called Decorator -> time_func
#
#[1.50035s] time_func(1.5) -> None
#---------------------------------------- Called Decorator -> sum_func
#
#[0.00000s] sum_func(100, 200, 300, 400, 500) -> 1500

