# Деревья

## Несбалансированное

### Случайные числа

| Элементы | Вставка | Поиск | Удаление |
|:--------:|---------|-------|----------|
|   100    | 0 ms    | 0 ms  | 2 ms     |
|  1 000   | 4 ms    | 0 ms  | 1 ms     |
|  10 000  | 48 ms   | 3 ms  | 10 ms    |
| 100 000  | 2094 ms | 16 ms | 221 ms   |


### Возрастающие числа

| Элементы | Вставка | Поиск   | Удаление |
|:--------:|---------|---------|----------|
|   100    | 1 ms    | 0 ms    | 0 ms     |
|  1 000   | 64 ms   | 12 ms   | 16 ms    |
|  10 000  | 6211 ms | 504 ms  | 549 ms   |
| 100 000  | timeout | timeout | timeout  |

### Вывод

Несбалансированное дерево эффективно работает при +- равномерно распределенных данных,
а в худшем случае ведет себя как связанный список.

## Сбалансированное

### Случайные числа

| Элементы | Вставка | Поиск | Удаление |
|:--------:|---------|-------|----------|
|   100    | 2 ms    | 0 ms  | 0 ms     |
|  1 000   | 13 ms   | 0 ms  | 2 ms     |
|  10 000  | 189 ms  | 3 ms  | 23 ms    |
| 100 000  | 2614 ms | 51 ms | 267 ms   |

### Возрастающие числа

| Элементы | Вставка | Поиск | Удаление |
|:--------:|---------|-------|----------|
|   100    | 1 ms    | 0 ms  | 0 ms     |
|  1 000   | 14 ms   | 8 ms  | 1 ms     |
|  10 000  | 178 ms  | 3 ms  | 29 ms    |
| 100 000  | 2226 ms | 51 ms | 250 ms   |

В отличии от обычного дерева сбалансированное показывает чуть более медленную вставку
на случайных числах (из за перебалансировки). Однако на других операциях производительность
не зависит от порядка вставки, то есть и средний, и худший случай работают с одинаковой скоростью.

