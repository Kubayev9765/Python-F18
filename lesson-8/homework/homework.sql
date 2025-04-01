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
