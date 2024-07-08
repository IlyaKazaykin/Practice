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
8. Загрузить имеющиеся объекты БД /company/create , /buyer/create или /deal/create , а также можно создать в /admin/
Для использования admin, нужно создать суперпользователя:
```mark7
python manage.py createsuperuser 
```
9. Запустить сервер
```mark8
python manage.py runserver
```
10. Перейти по http ссылке и добавить к ней, для проверки задания:  
admin/  
company/  
company/create/  
buyer/  
buyer/create/  
deal/  
deal/create/  
 Также данные можно фильтровать, используя конструкции:  
/deal/?company_id=1 (выведет сделки, где принимала участие компания с id=1)  
/company/?name=Лукойл (выведет компанию с названием "Лукойл")  
/buyer/?name=Сидоров К.В. (выведет покупателя под именем "Сидоров К.В.")  
