# Chapter 04 - 03 : 시퀀스 형
# 자료형의 종류
# 1. container : 서로다른 자료형을 담을 수 있음[list, tuple, collections.deque]
# 2. flat : 단일 자료형만 담을 수 있음[str, bytes, bytearray, array.array, memoryview]
# 가변형(mutable)[list, bytearray, array.array, memoryview, deque]
# 불변형(immutable)[tuple, str, bytes]
# Sequence란? : 순서가 있는 자료형

# 해시테이블 : key에 value를 저장하는 구조
# python에서는 dictionary 형태가 해시테이블의 예
# !!!키 값의 연산 결과에 따라 직접 접근이 가능한 구조!!!
# key 값을 해싱 함수 -> 해시 주소 -> key에 대한 value를 참조

# Dict 구조
# print(__builtins__.__dict__)

# Hash 값을 확인한다. -> 고유 값을 확인한다.
t1 = (10, 20, (30, 40, 50))
t2 = (10, 20, [30, 40, 50])
print(hash(t1))
# print(hash(t2)) : Error -> mutable한 list가 값으로 들어가 있기 대문에 hash 값을 가져올 수 없음.
print()
print()

# Dict Setdefault 사용 예제
source = (('k1', 'val1'),
          ('k1', 'val2'),
          ('k2', 'val3'),
          ('k2', 'val4'),
          ('k2', 'val5'))

new_dict1 = {}
new_dict2 = {}
new_dict3 = {}

# No use Setdefault
for k, v in source:
    if k in new_dict1:
        new_dict1[k].append(v)
    else:
        new_dict1[k] = [v]

print(new_dict1)


# Use Setdefault
for k, v in source:
    new_dict2.setdefault(k, []).append(v)   # default 값을 설정 후 v를 append 한다.

print(new_dict2)

# 주의
new_dict3 = {k: v for k, v in source}

print(new_dict3)