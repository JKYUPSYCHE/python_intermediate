# Chapter 04 - 02 : 시퀀스 형
# 자료형의 종류
# 1. container : 서로다른 자료형을 담을 수 있음[list, tuple, collections.deque]
# 2. flat : 단일 자료형만 담을 수 있음[str, bytes, bytearray, array.array, memoryview]
# 가변형(mutable)[list, bytearray, array.array, memoryview, deque]
# 불변형(immutable)[tuple, str, bytes]
# Sequence란? : 순서가 있는 자료형

# 리스트 및 튜플 고급
# Tuple Advanced : Unpacking
# ex) b, a = a, b

print(divmod(100, 9))  # (몫, 나머지)
print(divmod(*(100, 9))) # (100, 9)를 unpacking 하여 전달
print(*(divmod(100, 9))) # divmod() 함수의 결과 튜플을 unpacking 하여 전달

print()

# x, y, rest = rang(10) : Error
x, y, *rest = range(10)  # 0부터 9까지 x y에 순서대로 넣고 나머지는 rest에 unpacking
print(x, y, rest)

x, y, *rest = range(2)
print(x, y, rest)

x, y, *rest = 1, 2, 3, 4, 5
print(x, y, rest)

print()
print()

# Mutable(가변) vs Immutable(불변)
l = (15, 20, 25) # tuple
m = [15, 20, 25] # list

print(l, id(l))
print(m, id(m))

l = l * 2
m = m * 2
print(l, id(l))
print(m, id(m))

l *= 2
m *= 2
print(l, id(l))
print(m, id(m))
# m *= 2 연산의 경우 id 값이 변하지 않는다. 가변형 자료구조이기 때문에 값이 변화하여 다시 저장되는 구조

print()
print()

# sort vs sorted
# reverse, key = len, key = set.lower, key = func...
# sorted : 정렬 후 새로운 객체로 반환 (원본이 수정되지 않음)
f_list = ['orange', 'apple', 'mango', 'papaya', 'lemon', 'strawberry', 'coconut']
print('sorted - ', sorted(f_list))
print('sorted - ', sorted(f_list, reverse=True)) # 역순 정렬
print('sorted - ', sorted(f_list, key=len))      # 길이 순 정렬 **key에는 사용자지정 함수도 사용 가능
print('sorted - ', sorted(f_list, key=lambda x: x[-1], reverse=True)) # lambda이용 예제 : 끝 글자의 알파벳 순, reverse를 적용하여 반대로
print('sorted - ', f_list)
print()

# sort : 정렬 후 객체를 직접 변경 (원본을 직접 수정)
# 반환 값 확인(None)
print('sort - ', f_list.sort(), f_list)
print('sort - ', f_list.sort(reverse=True), f_list)
print('sort - ', f_list.sort(key=len), f_list)
print('sort - ', f_list.sort(key=lambda x : x[-1]), f_list)
print('sort - ', f_list.sort(key=lambda x : x[-1], reverse=True), f_list)

# List vs Array 적합한 사용법 설명
# 리스트 기반 : 융통성, 다양한 자료형, 범용적 사용
# 숫자(array) 기반 : 배열(리스트와 거의 호환) - 딥러닝, 머신러닝 등 고속 연산이 필요한 경우.
