# homework_58_zulufov_ruslan
Данные админки:  
 Логин - admin  
 Пароль - admin  
 
 ЭТАП 2
 
from tracker.models import Issue  
from django.db.models import Q  
1. Закрытые задачи за последний месяц от текущей даты (вхождение определяйте по дате последнего обновления):  
	today = datetime.today()  
	today_timedelta = today - timedelta(days=30)  
	Issue.objects.filter(updated_at__range=(today_timedelta, today), status__name='Done')  

2. Задачи, имеющие один из указанных статусов И один из указанных типов (в запросе укажите 2 любых названия типа и 2 названия статуса, которые есть в вашей базе):  
	Issue.objects.filter((Q(types__name='Task') | Q(types__name='Bug')) & (Q(status__name='New') | Q(status__name='Done')))  

3. Задачи, в названии которых содержится слово "bug" в любом регистре или относящиеся к типу "Баг", имеющие НЕ закрытый статус:  
	Issue.objects.filter(Q(types__name='Bug') | Q(summary__icontains='New')).exclude(status__name='Done')  


Бонусы:  
1. Для всех задач только следующие поля: id, название задачи, название типа и название статуса:  
	Issue.objects.values('id', 'summary', 'status__name', 'types__name')  

2. Задачи, где краткое описание совпадает с полным:  
for desc in description:  
    for key, value in desc.items():  
        if Issue.objects.filter(summary__iexact=value):  
            Issue.objects.filter(summary__iexact=value)  

3. Количество задач по каждому типу:  
	bug = Issue.objects.filter(types__name='Bug').count()  
	enhancement = Issue.objects.filter(types__name='Enhancement').count()  
	task = Issue.objects.filter(types__name='Task').count()  
	print(f"Bug type: {bug}\nEnhancement type: {enhancement}\nTask type: {task}")  
