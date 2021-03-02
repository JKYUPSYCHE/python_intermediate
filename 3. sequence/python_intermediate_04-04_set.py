# Chapter 04 - 04 : 시퀀스 형
# 해시테이블(hashtable) -> 적은 리소스로 많은 데이터를 효율적으로 관리
# Dict -> key 중복을 허용 X, Set -> 원소의 중복을 허용 X
# Dict 및 Set 심화

# immutable Dict 생성
from types import MappingProxyType
d = {'key1': 'value1'}
# 선언한 dict의 값이 변경되는 것을 원치 않을 때, 수정이 불가능한 dict 형태로 변경하는 방법
# Read Only
d_frozen = MappingProxyType(d)

print(d, id(d))
print(d_frozen, id(d_frozen))

# 수정 가능
d['key2'] = 'value2'
print(d)

# frozen 형태의 dict 수정?
# d_frozen['key2'] = 'value2' -> Error : TypeError: 'mappingproxy' object does not support item assignment

print()
print()


# Set 예제들
set1 = {'Apple', 'Orange', 'Apple', 'Orange', 'Kiwi'} # 중복을 허용하지 않기 때문에 중복되는 값은 생략
set2 = set(['Apple', 'Orange', 'Apple', 'Orange', 'Kiwi'])
set3 = {3}
set4 = {}                                             # 빈 중괄호 형태는 dict로 인식된다.
set5 = frozenset({'Apple', 'Orange', 'Apple', 'Orange', 'Kiwi'})

set1.add('Melon')
print(set1)

# 추가 불가
# set5.add('Melon') Error : AttributeError: 'frozenset' object has no attribute 'add'

print(set1, type(set1))
print(set2, type(set2))
print(set3, type(set3))
print(set4, type(set4))
print(set5, type(set5))

print()
print('-'* 30)

# 선언 최적화
# 바이트 코드 -> 파이썬 인터프리터가 바이트 코드를 실행
from dis import dis # 바이트 코드가 어떻게 실행되는 지 순서를 볼 수 있음
# set1의 선언과 set2의 선언 중 어떤것이 더 빠른가?
# 결론 : set 함수를 사용하는 것 보다 직접 선언하는 것이 조금 더 빠르기는 하다.

print(dis('{10}'))
print('-'* 30)
print(dis('set([10])'))
print('-'* 30)

# 지능형 집합(Comprehending Set)
from unicodedata import name
print({name(chr(i), '') for i in range(0, 256)})
