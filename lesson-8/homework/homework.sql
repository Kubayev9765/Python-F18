1.
def Sum_Zero (a, b):
 
    try:
        sum=a/b
        print(f"Natija: {sum}")
    except ZeroDivisionError:
        print("0 soniga bo'lish mumkin emas")
  
a = float(input("1- sonni kiriting: "))
b = float(input("2- sonni kiriting: "))
Sum_Zero(a, b)

2.
def Butun_son():
    Son = input("Son kiriting: ")
    if not Son.strip().lstrip('-').isdigit():
        raise ValueError("Kiritilgan son butun son emas.")
    return int(Son)

try:
    number = Butun_son()
    print(f"Butun son kiriting!: {number}")
except ValueError as e:
    print(f"Xatolik: {e}")

