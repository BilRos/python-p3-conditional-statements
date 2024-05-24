#!/usr/bin/env python3

def admin_login(username, password):
    # your code here
    pass
    if (username == "ADMIN" ) and (password == 12345):
       return "Access granted"
    elif(username == "admin") and (password == 12345):
        return "Access granted"
    else:
       return "Access denied"

admin_login("sudo", "12345")
admin_login("admin", "12345")
admin_login("ADMIN", "12345")

def hows_the_weather(temperature):
    # your code here
    pass
    if temperature < 40:
        return "Its brisk out there!"
    elif temperature >= 40 and temperature <= 65:
        return "It's a little chilly out there!"
    elif temperature > 85:
        return "Its too dang hot out there!"
    else:
        return "Its perfect out there!"

hows_the_weather(33)
hows_the_weather(99)
hows_the_weather(75)


def fizzbuzz(num):
    # your code here
    pass
    if num%3 == 0:
        return "Fizz"
    elif num%5 == 0:
        return "Buzz"
    elif num%3 == 0 and num%5 == 0:
        return "FizzBuzz"
    else:
        return num
fizzbuzz(1)
fizzbuzz(2)
fizzbuzz(3)
fizzbuzz(4)
fizzbuzz(5)
fizzbuzz(15)


def calculator(operation, num1, num2):
    # your code here
    pass
    if (operation == "+"):
        return num1 + num2
    elif (operation == "-"):
        return num1 - num2
    elif (operation == "*"):
        return num1 * num2
    elif (operation == "/"):
        return num1 / num2
    else:
        print(f"Invalid operation!")
        return None
calculator("+", 1, 1)
calculator("-", 3, 1)
calculator("*", 3, 2)
calculator("/", 4, 2)
calculator("nope", 4, 2)