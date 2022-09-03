# Отус алгоритмы и структуры данных

## Куприянов Павел

### Тестер

```
usage: python3 -m tester [-h] [-c CASES] [-i INPUT_EXT] [-o OUTPUT_EXT] [-m MODULE] [-f FUNCTION] [-d DESCRIPTION] [-t TESTS] [-s | --short | --no-short] [--timeout TIMEOUT]
                   task

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
  -s, --short, --no-short
                        Сокращенный формат вывода (default: False)
  --timeout TIMEOUT     Максимальное время выполнения функции (секунды)

 ```

#### Запуск тестера:

* Счастливые билеты: `python3 -m tester tickets`
* Возведение в степень через разложение: `python3 -m tester power --module power_log_n`
* Итеративное возведение в степень: `python3 -m tester power --module power_n`
* Рекурсивное число Фибоначчи: `python3 -m tester fibo --module fibo_recursive`
* Итеративное число Фибоначчи: `python3 -m tester fibo --module fibo_iter`
* Матричное число Фибоначчи: `python3 -m tester fibo --module fibo_matrix`
* Простые числа квадрат: `python3 -m tester primes --module primes_square`
* Простые числа оптимизации: `python3 -m tester primes --module primes_cache`
* Простые числа Эратосфен: `python3 -m tester primes --module primes_eratosphene`