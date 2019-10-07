model.py에 클래스 추가시  

python manage.py makemigrations

python manage.py migrate



**python manage.py shell_plus**



# django ORM

### READ

```python
Question.objects.get(id=1)
```



### 댓글 생성

```python
In [10]: answer = Answer()

In [11]: answer
Out[11]: <Answer: Answer object (None)>

In [12]: answer.content
Out[12]: ''

In [14]: answer.content = "이것은 댓글입니다"

In [15]: answer
Out[15]: <Answer: Answer object (None)>

In [16]: answer.content
Out[16]: '이것은 댓글입니다'
    
In [27]: Answer.objects.create(content="두번쨰", question=question)
Out[27]: <Answer: Answer object (2)>
```



### 댓글 정보

```python
In [28]: answer
Out[28]: <Answer: Answer object (1)>

In [29]: answer.content
Out[29]: '이것은 댓글입니다'

In [30]: answer.id
Out[30]: 1

In [31]: answer.pk
Out[31]: 1

In [32]: answer.question_id
Out[32]: 1

In [33]: answer.question.id
Out[33]: 1
   
In [34]: answer.question.pk
Out[34]: 1

In [35]: answer.question.content
Out[35]: '123'

```



### 1:N

- Question(1) => Answer(N) : answer_set

  ```python
  In [39]: question.answer_set.all()
  Out[39]: <QuerySet [<Answer: Answer object (1)>, <Answer: Answer object (2)>]>
  ```

  - question.answer 로는 가져올 수 없다.

- Answer(N) => Question(1) : question

```python
In [25]: answer.question
Out[25]: <Question: Question object (1)>
```















