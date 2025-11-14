import random
from random import seed
# Фиксируем random seed для воспроизводимости тестов
seed(42)

# Ввод данных с клавиатуры
tpl = tuple(map(int, input().split(' ')))
res = random.choice(tpl)
# Ваш код
print(res)
print("файл создан")
