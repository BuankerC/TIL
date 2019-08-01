2019-07-29 과목평가 다시보기



1. 파이썬에서 제공하는 빌트인 함수가 아닌것은? sqrt()

2. 시퀀스 자료형의 특징이 아닌 것은? 기본적으로 정렬이 되어 있지만, 사용자 임의대로 순서를 변경할 수 있다. (정렬이 아니라 순서가 정해져 있음)

3. 보기의 파이썬 코드를 시행 했을때 결과는?

   ```python
   names = ['John', 'Ron', 'James', 'Betty']
   print(name[-2][-2])
   ```

   답: e

4. p3. population 출력시 나오는 값? 답: 3

   ```python
   class Person"
   	population = 0
       
       def __init__(self, name):
           self.name = name
           Person.population += 1
           
    p1 = population('kang')
    p2 = population('kim')
    p3 = population('ko')
   
           
   ```

   

5. ```python
   def func(c, b, a):
       return a*b+c
   
   print(func(2, 5, 4))
   ```

   답: 22

6. ```python
   print({'a : apple'})
   ```

   답: dict

7. 함수에 대한 설명으로 옳지 않는 것은?

   답: 함수에서 return을 작성하지 않으면 코드 실행 시 오류가 발생한다.(리턴 미작성시 None값을 반환)

8. 다섯 개의 정수 0을 가진 리스트를 만드는 방법 중 틀린 것은?

   ```python
   numbers = []
   numbers.append(0*5)
   ```

   

9. ```python
   s = 'hello my name is ssafy'
   for i in s:
       if i in s:
           if == 'm'
           print(s)
   ```

   답: hello my name is ssafy hello my name is ssafy

10. ```python
    d1 = {'d': dict()}
    d2 = dict(d={})
    ```

    코드 실행 시 다음 중 옳은 것은?

    답: d1의 value와 d2의 value는 모두 비어있는 딕셔너리다.

11. ```python
    fruits = {'apple': '사과', 'banana': '바나나'}
    a = fruits.get('apple')
    b = fruits.get('cherry')
    c = fruits.get('melon', True)
    d = {a:b}
    if c:
        print(d)
    ```

​      코드 실행시 다음 중 옳은 것?

​	답: b는 None이다.

12. ```python
    def func(c=5, *args):
        a, c, b = args
        return a + b + c
    print(func('3','4','1','2'))
    
    # func('3',('4','1','2'))
    # a, c, b = (4, 1, 2)
    # return a + b + c
    # 421
    ```

    다음 코드 실행 시 출력되는 결과는?

    답 : 421

13. 

    ```python
    name = 'hong'
    
    class Person:
        name = 'choi'
        def greeting(self):
            print(name)
    p1 = Person()
    p1.name = 'kim'
    p1.greeting()
    ```

    다음 코드 실행 시 출력되는 결과는?

    답:  hong

14. ```python
    my_int = 3
    ```

    보기의 my_int가 정수형인지 확인하는 방법 중 맞는 것은?

    답 : type(my_int) == int

15. ```python
    class Person:
        def __init__(self, name, age):
            self.name = name
    ```

    보기의 코드를 작성한 후 인스턴스를 만들려고 한다. 다음 중 옳은 것은?

    ```python
    p3 = Person(age=3, name='kang')
    ```

    

16. ```python
    word = 'python'
    indexing = word[3:8]
    print(indexing)
    ```

    답: hon

17. ```python
    def my_sum(a,b):
        c = a + b
        print(c)
        
    result = my_sum(5, 8)
    ```

    답: None

18. ```python
    string = 'I am hungry'
    result = ""
    for idx, value in enumerate(string):
        if idx % 2:
            result += value.upper()
        else:
            result += value
    print(result)        
    ```

    답 2번

19. ```python
    d = {'a':1, 'b':2}
    a1 = d.update(c=3)
    a2 = a1
    ```

    코드 실행 시 다음 중 옳은 것은? 보기중에는 답이 없다.

20. ```python
    def func(a, b=1, c=2, *args, **kwargs):
        d = sum([n*2 for n in args if n > 2])
        e = sum([v*v for k, v in kwargs.items()])
        return a + b + c + d + e
    
    print(func(9, 4, 2, 3, 1, 7, d=3,e=6))
    ```

    코드 실행시 출력 되는 결과?

    ```python
    func(9, 4, 2, (3, 1, 7), {d=3, e=6})
    
    #80
    ```

    

21. ```python
    def fib(n):
        if n == 0 or n == 1:
            return 1
        else:
            return fib(n-1) + fib(n-2)
        
    print(fib(4))
    ```

    코드 실행시 fib(1)과 fib(0)이 호출되는 횟수? 3회, 2회

22. ```python
    a = 1
    def func_1():
        a = 5
        func_2()
        
    def func_2():
        print(a, end="")
    func_1()
    print(a)
    ```

    코드 실행 시 나오는 답?

    11

23. ```python
    import copy
    
    list1 = [3, 'a', 'b']
    list2 = [1, 2, list1]
    
    list3 = list1[:]
    list4 = copy.copy(list2)
    list5 = copy.deepcopy(list2)
    ```

    다음 코드 실행 시 틀린 것은?

    답: list4[2] = 5 print(list2[2])의 결과는 5이다.

24. 