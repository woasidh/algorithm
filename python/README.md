# Python 정리

## 문자열

#### 문자열 곱셈
```python
'a'*5 = 'aaaaa'
```

#### 문자열 슬라이싱
```python
phoneNumber = '01025012501';
lastFourDigits = phoneNumber[-4:]; // 마지막 4자리
firstFourDigits = phoneNumber[:4]; // 처음 4자리
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
arr.sort(); // 오름차순 정렬
arr.sort(reverse = True); // 내림차순 정렬
```

#### 배열 수정
- index로 없애기
```python
arr = [0, 1, 2 ,3];
del arr[-1];
print(arr); // [0, 1, 2]
```

- vlaue로 없애기
```python
arr = [1, 3, 2, 3];
arr.remove(3);
print(arr); // [1, 2, 3] - 첫 원소만 없앰
```

- filter (List Comprehension)
```python
arr = [1, 3, 2, 3, 1];
arr = [x for x in arr if x != 3]; // 3인 애들 모두 filter
print(arr); // [1, 2, 1]
```

## 자료형

#### 문자열 - 숫자형 변환
```python
str = '1';
num = 1;

strToNum = int(str); // 1 
numToStr = str(num); // '1'
```

#### bool 연산자
- python은 %% || 대신 and, or 사용



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
