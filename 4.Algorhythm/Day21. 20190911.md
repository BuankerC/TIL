[TOC]

# SW 문제 해결 응용

## 프로그래밍하기 위한 제약 조건과 요구사항

- 프로그래밍 언어의 특성
- 프로그램이 동작할 HW와 OS에 관한 지식
- 라이브러리들의 유의 사항들
- 프로그램이 사용할 수 있는 최대 메모리
- 사용자 대응 시간 제한
- 재사용성이 높은 간결한 코드



## 복잡도 분석

### 알고리즘

- (명) 알고리즘 : 유한한 단계를 통해 문제를 해결하기 위한 절차나 방법이다. 주로 컴퓨터용어로 쓰이며, 컴퓨터가 어떤 일을 수행하기 위한 단계적 방법을 말한다.
- 간단하게 다시 말하면 어떠한 문제를 해결하기 위한 절차라고 볼 수 있다.
- 예를 들어 1부터 100까지의 합을 구하는 문제를 생각해 보자



### 알고리즘의 효율

- 공간적 효율성과 시간적 효율성
  - 공간적 효율성은 연산량 대비 얼마나 적은 메모리 공간을 요하는 가를 말한다.
  - 시간적 효율성은 연산량 대비 얼마나 적은 시간을 요하는 가를 말한다.
  - 효율성을 뒤집어 표현하면 복잡도(Complexity)가 된다. 복잡도가 높을수록 효율성은 저하된다.
- 시간적 복잡도 분석
  - 하드웨어 환경에 따라 처리시간이 달라진다.
    - 부동소수 처리 프로세서 존재유무, 나눗셈 가속기능 유무
    - 입출력 장비의 성능, 공유여부
  - 소프트웨어 환경에 따라 처리시간이 달라진다.
    - 프로그램 언어의 종류
    - 운영체제, 컴파일러의 종류
  - 이러한 환경적 차이로 인해 분석이 어렵다.



## 실수

### 실수를 저장하기 위한 형식

- 단정도 실수(32비트)
- 배정도 실수(64비트)
  - 가수부(mantissa) : 실수의 유효 자릿수들을  부호화된 고정 소수점으로 표현한 것
  - 지수부(exponent) : 실제 소수점의 위치를 지수 승으로 표현한 것

### 단정도 실수의 가수 부분을 만드는 방법

- 예 : 1001.0011
  - 정수부의 첫 번째 자리가 1이 되도록 오른쪽으로 시프트
  - 소수점 이하를 23비트로 만든다.
  - 소수점 이하만을 가수 부분에 저장
  - 지수 부분은 시프트 한 자릿수 만큼 증가 또는 감소

```python
0001.0010011
0001.00100110000000000000000
00100110000000000000000

-> 1.0010011 * 2**3
```



### 단정도 실수의 지수 부분을 만드는 방법

- 지수부에는 8비트가 배정(256개의 상태를 나타낼 수 있음)
- 숫자로는 0-255까지 나타낼 수 있지만, 음수 값을 나타낼 수 있어야 하므로 익세스(excess) 표현법을 사용
  - 익세스 표현법 : 지수부의 값을 반으로 나누어 그 값을 0으로 간주하여 음수지수와 양수지수를 표현하는 방법

### 단정도 표현에서의 지수부 익세스 표현



### 컴퓨터는 실수를 근사적으로 표현한다.

- 이진법으로 표현할 수 없는 형태의 실수는 정확한 값이 아니라 근사 값으로 저장되는데 이때 생기는 작은 오차가 계산 과정에서 다른 결과를 가져온다.

### 실수 자료형의 유효 자릿수를 알아두자.

- 32 비트 실수형 유효자릿수(십진수) -> 6
- 64 비트 실수형 유효자릿수(십진수) -> 15

### 파이썬에서의 실수 표현 범위를 알아보자.

- 파이썬에서는 내부적으로 더 많은 비트를 사용해서 훨씬 넓은 범위의 실수를 표현할 수 있다.
- 최대로 표현할 수 있는 값은 약 1.8 * 10 ** 308 이고 이 이상은 inf로 표현

- 최소로 표현할 수 있는 값은 약 5.0 * 10 ** -324이며, 이 이하는 0으로 표현



# 2. 완전 검색 & 그리디

##



​										거북선 거북선 거북선

판옥선 판옥선 판옥선 판옥선 판옥선 판옥선 판옥선 판옥선 판옥선 판옥선 판옥선 판옥선