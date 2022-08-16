# Отус алгоритмы и структуры данных
## Куприянов Павел
### Тестер
```
Фреймворк для запуска тестов

positional arguments:
  task                  Имя каталога для запуска тестов

options:
  -h, --help            show this help message and exit
  -c CASES, --cases CASES
                        Путь к каталогу с тестами относительно module
  -i INPUT_EXT, --input_ext INPUT_EXT
                        Разрешение файлов входных данных
  -o OUTPUT_EXT, --output_ext OUTPUT_EXT
                        Разрешение файлов результатов
  -m MODULE, --module MODULE
                        Модуль python с кодом решения задачи
  -f FUNCTION, --function FUNCTION
                        Имя функции в модуле
  -d DESCRIPTION, --description DESCRIPTION
                        Путь к файлу с описанием задачи
  -t TESTS, --tests TESTS
                        Список имен файлов для тестов, разделенных запятой

 ```
#### Запуск тестера:
`python3 -m tester <имя пакета, например: tickets>`