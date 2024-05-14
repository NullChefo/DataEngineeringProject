import math
import re
import datetime
import random
import json
import requests
from bs4 import BeautifulSoup


# 1. Hello World:
print("Hello, World!")

# 2. Variables and arithmetic:
a = 10
b = 5
c = a + b

# 3. User input:
name = input("Enter your name: ")
print("Hello, " + name)

# 4. Conditional statement:
num = 7
if num > 0:
    print("Positive number")
elif num == 0:
    print("Zero")
else:
    print("Negative number")


# 5. Loop:
for i in range(5):
    print(i)


# 6. List manipulation:
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
print(fruits)


# 7. String manipulation:
sentence = "Python is awesome"
print(sentence.upper())
print(sentence.split())


# 8. Dictionary:
person = {"name": "John", "age": 30, "city": "New York"}
print(person["name"])

# 9. Functions:
def square(x):
    return x ** 2

print(square(5))

# 10. File handling:
file = open("example.txt", "w")
file.write("Hello, World!")
file.close()


# 11. Exception handling:
try:
    num = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")


# 12. Regular expressions:
text = "Hello, my email is example@example.com"
pattern = r'\w+@\w+\.\w+'
match = re.search(pattern, text)
print(match.group())

# 13. List comprehension:
numbers = [1, 2, 3, 4, 5]
squared = [x ** 2 for x in numbers]
print(squared)

# 14. Lambda functions:
multiply = lambda x, y: x * y
print(multiply(3, 4))


# 15. Date and time:

now = datetime.datetime.now()
print(now)


# 16. Random numbers:

number = random.randint(1, 10)
print(number)


# 17. JSON handling:
data = '{"name": "John", "age": 30}'
person = json.loads(data)
print(person["name"])

# 18. Web scraping with Beautiful Soup:

url = "https://example.com"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
title = soup.title.string
print(title)

