1.
python -m venv myenv

myenv\Scripts\activate

pip install numpy pandas matplotlib

pip freeze > requirements.txt

pip install -r requirements.txt

2.
# math_operations.py

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Bo'lishda nolga bo'lish mumkin emas.")
    return a / b

# string_utils.py

def reverse_string(s):
    return s[::-1]

def count_vowels(s):
    vowels = 'aeiouAEIOU'
    return sum(1 for char in s if char in vowels)

from math_operations import add, subtract, multiply, divide
from string_utils import reverse_string, count_vowels

print(add(5, 3))               # 8
print(subtract(10, 4))         # 6
print(multiply(6, 7))          # 42
print(divide(8, 2))            # 4.0

print(reverse_string("hello")) # "olleh"
print(count_vowels("hello"))   # 2


3.
geometry/
│
├── __init__.py
└── doira.py

# doira.py

import math

def calculate_area(radius):
    return math.pi * radius ** 2

def calculate_circumference(radius):
    return 2 * math.pi * radius


file_operations/
│
├── __init__.py
├── file_reader.py
└── file_writer.py
# file_reader.py

def read_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        return "Fayl topilmadi."


# file_writer.py

def write_file(file_path, content):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)


# main.py

from geometry.doira import calculate_area, calculate_circumference
from file_operations.file_reader import read_file
from file_operations.file_writer import write_file

# Geometry
radius = 5
print(f"Yuza: {calculate_area(radius)}")
print(f"Aylana uzunligi: {calculate_circumference(radius)}")

# Fayl bilan ishlash
write_file('test.txt', 'Salom, dunyo!')
print(read_file('test.txt'))

