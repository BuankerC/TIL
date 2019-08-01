20190802 test before

ex01

```python
# 파일명 및 함수명을 변경하지 마시오.
def positive_sum(numbers):
    """
    여기에 코드를 작성하시오.
    numbers는 숫자들이 담긴 리스트입니다.
    numbers에 담긴 숫자들 중, 양의 정수들의 합을 반환합니다.
    """
    sum = 0
    for number in numbers:
        if number > 0:
            sum += number
    return sum





# 실행 결과를 확인하기 위한 코드입니다. 수정하지 마시오.
if __name__ == '__main__':
    print(positive_sum([1, -4, 7, 12])) #=> 20
    print(positive_sum([-1, -2, -3, -4])) #=> 0
```

ex02-1

```python
# 파일명 및 함수명을 변경하지 마시오.
def calc(equation):
    """
    아래에 코드를 작성하시오.
    equation은 덧셈 뺄셈으로 이루어진 수식 문자열입니다.
    계산된 결과를 정수로 반환합니다.
    """
    return sum(list(map(int, ('0' + equation).replace('-', '+-').split('+'))))





# 실행 결과를 확인하기 위한 코드입니다. 수정하지 마시오.
if __name__ == '__main__':
    print(calc('123+2-124'))
    print(calc('-12+12-7979+9191'))
    print(calc('+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1'))
```

ex02

```python
# 파일명 및 함수명을 변경하지 마시오.
def calc(equation):
    """
    아래에 코드를 작성하시오.
    equation은 덧셈 뺄셈으로 이루어진 수식 문자열입니다.
    계산된 결과를 정수로 반환합니다.
    """
    result = 0
    part = '0'
    for equ in equation:
        if equ == '-' or equ == '+':
            part_int = int(part)
            result += part_int
            if equ == '-':
                part = '-'
            else:
                part = '+'
        else:
            part += equ
    part_int = int(part)
    result += part_int
    return result





# 실행 결과를 확인하기 위한 코드입니다. 수정하지 마시오.
if __name__ == '__main__':
    print(calc('123+2-124'))
    print(calc('-12+12-7979+9191'))
    print(calc('+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1'))
```

ex-03

```python
# 파일명을 변경하지 마시오.
# 아래에 클래스 Point와 Circle을 선언하시오.
class Point:
    x = 0
    y = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f'Point:({self.x}, {self.y})'
    



class Circle:
    r = 0

    def __init__(self, center, r):
        self.x = center.x
        self.y = center.y
        self.r = r

    def get_area(self): 
        return self.r * self.r * 3.14

    def get_perimeter(self):
        return self.r * 2 * 3.14

    def get_center(self):
        return (self.x, self.y)

    def __str__(self):
        return f'Circle:({self.x}, {self.y}), r:{self.r}'





# 실행 결과를 확인하기 위한 코드입니다. 수정하지 마시오.
if __name__ == '__main__':
    p1 = Point(0, 0)
    c1 = Circle(p1, 3)
    print(c1.get_area())
    print(c1.get_perimeter())
    print(c1.get_center())
    print(c1)
    p2 = Point(4, 5)
    c2 = Circle(p2, 1)
    print(c2.get_area())
    print(c2.get_perimeter())
    print(c2.get_center())
    print(c2)
```

