# 2 таблицы : Список животных. и список клиенттов.
# Django Rest Framework

1. Создани таблицы
2. Сделали миграцию
3. Сделали CRUD  backend
4. Создали папку frontend 
5. Создали файл index.html
6. Связали с сервером. Проверили если фронт видит данные из датабейз и показали в консоли. Нужно было еще сделать
    ### 1.pip install django-cors-headers
    ### 2.# settings.py
            INSTALLED_APPS = [
                ...
                'corsheaders',
                ...
            ]

            MIDDLEWARE = [
                ...
                'corsheaders.middleware.CorsMiddleware',
                ...
            ]
        Чтобы разрешить запросы со всех доменов
        CORS_ALLOW_ALL_ORIGINS = True
    
    ### 3. 
        <script>
            const SERVER2 = "http://127.0.0.1:8000/clients/";
            axios(SERVER2).then(res => console.log(res.data))

        </script>

7. Сделали CRUD для frontend
8. Authentication
