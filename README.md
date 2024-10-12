# cadastr_api_test_case
[![Python CI](https://github.com/Andrey-Barinov/cadastr_api_test_case/actions/workflows/pyci.yml/badge.svg)](https://github.com/Andrey-Barinov/cadastr_api_test_case/actions/workflows/pyci.yml)
[![Maintainability](https://api.codeclimate.com/v1/badges/81447a78330f568b3165/maintainability)](https://codeclimate.com/github/Andrey-Barinov/cadastr_api_test_case/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/81447a78330f568b3165/test_coverage)](https://codeclimate.com/github/Andrey-Barinov/cadastr_api_test_case/test_coverage)
<h1>Описание задания: </h1>

1. Написать сервис, который принимает запрос с указанием кадастрового номера, широты и долготы, эмулирует отправку запроса на внешний сервер, который может обрабатывать запрос до 60 секунд. Затем должен отдавать результат запроса. Считается, что внешний сервер может ответить `true` или `false`.
2. Данные запроса на сервер и ответ с внешнего сервера должны быть сохранены в БД. Нужно написать АПИ для получения истории всех запросов/истории по кадастровому номеру.
3. Сервис должен содержать следующие эндпоинты:<br>
    <b>"/query"</b> - для получения запроса<br>
    <b>“/result"</b> - для отправки результата<br>
    <b>"/ping"</b> - проверка, что  сервер запустился<br>
    <b>“/history”</b> - для получения истории запросов<br>
4. Добавить Админку.
5. Сервис завернуть в Dockerfile.
6. *В качестве дополнительного задания. Можно добавить дополнительный сервис, который будет принимать запросы первого сервиса и эмулировать внешний сервер.

Будет плюсом!<br>

7. Документация к сервису<br>

8. Тесты функционала<br>

<b>Все задания выполнены кроме пункта №6</b>

<h2>Стек:</h2>
python = "^3.10"<br>
django = "^5.1"<br>
djangorestframework = "^3.15.2"<br>

<h2>Установка:</h2>
<b>Docker-контейнер:</b><br>
1. Необходимо иметь установленный Docker<br>
2. Клонировать репозиторий: <b>git clone git@github.com:Andrey-Barinov/cadastr_api_test_case.git</b><br>
3. Перейти в директорию: <b>cd cadastr_api_test_case/</b><br>
4. Собрать Docker-образ: <b>docker build . -t cadastr_api</b><br>
5. Запустить сервер: <b>docker run -p 8000:8000 cadastr_api</b><br>
6. Зайти в браузер и перейти по адресу <b>http://localhost:8000</b><br><br>
<b>Примечание:</b><br> 
Суперпользователь создаётся автомачески.<br>
Логин: admin<br>
Пароль: admin<br>

<h2>Документация:</h2>
<b>Эндпоинты:</b><br><br>
<b>1. "/ping"</b><br>
<b>Метод запроса:</b><br>
GET<br>
<b>Описание:</b><br>
Запрос возвращает словарь с сообщением о том, что сервер работает.<br>
<b>Коды ответа:</b><br>
200<br>
<b>Пример возвращаемых данных:</b><br>
{"message": "Server is running"}<br><br>

<b>2. "/query"</b><br>
<b>Методы запроса:</b><br>
POST<br>
<b>Описание:</b><br>
Этот запрос используется для передачи данных о кадастровом номере, широте, долготе и выполняет проверку.
Возвращает запись с pk, кадастровым номером, широтой, долготой и результатом проверки.<br>
<b>Коды ответа:</b><br>
201 - в случае успешного создания записи<br>
400 - в случае неккорректно введенных данных<br>

<b>Параметры запроса:</b><br>
<b>cadaster_number</b>(строка): Кадастровый номер объекта.<br>
<b>Обязательный:</b> Да<br>
<b>Пример:</b> "77:01:0004011:3880"<br>

<b>latitude</b> (число с плавающей запятой): Широта объекта.<br>
<b>Обязательный:</b> Да<br>
<b>Пример:</b> 55.7558<br>

<b>longitude</b> (число с плавающей запятой): Долгота объекта.  <br>
<b>Обязательный:</b> Да<br>
<b>Пример:</b> 37.6176<br>

<b>Пример возвращаемых данных:</b><br>
{
    "pk": 1,
    "cadastral_number": "77:01:0004011:3880",
    "latitude": 55.7558,
    "longitude": 37.6176,
    "result": true
}<br>

<b>3. "/result/" "result/?cadastral_number=ваш_кадастровый_номер"</b><br>
<b>Метод запроса:</b><br>
GET<br>
<b>Описание:</b><br>
Запрос возвращает список со всеми проверками по указанному кадастровому номеру. 
Если кадастровый номер не указан, возращает список всех проверок по всем кадастровым номерам.<br>
<b>Коды ответа:</b><br>
200<br>
<b>Параметры запроса:</b><br>
cadastral_number=ваш_кадастровый_номер

<b>Пример возвращаемых данных:</b><br>
[
{
"pk": 18,
"cadastral_number": "77:01:0004011:3880",
"latitude": 55.7558,
"longitude": 37.6176,
"result": true
}
]<br>

<b>4. "/history/"</b><br>
<b>Метод запроса:</b><br>
GET<br>
<b>Описание:</b><br>
Запрос возвращает список c историей всех проверок по всем кадастровым номерам.<br>
<b>Коды ответа:</b><br>
200<br>

<b>Пример возвращаемых данных:</b><br>
[{
    "pk": 1,
    "cadastral_number": "77:01:0004011:3880",
    "latitude": 55.7558,
    "longitude": 37.6176,
    "result": true
},<br>
{
    "pk": 2,
    "cadastral_number": "77:01:0005322:5790",
    "latitude": 34.7999,
    "longitude": 42.6537,
    "result": false
}]<br>




