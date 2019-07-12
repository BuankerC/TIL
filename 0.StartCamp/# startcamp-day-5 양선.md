# Startcamp-Day-5 양선





오늘 배울 것

플라스크 홈페이지 띄우고

텔레그램으로 플라스크 페이지에 요청

```python
#app.py

#플라스크에서 플라스크,리퀘스트,렌더 템플릿 가져옴
from flask import Flask, request, render_template 
from decouple import config
import requests
from bs4 import BeautifulSoup
import random

app = Flask(__name__)
#.env 파일 만들어서 중요한 정보는 숨김 처리
api_url = "https://api.telegram.org"
token = config("TELEGRAM_TOKEN")
chat_id = config("CHAT_ID")
naver_id = config("NAVER_ID")
naver_secret = config("NAVER_SECRET")


#사용자의 input 값을 받는 중
@app.route("/write")
def write():
    return render_template("write.html")

#사용자의 input 값을 텔레그램에 전달
@app.route("/send")
def send():
    msg = request.args.get('msg')
    url = f"{api_url}/bot{token}/sendMessage?chat_id={chat_id}&text={msg}"
    res = requests.get(url)
    return render_template("send.html")

@app.route(f"/{token}", methods=['POST'])
def telegram():
    print(request.get_json())
    data = request.get_json()
    user_id = (data.get('message').get('from').get('id'))
    user_msg = (data.get('message').get('text'))
	#표시하고 싶은 정보를 찾아 주소값을 입력
    
    if data.get('message').get('photo') is None:

        if user_msg == "점심메뉴":
            menu_list = ["삼계탕", "철판낙지볶음밥", "물냉면"]
            result = random.choice(menu_list)
        elif user_msg == "로또":
            numbers = list(range(1, 46))
            result = sorted(random.sample(numbers, 6))
        
        elif user_msg == "환율":
            url = "https://finance.naver.com/marketindex/?tabSel=exchange#tab_section"

            html = requests.get(url).text
            soup = BeautifulSoup(html, 'html.parser')
            select = soup.select_one('#exchangeList > li.on > a.head.usd > div > span.value')

            result = (f'지금 1$는 {select.text}원 입니다.')

        elif user_msg == "코스피":
            url = "https://finance.naver.com/sise/"

            html = requests.get(url).text
            soup = BeautifulSoup(html, 'html.parser')
            select = soup.select_one('#KOSPI_now')

            result = (f"코스피 지수 : {select.text}")

        elif user_msg == "디저트":
            menu = ["자바칩프라푸치노","아메리카노","비스켓","소프트콘","카라멜","감자칩"]
            choice = random.choice(menu)
            
            result = (f"오늘 디저트는 {choice} 어떤가요?")

        elif user_msg == "네이버":
            response = requests.get("https://naver.com").text
            soup = BeautifulSoup(response, "html.parser")
            naver = soup.select_one("#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_list.PM_CL_realtimeKeyword_list_base > ul:nth-child(5) > li:nth-child(1) > a.ah_a > span.ah_k")

            result = (naver.text)

        elif user_msg[0:2] == "번역":
            # 번역 안녕하세요 저는 누구입니다.
            raw_text = user_msg[3:]
            papago_url = "https://openapi.naver.com/v1/papago/n2mt"
            data = {
                "source":"ko", #한국어를
                "target":"en", #영어로 번역
                "text": raw_text
            }
            header = {
                'X-Naver-Client-Id':naver_id,
                'X-Naver-Client-Secret':naver_secret
            }
            res = requests.post(papago_url, data=data, headers=header)
            translate_res = res.json()
            translate_result = translate_res.get('message').get('result').get('translatedText')
            result = translate_result 
  			#네이버에서 오픈API가져와서 번역기능 사용하기      
        else:
            result = user_msg
    else:
        #사용자가 보낸 사진을 찾는 과정
        result="asdg"
        file_id = data.get('message').get('photo')[-1].get('file_id')
        file_url = f"{api_url}/bot{token}/getFile?file_id={file_id}"
        file_res = requests.get(file_url)
        file_path = file_res.json().get('result').get('file_path')
        file = f"{api_url}/file/bot{token}/{file_path}"

        #사용자가 보낸 사진을 클로버로 전송
        res = requests.get(file, stream=True)
        clova_url = "https://openapi.naver.com/v1/vision/celebrity"
        header = {
                'X-Naver-Client-Id':naver_id,
                'X-Naver-Client-Secret':naver_secret
            }
        clova_res = requests.post(clova_url, headers=header, files={'image':res.raw.read()})
        
        if clova_res.json().get('info').get('faceCount'):
            # 누구랑 닮았는지 출력
            celebrity = clova_res.json().get('faces')[0].get('celebrity')
            name = celebrity.get('value')
            confidence = celebrity.get('confidence')
            result = f"{name}일 확률이 {confidence*100}%입니다."
        else:
            # 사람이 없음
            result = "사람이 없습니다."



    res_url = f"{api_url}/bot{token}/sendMessage?chat_id={user_id}&text={result}"
    requests.get(res_url)
   
    return '', 200

if __name__ == "__main__":
    app.run(debug=True)   
```

