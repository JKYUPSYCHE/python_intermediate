# Chapter 03 - 03 : 파이썬 데이터 모델 추상화

# 객체 -> 파이썬의 데이터를 추상화
# 모든 객체 -> id, type -> value

# 일반적인 튜플
# 두 점사이의 거리를 튜플을 이용해 구하기
# sqrt((x1 - x2)^2 + (y1 - y2)^2)
pt1 = (1.0, 5.0) # 좋지 못한 코딩
pt2 = (2.5, 1.5)

from math import sqrt # math 모듈의 제곱근을 구하는 함수 import

l_length1 = sqrt((pt1[0] - pt2[0]) ** 2 + (pt1[1] - pt2[1]) ** 2) # index를 이용해 접근 하는 방식은 헷갈린다.
print(l_length1)

# 네임드 튜플 사용
from collections import namedtuple

# 네임드 튜플 선언 방법
Point = namedtuple('Point', 'x y') # 선언하는 방법은 여러가지
pt3 = Point(1.0, 5.0)
pt4 = Point(2.5, 1.5)
print(pt3, pt4) # Point(x=1.0, y=5.0) Point(x=2.5, y=1.5)
print(pt3[0])

l_length2 = sqrt((pt3.x - pt4.x) ** 2 + (pt3.y - pt4.y) ** 2) # index를 사용하는 방식보다 명시적.
print(l_length2)
print(l_length2 == l_length1)

# 네임드 튜플을 선언하는 다양한 방법
Point1 = namedtuple('Point', ['x', 'y']) # 리스트 형태로 선언
Point2 = namedtuple('Point', 'x, y')  # 콤마를 사용해 구분
Point3 = namedtuple('Point', 'x y')  # 스페이스를 사용해 구분
Point4 = namedtuple('Point', 'x y x class', rename=True) # Default = False -> 이 상황에서 Error 발생. 난수를 생성해 이름 생성

# 출력
print(Point1, Point2, Point3, Point4)

# Dict to Unpacking
temp_dict = {'x': 75, 'y': 55}

# 객체 생성
p1 = Point1(x=10, y=35)
p2 = Point2(20, 40)
p3 = Point3(y=20, x=40)
# rename test
p4 = Point4(10, 20, 30, 50)
# dictionary unpacking test
p5 = Point(**temp_dict) # dictionary 형태를 unpacking 하여 mapping

print()

print(p1)
print(p2)
print(p3)
print(p4)
print(p5)

# 사용
print(p1[0] + p2[1])
print(p1.x + p2.y)

# unpacking
x, y = p2
print(x, y)

# 유용한 네임드 튜플 메소드들
temp = [52, 38]
# _make() : list를 기반으로 새로운 객체를 생성
p4 = Point1._make(temp)
print(p4)

# _fields : 필드 네임 확인
print(p1._fields, p2._fields, p3._fields, p4._fields)

# _asdict() : OrderedDict 반환
print(p1._asdict())
print(p4._asdict())


# 실사용 실습
# class 당 20명, 4개의 class(A,B,C,D)
Classes = namedtuple('Classes', ['rank', 'number'])
# 그룹 리스트 선언
numbers = [str(n) for n in range(1, 21)] # 1부터 20까지의 문자열 형태의 리스트 생성
ranks = 'A B C D'.split() # 공백을 기준으로 split 하여 리스트화
print(numbers)
print(ranks)

# List Comprehension
students = [Classes(rank, number) for rank in ranks for number in numbers]
print(len(students))
print(students)

# List Comprehension을 좀 더 가독성 있게 만드는 법 - 위의 과정을 내부적으로 처리
students2 = [Classes(rank, number)
             for rank in 'A B C D'.split()
             for number in [str(n)
                            for n in range(1, 21)]]

# 출력
for s in students2:
    print(s)