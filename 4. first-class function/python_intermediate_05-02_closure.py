# Chapter 05 - 02 : closure의 개념 이해

# 중요!
# 파이썬의 변수 범위(scope)
# EX 1
def func_v1(a):
    print(a)
    print(b)

# func_v1(10) NameError: name 'b' is not defined

# EX 2
b = 20

def func_v2(a):
    print(a)
    print(b)

func_v2(10)

# EX 3
c = 30
def func_v3(a):
    global c
    print(a)
    print(c)
    c = 40       # global c를 40으로 치환

print('>>', c)   # 함수 실행 전의 c(30)를 출력
func_v3(10)
print('>>>', c)  # 함수 실행 후 치환된 c(40)를 출력

print()
print()

# Closure(클로저)를 사용하는 이유
# 서버 프로그래밍등에서 동시성(Concurrency) 제어 -> 한정된 메모리 공간에 여러 자원이 접근 -> 교착상태(Dead Lock)
# 메모리를 공유하지 않고 메세지 전달로 처리하기 위한 Erlang
# 공유하되 변경되지 않는(Immutable, Read Only) 적극적으로 사용 -> 함수형 프로그래밍과 연관
# 불변자료구조 및 atom, STM -> 멀티스레드(Coroutine) 프로그래밍에 강점
# '불변 상태를 기억한다' -- 상태를 책갈피?

a = 100
print(a + 100)
print(a + 1000)

# 결과를 누적하려면
print(sum(range(1, 51)))

# 클래스를 이용
class Averager():  # 누적되는 값의 평균을 구하는 class
    def __init__(self):
        self._series = []

    def __call__ (self, v): # 클래스를 함수처럽 호출 할 수 있도록 하는 method
        self._series.append(v)
        print('inner >> {} / {}'.format(self._series, len(self._series)))
        return sum(self._series) / len(self._series)

# 인스턴스 생성
averager_cls = Averager()

# 누적
print(averager_cls(10)) # inner >> [10] / 1 : 10.0
print(averager_cls(30)) # inner >> [10, 30] / 2 : 20.0
print(averager_cls(50)) # inner >> [10, 30, 50] / 3 : 50
