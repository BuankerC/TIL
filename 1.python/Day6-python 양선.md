# 2019-07-22

## 모듈

### import

- 모듈을 활용하기  위해서는 반드시 import문을 통해 내장 모듈을 이름 공간으로 가져와야 합니다.

  ```python
  import fibo
  print(dir(fibo))
  print(fibo.fib(5))
  print(fibo.fib_loop(10))
  ```

  

### 패키지

- 패키지는 '점으로 구분된 모듈 이름'을 써서 파이썬의 모듈 이름 공간을 구조화하는 방법입니다. 예를 들어, 모듈 이름 myPackage.math는 myPackage라는 이름의 패키지에 있는 math라는 이름의 서브 모듈을 가리킵니다.
- 단, 파이썬이 디렉터리를 패키지로 취급하게 만들기 위해서  __init__.py 파일이 필요합니다. 이렇게 하는 이유 는 string처럼 흔히 쓰는 이름의 디렉터리가 의도하지 않게 모듈 검색 경로의 뒤에 등장하는 올바른 모듈들을 가리는 일을 방지하기 위함입니다.

