# Practice
Work on practice 2024

# Автор: Казайкин Илья Александрович

Изменил задание на Python следующим образом: 
Реализовал сервис, который принимает и отвечает на HTTP запросы.
База данных: Биржа.
Объекты: Предприятие, покупатель, сделка. (смотреть "Иллюстрация БД.png")

# Подготовительные действия:
1. Установить Python 3.12.4
2. Клонировать проект и перейти в папку с проектом, для это нужно ввести команды в командной строке Windows:
\```
git clone https://github.com/IlyaKazaykin/Practice.git
cd Practice
\```

3. Создать и активировать виртуальную среду:
\```   
python -m venv myenv
myenv\Scripts\activate
\```

5. Установить модули из файла requirements.txt:   
pip install -r requirements.txt

6. Создать пустую БД в Postgresql:
CREATE DATABASE Stock_market;

6. Зайти в файл mydjangoproject/setting.py и изменить в DATABASES параметры на те, которые вы задали при создании пустой БД, например:
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

7. Сделать миграции БД:
python manage.py makemigrations
python manage.py migrate

8. Загрузить имеющиеся объекты БД /company/create /buyer/create или /deal/create , а также можно создать в /admin/
Для использования admin, нужно создать суперпользователя:
python manage.py createsuperuser 

9. Запустить сервер
python manage.py runserver

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
