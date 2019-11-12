# git 협업

팀장 : 박정우 팀원 : 양선

### 팀장님 먼저!

깃헙에 pr-test 레포지토리 생성

깃배쉬가서 git-pr-test 레포지토리 생성

open with code

README.md 작성

```markdown
## N행시
> 아래의 제시 단어를 이용해서 N행시를 지어주세요
OOO

```

깃 배쉬 켜서

git init

git add .

git commit -m "20191105 | 기본구조완성"

git add origin "깃헙주소"

git push origin master



### 팀원 차례!

팀장님에게 깃헙주소를 받아 접속한다.

fork버튼 클릭

fork - 기존의 정보를 가져와 다른 분기로 나누는 것(협업을 위한 도구)

깃 배쉬 열어서 클론하기

git clone https://github.com/BuankerC/git-pr-test.git

내용 수정 후

git add.

git commit -m "고양이 완료"

git push origin master

깃헙 페이지 들어가서 팀원이 팀장보다 커밋이 많아야 정상

pull request로 들어감

New pull request 접속

작성 



### 팀장 턴!!

반려



### 팀원 턴!!

수정후 풀리퀘스트 한번 더

팀장이 merge pull request하면 반영됨



### 팀장 턴

git pull origin master해서

없었던 데이터를 받아옴



### 팀원 턴

git pull 한번 더(merge commit이 없기 때문)

팀장 깃 주소가서 깃 클론

git remote add upstream https://github.com/betrayers000/git-pr-test.git

git fetch upstream

git log --oneline

결과창

2fc2480 (HEAD -> master, origin/master, origin/HEAD) 고양이수정
b9072cb 고양이완료
50a0b30 basic

git merge upstream/master

git push origin master

팀장 팀원의 원격/로컬의 파일 일치시키기 완료



## 새로운 프로젝트 브랜치



### 팀장턴

collaborator에서 팀원 아이디 추가

폴더 만들고

문서 생성

git init

git branch

git checkout -b dev-seon



### 팀원

git checkout -b dev-woo

문서 수정

git add .

git commit -m "가위"

git push origin dev-woo