**만든 프로그램 배포하기**

파이썬애니웨어 들어가서 만들기

```python
#test.py

import requests
from decouple import config
token = config("TELEGRAM_TOKEN")
url = f"https://api.telegram.org/bot{token}/"
user_id = config("CHAT_ID")

# send_url = f"{url}sendMessage?chat_id={user_id}&text=꽃길만걷게해줄게"
# requests.get(send_url)
ngrok_url = "https://buankerc.pythonanywhere.com"
webhook_url = f"{url}setWebhook?url={ngrok_url}/{token}"
print(webhook_url)
```



**send.html**

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <h1>
        성공적으로 메세지가 전달되었습니다
    </h1>
</body>
</html>
```



**write.html**

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <form action="/send">
        <input type="text" name="msg">
        <input type="submit">
    </form>
</body>
</html>
```

홈페이지에 입력창 만들기



***env파일 만들어서 중요정보 숨김처리하기***

```env
TELEGRAM_TOKEN='866368695:AAHia-sDi9K9mQeOUUXReHCLogBx537jkks'
CHAT_ID='830079394'
NAVER_ID='aPkY8yPPPXE7a5q_nG9g'
NAVER_SECRET='nPSIitT5vL'
```



***gitignore 파일 만들어서 env 파일 포함 및 ignore할 파일 정리하기***

```gitignore
.env

# Created by https://www.gitignore.io/api/python,windows,visualstudiocode
# Edit at https://www.gitignore.io/?templates=python,windows,visualstudiocode

### Python ###
# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# C extensions
*.so

# Distribution / packaging
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
pip-wheel-metadata/
share/python-wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST

# PyInstaller
#  Usually these files are written by a python script from a template
#  before PyInstaller builds the exe, so as to inject date/other infos into it.
*.manifest
*.spec

# Installer logs
pip-log.txt
pip-delete-this-directory.txt

# Unit test / coverage reports
htmlcov/
.tox/
.nox/
.coverage
.coverage.*
.cache
nosetests.xml
coverage.xml
*.cover
.hypothesis/
.pytest_cache/

# Translations
*.mo
*.pot

# Django stuff:
*.log
local_settings.py
db.sqlite3
db.sqlite3-journal

# Flask stuff:
instance/
.webassets-cache

# Scrapy stuff:
.scrapy

# Sphinx documentation
docs/_build/

# PyBuilder
target/

# Jupyter Notebook
.ipynb_checkpoints

# IPython
profile_default/
ipython_config.py

# pyenv
.python-version

# pipenv
#   According to pypa/pipenv#598, it is recommended to include Pipfile.lock in version control.
#   However, in case of collaboration, if having platform-specific dependencies or dependencies
#   having no cross-platform support, pipenv may install dependencies that don't work, or not
#   install all needed dependencies.
#Pipfile.lock

# celery beat schedule file
celerybeat-schedule

# SageMath parsed files
*.sage.py

# Environments
.env
.venv
env/
venv/
ENV/
env.bak/
venv.bak/

# Spyder project settings
.spyderproject
.spyproject

# Rope project settings
.ropeproject

# mkdocs documentation
/site

# mypy
.mypy_cache/
.dmypy.json
dmypy.json

# Pyre type checker
.pyre/

### VisualStudioCode ###
.vscode/*
!.vscode/settings.json
!.vscode/tasks.json
!.vscode/launch.json
!.vscode/extensions.json

### VisualStudioCode Patch ###
# Ignore all local history of files
.history

### Windows ###
# Windows thumbnail cache files
Thumbs.db
Thumbs.db:encryptable
ehthumbs.db
ehthumbs_vista.db

# Dump file
*.stackdump

# Folder config file
[Dd]esktop.ini

# Recycle Bin used on file shares
$RECYCLE.BIN/

# Windows Installer files
*.cab
*.msi
*.msix
*.msm
*.msp

# Windows shortcuts
*.lnk

# End of https://www.gitignore.io/api/python,windows,visualstudiocode
```

