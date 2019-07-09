***CLI***
Command Line Interface

***종류***
1. 유닉스 shell(sh, zsh, bash 등)

```bash 명령어 기초```

	ls 현재 디렉토리의 내용을 나열
	
	pwd 현재 작업하고 있는 위치를 알려줌
	
	cd 현재 작업하는 디렉토리를 변경
	
	mkdir 새로운 디렉토리 생성
	
	touch 새로운 파일을 생성
	
	echo 문자열 출력
	
	rm 파일 지우기
	
	rm-r 폴더 지우기
	
	exit 터미널종료
	
	위쪽화살표버튼 가장 최근에 사용한 명령어 불러오기    


CLI에는 항상 자신에 ***어디에 있는 지*** 주의하자!

## 2. Python 활용하기

### 2-1 Python 내장함수 browser 이용

import webbrowser

url = "https://search.naver.com/search.naver?sm=top_hty&fbm=0&ie=utf8&query="
my_keywords = ["에이프릴","ITZY","Daybreak","clazziquai"]
for my_keyword in my_keywords:
    webbrowser.open(url + my_keyword)
    
### 2-2 Beautiful Soup 이용하기

import requests
from bs4 import BeautifulSoup

response = requests.get("https://naver.com").text
soup = BeautifulSoup(response, "html.parser")
naver = soup.select_one("#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_list.PM_CL_realtimeKeyword_list_base > ul:nth-child(5) > li:nth-child(1) > a.ah_a > span.ah_k")

print(naver.text)

### 2-3 파일명 바꾸기

    import os
    사용할 함수를 선언하고

os.chdir(r"C:\Users\student\startcamp\students")

​              **(r'폴더주소')**



for filename in os.listdir("."):

- 리스트의 개수만큼 반복 가능

​    os.rename(filename, "SAMSUNG_" + filename)

### 2-4 다시 바꾸기

import os

 **파일명을 바꿀 위치 지정하기**

os.chdir(r"C:\Users\student\startcamp\students")



for filename in os.listdir("."):
    os.rename(filename, filename.replace("SSAFY", "SSAFY_"))

**폴더에서 파일이름 지정한 후 대체할 이름으로 변경**

환율 가져오기

import requests
from bs4 import BeautifulSoup
url = "https://finance.naver.com/marketindex/exchangeList.nhn"
response = requests.get(url).text
soup = BeautifulSoup(response, "html.parser")

tr = soup.select("tbody > tr")
for r in tr:
    print(r.select_one('.tit').text.strip())
    print(r.select_one('.sale').text) 

**select** 

- 리스트의 모든 변수를 선택

  **select.one**

  -리스트의 하나의 변수를 선택

  

### 3-1 이름 랜덤 생성하기

**faker 함수**

- 임의의 정보를 랜덤하게 생성하는 함수
- 한국어도 지원 가능

from faker import Faker
import os

f = Faker('ko_KR')

for i in range(100):
    filename = f"{i}_{f.name()}.txt"
    cmd = f"touch {filename}"
    os.system(cmd)

### 3-2 코스피 지수

**BeautifulSoup 함수**



import requests
from bs4 import BeautifulSoup

response = requests.get("https://finance.naver.com/sise/").text
soup = BeautifulSoup(response, "html.parser")
kospi = soup.select_one('#KOSPI_now')
print(kospi.text)

### 3-3 실시간 검색어 1위 찾기
**import requests**

1) request.get(주소)

2) request.

from bs4 import BeautifulSoup

response = requests.get("https://naver.com").text
soup = BeautifulSoup(response, "html.parser")
naver = soup.select_one("#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_list.PM_CL_realtimeKeyword_list_base > ul:nth-child(5) > li:nth-child(1) > a.ah_a > span.ah_k")

print(naver.text)








## git

(분산)버전 관리 시스템

코드의 History를 관리하는 도구
개발된 과정과 역사를 볼 수 있으며,
프로젝트의 이전 버전을 복원하고 변경 사항을 비교, 분석 및 병합도 가능

### DVCS(Distributed Version Control System)

git이 있다면

- 차이가 무엇이고 수정이유를 log로 남길 수 있다.

git의 작업 흐름

    add  커밋할 목록에 추가
    commit  커밋(create a snapshot) 만들기
    push  현재까지의 역사(commits)가 기록되어 있는 곳에 새로 생성한 커밋들 반영하기


## 3 내 인생 첫 Git 및 Github 활용과정
    > Git과 GitHub 사용이 익숙해지면 따로 정리하자

###3-1 처음 내 repo 올리기
	1. Git Bash 들어가기
	2. 내 프로젝트 폴더에 들어가서 git init 명령어 타이핑
	> 현재 위치 옆 부분에 (master) 있는 확인할 것
	3. ls -a 입력 후, git/ 생성되었는 지 확인
	4. Visual Studio Code에 들어가서 .gitignore파일을 새로 생성
	5. https://gitignore.io/ 사이트 접속 후 프로젝트에 사용된 프로그램. 언어 찾기
	6. 모두 복사해 .gitignore 파일에 모두 붙여넣기
	7. Git Bash에 명령어 git add
	> 위의 명령어는현재 폴더 내의 모든 파일을 추가할 것이다.
	8. git commit -m "First commit" 이 올릴 파일에 커멘트를 추가하기
	9. 초기 설정 시 어디에 올릴지 모르기 때문에 commit 명령어에서 오류가 큼
	10. git config --global user. email 내에 "내 Github 이메일 입력"
	11. git config --global user. name 내에 "내 Github 닉네임 입력"
	12. 위의 두 명령어를 Git Bash에 타이핑해 설정을 완료할 것
	13. 로그인하려는 팝업창이 뜰텐데 로그인 해주세요
	14. 다시 git commit -m "first commit" 명령어로 커밋 추가
	15. new repository 항목을 클릭하고 Repository name에 프로젝트명 넣기
	16. 자랑하고 싶으면 Public으로 공개하도록 하자 그 후 만들기 버튼 누르면
	17. 창이 뜨면서 gi remote ~~~ 라는 부분을 복사해 git bash에 붙여넣는다.
	18. 그래서 git bash에 붙인 명령어를 실행할 것
	19. 다시 git bash에 git push origin master를 누르면 모든게 업로드됩니다.














~~~

~~~