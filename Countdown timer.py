#Countdown timer
import time


def  countdown_timer (seconds):
    for i in range(seconds, 0, -1):
        print(i)
        time.sleep(1)
    print("Time up!better luck next time")
    print("This Program is created by Muhammad Hamza")

countdown_timer(int(input("Enter the number of seconds: ")))
