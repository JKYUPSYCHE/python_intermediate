# Chapter 05 - 03 : closure 심화
# 클로저 기초 : 외부에서 호출된 함수의 변수값 or 상태(레퍼런스) 복사 후 저장 -> 후에 접근 가능

# Closure 사용
def closure_ex1():
    # Free variable
    # 클로저 영역
    series = []
    def averager(v):
        series.append(v)
        print('inner >> {} / {}'.format(series, len(series)))
        return sum(series) / len(series)
    return averager # 함수자체를 return
# !여러 변수를 사용할 경우 클래스를 통해 구현하는 편이 좋다.

avg_closure1 = closure_ex1()

print(avg_closure1)
print(avg_closure1(10))  # 10.0
print(avg_closure1(30))  # 20.0
print(avg_closure1(50))  # 30.0

print()
print()
print()

# function inspection
print(dir(avg_closure1))
print(dir(avg_closure1.__code__))                # co_freevars, co_code, co_consts, ...?
print(avg_closure1.__code__.co_freevars)         # series
print(avg_closure1.__closure__[0].cell_contents) # [10, 30, 50]

# 잘못된 클로저 사용 예
def closure_ex2():
    # Free variable
    cnt = 0
    total = 0
    def averager(v):
        cnt += 1
        total += v
        return total / cnt
    return averager

avg_closure2 = closure_ex2()
# print(avg_closure2(10))  예외 발생 : UnboundLocalError: local variable 'cnt' referenced before assignment


# 해결
def closure_ex3():
    # Free variable
    cnt = 0
    total = 0
    def averager(v):
        nonlocal cnt, total # cnt, total을 free variable화
        cnt += 1
        total += v
        return total / cnt
    return averager

avg_closure3 = closure_ex3()
print(avg_closure3(15))  # 15.0
print(avg_closure3(35))  # 25.0
print(avg_closure3(45))  # 31.66666