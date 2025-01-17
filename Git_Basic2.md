**git revert commit id:** 특정 commit을 없었던 일로 만드는 작업
```
$ git revert <commit id>
```

- 변경 사항을 안전하게 실행 취소할 수 있도록 도와주는 순방향 실행 취소 작업
- commit 기록에서 commit을 삭제하거나 분리하는 대신, 지정된 변경 사항을 반전시키는 새 commit을 생성

    → git에서 기록이 손실되는 것을 방지하며 기록의 무결성과 협업의 신뢰성을 높임 

**git reset commit id:** 
```
- git reset --soft <commit id> : 
- git reset --mixed <commit id> :
- git reset --hard <coomit id> :
```
**git restore file name:**

**git stash:**

- **git stash pop:**