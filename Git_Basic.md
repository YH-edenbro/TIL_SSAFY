# GIT 관리하기
## 로컬 저장소
- GIT : 분산 버전 관리 시스템

**git init :** 로컬 저장소 설정(초기화) → git의 버전 관리를 시작할 디렉토리에서 진행
```
git init
```

### git 시작 전 기본 설정

**git config --global user.email "메일주소"** 

**git config --global user.name "유저네임"**
```
git config --global user.email "메일주소"

git config --global user.name "유저네임"
```
### commit 작성자(autor) 정보 설정

**git config --global -l:** git global 설정 정보 보기
```
git config --global -l
```

**git add {} :** 변경사항이 있는 파일을 staging area에 추가
```

git add
```
  - **git add -A:** add All
  ```
  git add -A
  ```

**git status :** 로컬 저장소의 파일 상태 확인
```
git status
```
- **git config --global alias.st 'status':** status의 별명을 st로 만들어 git st로 간편하게 사용할 수 있도록 만들기 
```
git config --global alias.st 'status' : can use git st
```
**git commit :** staging area에 있는 파일들을 저장소에 기록 → 해당 시점의 버전을 생성하고 변경 이력을 남기는 것
```
git commit
```

- **git commit -m "commit내용":** commit의 설명을 vim이 아닌 바로 설정할 수 있도록 만들어줌. 
```
git commit -m "내용"
```
- **git commit --amend:** 바로 직전의 c ommit 메시지 수정
```
git commit --amend
```

**git log:** commit history 보기
```
git log
```

- **git log --oneline:** commit 목록 한 줄로 보기
```
git log --oneline
```

## 원격 저장소(Git Hub와 연결)

**git remote add origin "연결할 repo URL:** 로컬 저장소에 원격 저장소 추가
```
git remote add origin "연결할 repo URL
```

- "origin"은 추가하는 원격 저장소의 별칭으로,별칭을 사용해 로컬 저장소 한 개에 여러 원격 저장소를 추가 할 수 있음.

**git push origin master:** 원격 저장소에 commit 목록을 업로드
```
git push origin master
```

**git pull origin master:** 원격 저장소의 변경사항만을 받아옴 (업데이트된 부분)
```
git pull origin master
```

- **git pull --rebase origin master:**
리베이스는 로컬 브랜치의 변경 사항을 원격 브랜치 위에 재적용
```
git pull --rebase origin master
```
**git clone "받아올 repo URL":** 원격 저장소 전체를 복제(다운로드)
```
git clone "받아올 repo URL
```

- clone으로 받은 프로젝트는 이미 **git init**이 되어 있음

### gitignore
- Git에서 특정 파일이나 디렉토리를 추적하지 않도록 설정하는 데 사용되는 텍스트 파일 
→ 프로젝트에 따라 공유하지 않아야 하는 것들도 존재하기 때문. (ex: API키, PW 등...)

- **.gitignore**로 생성

        주의사항!

        이미 git의 관리를 받은 이력이 있는 파일이나 디렉토리는 나중에 gitignore에 작성해도 적용되지 않음.
        (git rm --cached 명령어를 통해 git 캐시에서 삭제 필요)
- 유용한 사이트

[git ignore](https://www.toptal.com/developers/gitignore/)  : 프로젝트에 맞는 기본적인 ignore 목록을 다운 가능.

