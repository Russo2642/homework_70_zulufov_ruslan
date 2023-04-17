# homework_62_zulufov_ruslan
Данные админки:  
 Логин - admin  
 Пароль - admin  

# Инстукция к API
### Для проекта
1. Детальный просмотр  
GET http://127.0.0.1:8000/api/project/2  
2. Редактирование  
PUT http://127.0.0.1:8000/api/project/2/update  
В body передаём (изменяем тип передаваемых данных на JSON):  

{  
    "start_date": "2023-04-17",  
    "title": "Projec test api update",  
    "description": "Some desc"  
}  
  
3. Удаление
DELETE http://127.0.0.1:8000/api/project/2/delete

### Для задач
1. Детальный просмотр  
GET http://127.0.0.1:8000/api/issue/2  
2. Редактирование  
PUT http://127.0.0.1:8000/api/issue/2/update  
В body передаём (изменяем тип передаваемых данных на JSON)  
{  
    "summary": "Issue Test API update",  
    "status": 2,  
    "types": [1]  
}  
  
3. Удаление
DELETE http://127.0.0.1:8000/api/issue/3/delete
