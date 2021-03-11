# Chapter 06 - 01
# 병행성(Concurrency)
# Iterator, Generator

# 파이썬 반복 가능한 타입 : iterable
# collections, text file, list, Dict, Set, Tuple, unpacking, *args, ... -> Iterable

t = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
print(dir(t))
# iterable 하기 때문에 반복이 가능하다.
for c in t:
    print('>', c)
# 반복 가능한 이유? -> iter(x) 함수 호출 가능

print('-' * 30)

# while 문의 경우
w = iter(t)

while True:
    try:
        print(next(w))
    except StopIteration:
        break
print()

# iterable을 확인하는 방법

# 1. dir 을 통해 확인하는 방법

# 2. hasattr 함수 사용
print(hasattr(t, '__iter__'))  # iterable 하다면 True를 반환

# 3.
from collections import abc
print(isinstance(t, abc.Iterable)) # True

print()
print()

# 클래스 기반 제너레이터 구현
# next pattern 으로 word splitter 구현
class WordSplitter:
    def __init__(self, text):
        self._idx = 0
        self._text = text.split(' ') # 공백으로 구분

    def __next__(self):
        try:                         # 예외처리
            word = self._text[self._idx]
        except IndexError:
            raise StopIteration('Stopped Iteration')
        self._idx += 1
        return word

    def __repr__(self):
        return 'WordSplit({})'.format(self._text)

# 사용
w1 = WordSplitter('Do today what you could do tommorrow')
print(w1)
print(next(w1))

# Generator pattern
# 1. 지능형 리스트, 딕셔너리, 집합등에 유용 -> 데이터 양이 증가하면 메모리 사용량이 증가하기 때문에 generator 사용이 권장된다.
# 2. 단위 실행 가능한 코루틴 구현과 연동
# 3. 작은 메모리 조각 사용

class WordSplitGenerator:
    def __init__(self, text):
        self._text = text.split(' ')

    def __iter__(self):         # 내부적으로 예외처리까지 가능
        for word in self._text:
            yield  word         # generator  !yield에 대해서는 다음 시간에!
        return                  # return 하지 않아도 된다.

    def __repr__(self):
        return 'WordSplitGenerator({})'.format(self._text)

wg = WordSplitGenerator('Do today what you could do tommorrow')

wt = iter(wg)

print(wt, wg)
print(next(wt))
print(next(wt))
print(next(wt))