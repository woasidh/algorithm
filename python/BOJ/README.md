## 백준 파이썬 풀이시 유의사항

#### input()보다는 sys 모듈을 사용하자
```python
import sys

cmd = sys.stdin.readline();
```

#### input받을 때 개행 문자 유의사항
- readline의 string 자체에 '\n'이 포함되어 있어서
- split(' ')이 아닌 split()을 쓰자 (개행, 스페이스, 탭 등 모두 고려하여 split)