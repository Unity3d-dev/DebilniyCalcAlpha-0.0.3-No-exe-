import os
import time
mode = input("Выберите режим(+, -, *, /,): ")
if mode == "+":
    os.system("Start Details\Subtractions\LaunchPlus.py")
elif mode == "-":
    os.system("Start Details\Subtractions\LaunchMinus.py")
elif mode == "*":
    os.system("Start Details\Subtractions\LaunchMultiplication.py")
elif mode == "/":
    os.system("Start Details\Subtractions\LaunchDivision.py")
else:
    print("Ошибка, пожалуйста подождите . . .")
    time.sleep(2)
    os.system("cls")
    os.system("Helpmain.py")
