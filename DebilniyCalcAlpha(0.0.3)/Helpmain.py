import os
import time
mode = input("Выберите режим(+, -, *, /,): ")
if mode == "+":
    os.system("Start Details\Help\LaunchPlus.py")
elif mode == "-":
    os.system("Start Details\Help\LaunchMinus.py")
elif mode == "*":
    os.system("Start Details\Help\LaunchMultiplication.py")
elif mode == "/":
    os.system("Start Details\Help\LaunchDivision.py")
else:
    print("Ошибка, пожалуйста подождите . . .")
    time.sleep(2)
    os.system("cls")
    os.system("Helpmain.py")
