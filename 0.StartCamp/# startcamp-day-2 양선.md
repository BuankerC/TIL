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
	rm-r 지우기
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

os.chdir(r"C:\Users\student\startcamp\students")
for filename in os.listdir("."):
    os.rename(filename, "SAMSUNG_" + filename)

### 2-4 다시 바꾸기

import os


os.chdir(r"C:\Users\student\startcamp\students")
for filename in os.listdir("."):
    os.rename(filename, filename.replace("SSAFY", "SSAFY_"))

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
    
## git

(분산)버전 관리 시스템

코드의 History를 관리하는 도구
개발된 과정과 역사를 볼 수 있으며,
프로젝트의 이전 버전을 복원하고 변경 사항을 비교, 분석 및 병합도 가능

### DVCS(Distributed Version Control System)

git이 있다면

- 차이가 무엇이고 수정이유를 log로 남길 수 있다.

















~~~