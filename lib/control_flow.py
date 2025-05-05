#!/usr/bin/env python3

def admin_login(username, password):
    # your code here
    if (username == "ADMIN" or username =="admin") and (password == "12345"):
        return "Access granted"
    else:
        return "Access denied"
    # pass

def hows_the_weather(temperature):
    # your code here
    if temperature > 85:
        return "It's too dang hot out there!"
    elif temperature >= 40 and temperature < 65:
        return "It's a little chilly out there!"
    elif temperature < 40:
        return "It's brisk out there!"
    else:
        return "It's perfect out there!"
    # pass

def fizzbuzz(num):
    # your code here
    if (num % 3 == 0) and num % 5 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return num
    # pass

def calculator(operation, num1, num2):
    # your code here
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        return num1 / num2
    else:
        print("Invalid operation!")
        return None
    # pass



# Test calls # run: python3 lib/control_flow.py
print(admin_login("admin", "12345"))   # prints: Access granted
print (admin_login("ADMIN", "12345"))   # "Access granted"
print(admin_login("sudo", "12345"))    # Should print: Access denied