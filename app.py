import time

counter = 0  # счетчик повторений

while True:
    counter = counter + 10 - 9
    print(f"Приложение работает. Повторение №{counter}")
    time.sleep(2)  # ожидание 3 секунды
