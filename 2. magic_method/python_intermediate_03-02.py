# Chapter 03 - 02 : Magic method(Special Method)
# 파이썬의 핵심!! 1. 시퀀스(Sequence) 2. 반복(Iterator) 3. 함수(Function) 4. 클래스(Class)
# Magic method : 클래스안에 정의할 수 있는 특별한(bult - in) 메소드

# 클래스 예제 2 : 벡터연산
# (5,2) + (4, 3) = (9, 5) : __add__
# (10, 3) * 5 = (50, 15)  : __mul__
# Max((5, 10)) = 10       : __bool__

class Vector(object):
    def __init__(self, *args):
        '''Create a Vector, example : v = Vector(5, 10)'''
        if len(args) == 0:
            self._x, self._y = 0, 0
        else:
            self._x, self._y = args  # 언패킹을 이용하여

    def __repr__(self):
        '''Return the Vector informations.'''
        return 'Vector(%r, %r)' % (self._x, self._y)

    def __add__(self, other):
        '''Return the vector addition of self and other'''
        return Vector(self._x + other._x, self._y + other._y)

    def __mul__(self, scalar):
        return Vector(self._x * scalar, self._y * scalar)

    def __bool__(self):
        return bool(max(self._x, self._y))


# Vector Instance 생성
v1 = Vector(5, 7)
v2 = Vector(23, 35)
v3 = Vector()

# 매직메소드 출력
print(Vector.__init__.__doc__)
print(Vector.__repr__.__doc__)
print(Vector.__add__.__doc__)

print(v1, v2, v3)
print(v1 + v2)
print(v1 * 3)
print(v2 * 10)
print(bool(v1), bool(v2), bool(v3))