# Task 4. Database

В данном проекте реализованы сущности для работы с базой данных и таблицами.

Для корректной работы необходимо установить:
- [python](https://www.python.org/downloads/)
- [mysql](https://www.mysql.com/downloads/)

После установки вышеупомянутого ПО необходимо проинсталировать расширения и библиотеки, нужные для корректной работы 
скриптов на языке python.
Для этого необходимо в терминале прописать команду:

*pip install -r requirements*

Далее необходимо прописать необходимые установки в config файле:

- username/password - поля, которые заполняются при создании mysql сервера
- host/port - поля, которые генерируются автоматически mysql (можно отредакитировать)
- database_name - имя базы данных

Дамп базы данных находится в папке [database](https://github.com/tquality-education/m.ivanyuk/blob/fourth_task/database/dump.sql)