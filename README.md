
# TCP сервер

Получает данные, переводит их в нужный формат и раскидывает этот формат по необходимым файликам.

## Установка

Для взаимодействия с проектом и его библиотеками используется пакетный менеджер poetry.
Поэтому для установки необходимых пакетов нужно перейти в директарий с проектом и прописать 

```bash
  poetry install
```

## Использование

По умолчанию все данные для подключения содержаться в tct_server/main.py. 
Для запуска проекта необходим ввести следующее:

```bash
  poetry run main
```

Это запустит наш сервер и он будет готов к подключению.

Для того чтобы подключиться к нему (можете делать это по разному, я буду использовать утилиту telnet), нам необходимо узнать ip сервера и запустить на нем следующую команду:

```bash
  ip -4 address
```

Через этот ip и можно подключаться.
На клиенте пишем следующее:

```bash
    telnet 'server_ip' 8080
```
8080 - порт заданный программой по умолчанию, его можно менять.
И в появившемся поле вбиваем информацию, что мы хотим отправить на сервер.

## Логи
Все логи можно найти в файле tcp_server/logs/info.log

```bash
    less tcp_server/logs/info.log
```
## Информация
Вся форматированная информация лежит в папочке data, в ней она делиться еще на два файл: файл со всей входящей датой (all_income.log) и с датой содержащуе подходящую нам группу (main_group.log).