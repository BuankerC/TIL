# OOP advanced

## 클래스 변수 / 인스턴스 변수

### 클래스 변수

```python
class TestClass:
      class_variable = '클래스변수'
      ...

  TestClass.class_variable  # '클래스변수'
  TestClass.class_variable = 'class variable'
  TestClass.class_variable  # 'class variable'

  tc = TestClass()
  tc.class_variable  # 인스턴스 => 클래스 => 전역 순서로 네임스페이스를 탐
```



### 인스턴스 변수

```python
class TestClass:
      def __init__(self, arg1, arg2):
          self.instance_var1 = arg1
          self.instance_var2 = arg2

      def status(self):
          return self.instance_var1, self.instance_var2   

  tc = TestClass(1, 2)
  tc.instance_var1  # 1
  tc.instance_var2  # 2
  tc.status()  # (1, 2)
```



## 인스턴스 메서드 / 클래스 메서드 / 스태틱(정적) 메서드

### 인스턴스 메서드

- 인스턴스가 사용할 메서드 입니다.

- **정의 위에 어떠한 데코레이터도 없으면, 자동으로 인스턴스 메서드가 됩니다.**

- **첫 번째 인자로 self 를 받도록 정의합니다. 이 때, 자동으로 인스턴스 객체가 self 가 됩니다.**

  ```python
  class MyClass:
        def instance_method_name(self, arg1, arg2, ...):
            ...
  
    my_instance = MyClass()
    my_instance.instance_method_name(.., ..)  # 자동으로 첫 번째 인자로 인스턴스(my_instance)가 들어갑니다.
  ```

### 스태틱(정적) 메서드

* 클래스가 사용할 메서드 입니다.

* **정의 위에 `@staticmethod` 데코레이터를 사용합니다.**

* **인자 정의는 자유롭게 합니다. 어떠한 인자도 자동으로 넘어가지 않습니다.**

  ```python
  class MyClass:
        @staticmethod
        def static_method_name(arg1, arg2, ...):
            ...
  
    MyClass.static_method_name(.., ..)  # 아무일도 자동으로 일어나지 않습니다.
  ```

  

#### 정리

- 인스턴스는, 3가지 메서드 모두에 접근할 수 있습니다.
- 하지만 인스턴스에서 클래스메서드와 스태틱메서드는 호출하지 않아야 합니다. (가능하다 != 사용한다)
- 인스턴스가 할 행동은 모두 인스턴스 메서드로 한정 지어서 설계합니다.



#### 정리

- 클래스는, 3가지 메서드 모두에 접근할 수 있습니다.
- 하지만 클래스에서 인스턴스메서드는 호출하지 않습니다. (가능하다 != 사용한다)
- 클래스가 할 행동은 다음 원칙에 따라 설계합니다.
  - 클래스 자체(`cls`)와 그 속성에 접근할 필요가 있다면 클래스메서드로 정의합니다.
  - 클래스와 클래스 속성에 접근할 필요가 없다면 스태틱메서드로 정의합니다.



