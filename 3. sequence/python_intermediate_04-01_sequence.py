# Chapter 04 - 01 : 시퀀스 형
# 자료형의 종류
# 1. container : 서로다른 자료형을 담을 수 있음[list, tuple, collections.deque]
# 2. flat : 단일 자료형만 담을 수 있음[str, bytes, bytearray, array.array, memoryview]
# 가변형(mutable)[list, bytearray, array.array, memoryview, deque]
# 불변형(immutable)[tuple, str, bytes]
# Sequence란? : 순서가 있는 자료형

# 리스트 및 튜플 고급
# 지능형 리스트(Comprehending List)
chars = '+_)(*&^%$#@!)' # flat 이면서 immutable
# char[2] = 2 : Error -> immutable 이기 때문에
code_list1 = []

for s in chars:
    code_list1.append(ord(s))  # chars의 unicode를 code_list1에 append.

print(code_list1)

# Comprehending List 단순화
code_list2 = [ord(s) for s in chars]  # append 연산보다 미세하게 빠르다.
print(code_list2)

# Comprehending List + Map, Filter
code_list3 = [ord(s) for s in chars if ord(s) > 40] # filtering
print(code_list3)

code_list4 = list(filter(lambda x : x > 40, map(ord, chars))) # lambda를 이용해 mapping 후 filtering
print(code_list4)

print([chr(s) for s in code_list1])
print([chr(s) for s in code_list2])
print([chr(s) for s in code_list3])
print([chr(s) for s in code_list4])

print()
print()

# Generator 생성
# Generator : 한 번에 한 개의 항목을 생성(메모리 유지 X)
import array

tuple_g = (ord(s) for s in chars)
array_g = array.array('I', (ord(s) for s in chars))

print(tuple_g)  # 값이 출력되지 않음
print(next(tuple_g))

print(array_g)
print(type(array_g))
print(array_g.tolist())

# 제네레이터 예제
print(('%s' % c + str(n) for c in 'A B C D'.split() for n in range(1, 21)))

for s in ('%s' % c + str(n) for c in 'A B C D'.split() for n in range(1, 21)):
    print(s)

# 리스트 주의점
# 얕은 복사와 깊은 복사 - reference 참고

marks1 = [['~'] * 3 for _ in range(4)] # 언더바(_) 반복은 하지만 사용하지는 않을 변수를 쓸 때 언더바를 사용해 생략
marks2 = [['~'] * 3] * 4

print(marks1)
print(marks2)

print()

# 수정할 때
print('수정 시 문제점')
marks1[0][1] = 'X'
marks2[0][1] = 'X'
print(marks1)
print(marks2)
# 같은 결과물의 리스트지만 수정 시 id가 어떻게 복사되었냐에 따라 다른 결과물을 가져온다.

# 증명
print([id(i) for i in marks1])
print([id(i) for i in marks2])  # marks2의 id는 한번 생성된 아이디를 복사하는 구조.