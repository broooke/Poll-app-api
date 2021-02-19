# Poll App API

Задача: спроектировать и разработать API для системы опросов пользователей.

# Installation guide

```bash
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

# API documentation

### Login
* Request method: GET
* URL: http://localhost:8000/api/login/
* Body:
      * username: Username user
      * password: Password user


### Create Poll
* Request method: POST
* URL: http://localhost:8000/api/poll/create/
* Headers:
	* Authorization: Token 'userToken'
* Body:
	* name: Name of poll
	* date_end: Poll end date, format: YYYY-MM-DD HH:MM:SS
	*description: Description of poll


### Update Poll
* Request method: PUT
* URL: http://localhost:8000/api/poll/update/<Poll ID>/
* Headers:
	*Authorization: Token 'userToken'
* Body:
	* name: Name of poll
	* description: Description of poll
			

### Delete Poll
* Request method: DELETE
* URL: http://localhost:8000/api/poll/delete/<Poll ID>/
* Headers:
	*Authorization: Token 'userToken'


### Create Question
* Request method: POST
* URL: http://localhost:8000/api/question/create/<Poll ID>/
* Headers:
	* Authorization: Token 'userToken'
* Body:
	* name: Name of question
	* type_question: Type of question


### Update Question
* Request method: PUT
* URL: http://localhost:8000/api/question/update/<Question ID>/
* Headers:
	* Authorization: Token 'userToken'
* Body:
	* name: Name of question
	* type_question: Type of question
			
			
### Delete Question
* Request method: DELETE
* URL: http://localhost:8000/api/question/delete/<Question ID>/
* Headers:
	* Authorization: Token 'userToken'


### Create Choice
* Request method: POST
* URL: http://localhost:8000/api/choice/create/<Question ID>/
* Headers:
	* Authorization: Token 'userToken'
* Body:
	* text: Text of the choice


### Update Choice
* Request method: PUT
* URL: http://localhost:8000/api/choice/update/<Choice ID>/
* Headers:
	* Authorization: Token 'userToken'
* Body:
	* text: Text of the choice


### Delete Choice
* Request method: DELETE
* URL: http://localhost:8000/api/choice/delete/<Choice ID>/
* Headers:
	* Authorization: Token 'userToken'


### Active Polls
* Request method: GET
* URL: http://localhost:8000/api/polls/active/
* Headers:
	* Authorization: Token 'userToken'


### Answers
* Request method: POST
* URL: http://localhost:8000/api/answer/create/<Poll ID>/
* Headers:
	* Authorization: Token 'userToken'
*Body:
	* text{0,1,2,4....}: If the question type is "Text Answer", then depending on the number of questions, the number after the "text" will increase 
	* name: If the question type is "One Choice" 
	* choice{0,1,2,3,4....}: If the question type is "Many Choice", then depending on the number of choices, the number after the "choice" will increase
  


  
