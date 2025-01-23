# 모듈

- 한 파일로 묶인 변수와 함수의 모음.
- 특정한 기능을 하는 코드가 작성된 파이썬 파일(.py)
- **module.veri, module.func()**
- '. (dot)' 연산자 : "점의 왼쪽 객체에서 점의 오른쪽 이름을 찾아라"

### 모듈을 가져오는 방법

- **import** 문 사용 : 파이썬에서 더 권장(명시적, 어떤 모듈을 사용하는지 직관적으로 파악 가능능)
```
import math
print(math.sqrt(4))
```
- **from** 절 사용
```
from math import sprt
print(sqrt(4))
```

### 모듈 주의사항

- 서로 다른 모듈이 같은 이름의 함수를 제공할 경우 문제 발생
- 마지막에 import된 이름으로 대체됨
```
from math import pi, sqrt
from my_math import sqrt - 사용
```
```
그래서 모듈 내 모든 요소를 한번에 import하는 * 표기는 권장하지 않음

from math import *
```

### 'as' 키워드
- as 키워드를 사용하여 별칭(alias)을 부여

    - 두개 이상의 모듈에서 동일한 이름의 변수, 함수 클래스 등을 가져올 때 발생하는 이름 충돌 해결

```
from math import sqrt
from my_math import sqrt as my_sqrt
```

### 사용자 정의 모듈

### 파이썬 표준 라이브러리(Python Standard Library)

- 파이썬 언어와 함께 제공되는 다양한 모듈과 패키지 모음

### 패키지(Package)

- 연관된 모듈들을 하나의 디렉토리에 모아 놓은 것

**(모듈을 모아서 패키지, 모듈과 패키지를 모아서 라이브러리)**

```
from my_packge.math import my_math
from my_packge.statistics import tools
```

### 내부 패키지 VS 외부 패키지

- PSL 내부 패키지 : 설치 없이 바로 import하여 사용
- 외부 패키지 : **pip**를 사용하여 설치 후 import 필요요

### pip

- 외부 패키지들을 설치하도록 도와주는 파이썬의 패키지 관리 시스템
- PyPI(Python Package Index)에 저장된 외부 패키지들을 설치

### 패키지 설치

- 최신 버전/ 특정 버전/ 최소 버전을 명시하여 설치할 수 있음
```
pip install SomePackage (최신 버전)
pip install SomePackage==1.0.5 (특정 버전)
pip install SomePackage>=1.0.4 (최소 버전전)
```
```
pip list : pip로 설치한 패키지 확인인
```

### 패키지 사용 목적

- 모듈들의 이름공간을 구분하여 충돌을 방지.
- 모듈들을 효율적으로 관리하고 재사용할 수 있도록 돕는 역할할