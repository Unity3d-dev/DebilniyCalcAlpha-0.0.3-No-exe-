import os
import time
print("Прочитай Read me")
print("1 - Калькулятор")
print("2 - Альтернативеый запуск калькулятор(Если есть помехи)")
choice = input( "Введите команду: " )
if choice == "2": # Команда 2
    os.system("Start Helpmain.py")
elif choice == "1": # Команда 1
    os.system("cls")
    mode = input("Выберите режим(+, -, *, /,): ")
if mode == "+":
    os.system("Start Details\Subtractions\Plus.py")
elif mode == "-":
    os.system("Start Details\Subtractions\Minus.py")
elif mode == "*":
    os.system("Start Details\Subtractions\Multiplication.py")
elif mode == "/":
    os.system("Start Details\Subtractions\Division.py")
else:
    print("Ошибка, пожалуйста подождите . . .")
    time.sleep(2)
    os.system("cls")
    os.system("main.py")
