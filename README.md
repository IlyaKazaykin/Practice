# Автор: Казайкин Илья Александрович  

Изменил задание на Python следующим образом:  
Реализовал сервис, который принимает и отвечает на HTTP запросы.  
База данных: Биржа.  
Объекты: Предприятие, покупатель, сделка. (смотреть "Иллюстрация БД.png")  

# Подготовительные действия:  
1. Установить Python 3.12.4
2. Клонировать проект и перейти в папку с проектом, для это нужно ввести команды в командной строке Windows:
```mark1
git clone https://github.com/IlyaKazaykin/Practice.git
cd Practice
```
3. Создать и активировать виртуальную среду:
 ```mark2
python -m venv myenv
myenv\Scripts\activate
```
4. Установить модули из файла requirements.txt:
```mark3
pip install -r requirements.txt
```
5. Создать пустую БД в Postgresql:
```mark4
CREATE DATABASE Stock_market;
```
6. Зайти в файл mydjangoproject/setting.py и изменить в DATABASES параметры на те, которые вы задали при создании пустой БД, например:
```mark5
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "stock_market",
        "USER": "postgres",
        "PASSWORD": "bkmbxm12112002",
        "HOST": "localhost",
        "PORT": "5432",
    }
}
```
7. Сделать миграции БД:
```mark6
python manage.py makemigrations
python manage.py migrate
```
8. Загрузить имеющиеся объекты БД /company/create , /buyer/create или /deal/create , например для deal:
```mark7
{
        "deal_date": "2024-06-09",
        "shares_quantity": 23,
        "buyer": 4,
        "company": 4
}
```
 Для компании:
```mark8
{
        "name": "Яндекс",
        "address": "Самара, Московское шоссе, 32А",
        "share_price": "2300.4",
        "shares_available": 250000000,
        "controlling_stake": 51
}
```
 Для покупателя:
```mark9
{
        "name": "Казайкин И.А.",
        "address": "Самара, Московское шоссе, 32А",
        "phone": "+76927549329",
        "email": "kazaykin@mail.ru"
}
```
 Также можно создать в /admin/ .  
 Для использования admin, нужно создать суперпользователя:  
```mark10
python manage.py createsuperuser 
```
9. Запустить сервер
```mark11
python manage.py runserver
```
10. Перейти по http ссылке и добавить к ней, для проверки задания:
```mark12
admin/  
company/  
company/create/  
buyer/  
buyer/create/  
deal/  
deal/create/
```
 Также данные можно фильтровать, используя конструкции:  
 ```mark13
/deal/?company_id=1 (выведет сделки, где принимала участие компания с id=1),  
/deal/?buyer_id=1 (выведет сделки, где принимал участие покупатель с id=1),  
/deal/?deal_date=2024-06-08 (выведет сделки, даты которой 2024-06-08),
/company/?name=Лукойл (выведет компанию с названием "Лукойл"),  
/buyer/?name=Сидоров К.В. (выведет покупателя под именем "Сидоров К.В.").  
```
