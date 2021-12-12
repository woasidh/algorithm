# Python 정리

## 문자열

#### 문자열 곱셈
```python
# 'a'*5 = 'aaaaa'
```

#### 문자열 슬라이싱
```python
phoneNumber = '01025012501';
lastFourDigits = phoneNumber[-4:]; # 마지막 4자리
firstFourDigits = phoneNumber[:4]; # 처음 4자리
```

#### 알파벳인지 판별하기
```python
alpha = 'a';
nonAlpha = '1';

print(alpha.isalpha()); # True
print(nonAlpha.isalpha()); # False
```

#### 문자열 대체
```python
str = 'one2one';
str = str.replace('one', 'two');
print(str); # 'two2two'
```


## 배열

#### 배열 append
```python
# 특정 값 append
arr = [];
arr.append(1);

# 배열끼리 concat
arr1 = [1, 2, 3];
arr2 = [4, 5, 6];
joinedArr = arr1 + arr2;
```

#### 배열 정렬
```python
arr = [1, 3, 2];
arr.sort(); # 오름차순 정렬
arr.sort(reverse = True); # 내림차순 정렬

# sorted 사용 가능 (새로운 배열 반환)
sortedList = sorted(arr); # 인자로는 문자열, 배열, iterable한 객체는 모두 가능
sortedList = sorted(arr, reverse = True); # 인자로는 문자열, 배열, iterable한 객체는 모두 가능
```

#### 배열 수정
- index로 없애기
```python
arr = [0, 1, 2 ,3];
del arr[-1];
print(arr); # [0, 1, 2]
```

- vlaue로 없애기
```python
arr = [1, 3, 2, 3];
arr.remove(3);
print(arr); # [1, 2, 3] - 첫 원소만 없앰
```

- filter (List Comprehension)
```python
arr = [1, 3, 2, 3, 1];
arr = [x for x in arr if x != 3]; # 3인 애들 모두 filter
print(arr); # [1, 2, 1]
```

#### 배열 복사
```python
arr = [1, 2, 3];
tmpArr = arr[:];
```

#### map
```python
# 문자열로 이루어진 list를 정수형으로 변환하고 싶을 때
arr = ['1', '2', '3'];
arr = list(map(int, arr)); # map(함수, list/ tuple) 형식
```

#### 배열에서 value 찾기
```python
name = ['kim', 'park'];
print(name.index('kim')); #0
```

#### 문자열로 변환
```python
arr = ['a', 'b', 'c'];
str = ''.join(arr); #'abc'
strWithDash = '/'.join(arr); #'a/b/c'
```

#### 문자열에 특정 value 있는 지 찾기 (튜플, 문자열에서도 가능)
```python
print( 's' in ['s', 'd']); # True
```

#### sort 커스터마이징
```python
strings = ['aa', 'aab', 'ac'];
newList = sorted(strings, key = lambda x: (x[1], x)); # 2번째 char로 정렬
```

#### 배열 특정 원소 가지고 있는 지 확인
```python
arr = [1, 2, 3];
print(1 in arr); # True
```

## 자료형

#### 문자열

- int형으로 변환
```python
str = '1';
num = 1;

strToNum = int(str); # 1 
numToStr = str(num); # '1'
```

- 배열로 변환
```python
str = "Hello";
arr = list(str); # ['H', 'e', 'l', 'l', 'o'];
```

#### float형

- int형을 변환
```python
a = 1.234;
print(int(a)); # 1
```

- int형인 지 판별
```python
a = 1.234;
print(a.is_integer());

# 추가
print(a % 1 == 0); # 이거도 가능..
```

#### bool 연산자
- python은 %% || 대신 and, or 사용

#### tuple
```python
t = tuple([1]); # (1)
```

## 유틸

#### print
- 기본적으로 print('a)하면 print('a', end = '\n')
- 개행없이 하고 싶으면 print('a', end = '')

#### 삼항 연산자
```python
age = 15;
isOverFifteen = True if age > 15 else False;
```

#### 동시 할당

```python
m = 10;
n = 20;
a, b = max(m, n), min(m, n);
```

#### 제곱근 구하기
```python
import math;

num = 144;
print(math.sqrt(num)); # 12

# 추가
sqaureRoot = num ** (1/2); # 이거도 가능
```

#### for loop에서 index 구하기 
```python
word = [1, 2, 3, 4];
for idx, value in enumerate(word):
    print(idx, value);
```

#### ascii 코드
```python
# char에서 int 구하기
ord('a') # 97
# int에서 char 구하기
chr(97) # 'a'
```

#### 숫자인지 판별
```python

char1 = 'a';
char2 = '1';

print(char1.isdigit()); # false
print(char2.isdigit()); # true
```

#### call-by value? call-by-reference?
- python은 immutable / mutable한 객체로 나뉨 (인자로 넘겨주는 데이터 타입에 따라 달라짐)
- int,str같은 immutable한 애들 -> call by value
- list, tuple같은 mutable한 애들 -> call by reference

#### swap
- 파이썬 개쉬움 tmp 이딴거 필요없음
```python
a = 5;
b = 4;
a, b, = b, a;
```

#### if문 한줄로
```python
if a > 5: continue;
```

#### 배열 안에 여러 배열 넣기
```python
n = 10;
nestedEmptyArrs = [[] for _ in range(0, n)];
```

#### combination, permutation
```python
from itertools import combinations, permutations
arr = [1, 2, 3];
combinations(arr, 2); #12 13 23
permutations(arr, 2); # 12 13 21 23 31 32
```

#### any, all
- any: bool list중에 하나라도 True면
- all: bool list중에 모두가 True인지
```python
arr = [1, 2, 3];
print(any(i < 2 for i in arr)); # arr에 2보다 작은게 하나라도 있는지 - True
print(all(i < 4 for i in arr)); # arr가 모두 4보다 작은 지 - True
```

#### 올림, 내림
```python
import math
math.ceil()
math.floor()
```

####  class
```python
class Node:
    __init__(self, num):
        self.num = num;
        
    __lt__(self, other):
        return self.num < other.num;
```


#### 배열에서 특정 원소 index 찾기
```python
arr = [1, 2, 3];
arr.index(1); # 0
```

#### product
```python
from itertools import product
arr = [1, 2, 3];
product(arr, repeat = 2);
```