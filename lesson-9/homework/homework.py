1.
import math
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

  radius = float(input("Enter the radius of the circle: "))
  circle = Circle(radius)
    
  print(f"Area of the circle: {circle.area():.2f}")
  print(f"Perimeter of the circle: {circle.perimeter():.2f}")

2.
from datetime import datetime

class Person:
    def __init__(self, name, country, date_of_birth):
        self.name = name
        self.country = country
        self.date_of_birth = datetime.strptime(date_of_birth, "%Y-%m-%d")

    def get_age(self):
        today = datetime.today()
        age = today.year - self.date_of_birth.year
        if (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day):
            age -= 1
        return age


name = input("Enter the person's name: ")
country = input("Enter the person's country: ")
dob = input("Enter the person's date of birth (YYYY-MM-DD): ")

    person = Person(name, country, dob)
    print(f"{person.name} from {person.country} is {person.get_age()} years old.")

3.
class Kalkulyator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def qoshish(self):
        return self.a + self.b

    def ayirish(self):
        return self.a - self.b

    def kopaytirish(self):
        return self.a * self.b

    def bolish(self):
        try:
            return self.a / self.b
        except ZeroDivisionError:
            return "Xatolik: 0 ga bo'lish mumkin emas."

# Foydalanuvchidan sonlar kiritishni so'raymiz
try:
    a = float(input("Birinchi sonni kiriting: "))
    b = float(input("Ikkinchi sonni kiriting: "))

    calc = Kalkulyator(a, b)

    print("\nNatijalar:")
    print(f"Qo‘shish: {calc.qoshish()}")
    print(f"Ayirish: {calc.ayirish()}")
    print(f"Ko‘paytirish: {calc.kopaytirish()}")
    print(f"Bo‘lish: {calc.bolish()}")

except ValueError:
    print("Xatolik: Faqat raqam kiriting.")



4.
import math

# Asosiy sinf
class Shape:
    def area(self):
        raise NotImplementedError("Area metodi aniqlanmagan.")

    def perimeter(self):
        raise NotImplementedError("Perimeter metodi aniqlanmagan.")

    def __str__(self):
        return "Bu biror shakl (Shape)."

# Doira (Circle) sinfi
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

    def __str__(self):
        return f"Doira: radius = {self.radius}"

# Uchburchak (Triangle) sinfi (tekis tomonli uchun)
class Triangle(Shape):
    def __init__(self, a, b, c):  # 3 ta tomon
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        s = self.perimeter() / 2  # yarim perimetr
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))  # Geron formulasi

    def __str__(self):
        return f"Uchburchak: tomonlar = {self.a}, {self.b}, {self.c}"

# Kvadrat (Square) sinfi
class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

    def perimeter(self):
        return 4 * self.side

    def __str__(self):
        return f"Kvadrat: tomon = {self.side}"

# --- TEST QISMI ---

shakllar = [
    Circle(5),
    Triangle(3, 4, 5),
    Square(6)
]

for shakl in shakllar:
    print(shakl)
    print(f"Yuza: {shakl.area():.2f}")
    print(f"Perimetr: {shakl.perimeter():.2f}")
    print("-" * 30)


5.
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)
    
    def _insert_recursive(self, current_node, value):
        if value < current_node.value:
            if current_node.left is None:
                current_node.left = Node(value)
            else:
                self._insert_recursive(current_node.left, value)
        elif value > current_node.value:
            if current_node.right is None:
                current_node.right = Node(value)
            else:
                self._insert_recursive(current_node.right, value)
        else:
            # Duplicate values are not inserted in this BST
            print(f"Value {value} already exists in the tree.")

    def search(self, value):
        return self._search_recursive(self.root, value)
    
    def _search_recursive(self, current_node, value):
        if current_node is None:
            return False
        if value == current_node.value:
            return True
        elif value < current_node.value:
            return self._search_recursive(current_node.left, value)
        else:  # value > current_node.value
            return self._search_recursive(current_node.right, value)

    def inorder_traversal(self):
        return self._inorder_recursive(self.root)
    
    def _inorder_recursive(self, node):
        if node is None:
            return []
        return (
            self._inorder_recursive(node.left) +
            [node.value] +
            self._inorder_recursive(node.right)
        )

bst = BinarySearchTree()
elements = [50, 30, 70, 20, 40, 60, 80]
for elem in elements:
    bst.insert(elem)
    
print("Inorder Traversal:", bst.inorder_traversal())
print("Search for 60:", bst.search(60))
print("Search for 25:", bst.search(25))

6.
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            return "Stack is empty. Cannot pop."
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            return "Stack is empty."
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


  stack = Stack()
    
  print("Pushing 10, 20, 30 onto stack...")
  stack.push(10)
  stack.push(20)
  stack.push(30)

print("Current top element:", stack.peek())
print("Stack size:", stack.size())

print("Popping element:", stack.pop())
print("Current top element after pop:", stack.peek())
print("Stack size after pop:", stack.size())

print("Popping all elements...")
stack.pop()
stack.pop()
print("Trying to pop from empty stack:", stack.pop())

7.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        current = self.head
        if not current:
            print("The linked list is empty.")
            return
        print("Linked List:", end=" ")
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def insert(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def delete(self, key):
        current = self.head
        previous = None

        while current and current.data != key:
            previous = current
            current = current.next

        if not current:
            print(f"Value {key} not found in the list.")
            return

        if not previous:
            self.head = current.next  # Node to delete is head
        else:
            previous.next = current.next
        print(f"Deleted node with value {key}.")

ll = LinkedList()
    
ll.insert(10)
ll.insert(20)
ll.insert(30)
ll.display()

ll.delete(20)
ll.display()

ll.delete(40)
ll.display()

8.

class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_item(self, item_name, price, quantity=1):
        if item_name in self.items:
            self.items[item_name]['quantity'] += quantity
        else:
            self.items[item_name] = {'price': price, 'quantity': quantity}
        print(f"Added {quantity} x {item_name}(s) to the cart.")

    def remove_item(self, item_name, quantity=1):
        if item_name in self.items:
            if self.items[item_name]['quantity'] > quantity:
                self.items[item_name]['quantity'] -= quantity
                print(f"Removed {quantity} x {item_name}(s) from the cart.")
            else:
                del self.items[item_name]
                print(f"Removed {item_name} completely from the cart.")
        else:
            print(f"{item_name} not found in the cart.")

    def calculate_total(self):
        total = sum(item['price'] * item['quantity'] for item in self.items.values())
        return total

    def show_cart(self):
        if not self.items:
            print("The cart is empty.")
            return
        print("Shopping Cart Contents:")
        for item, details in self.items.items():
            print(f"{item}: ${details['price']} x {details['quantity']}")
        print(f"Total: ${self.calculate_total():.2f}")

cart = ShoppingCart()
cart.add_item("Apple", 0.99, 3)
cart.add_item("Banana", 0.50, 5)
cart.show_cart()
cart.remove_item("Apple", 2)
cart.show_cart()
cart.remove_item("Apple")
cart.show_cart()


9.
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)
        print(f"Pushed '{item}' onto the stack.")

    def pop(self):
        if self.is_empty():
            print("Stack is empty. Nothing to pop.")
            return None
        item = self.stack.pop()
        print(f"Popped '{item}' from the stack.")
        return item

    def display(self):
        if self.is_empty():
            print("The stack is empty.")
        else:
            print("Stack contents (top to bottom):")
            for item in reversed(self.stack):
                print(item)

    def is_empty(self):
        return len(self.stack) == 0


stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
stack.display()
stack.pop()
stack.display()


10.
class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)
        print(f"Enqueued '{item}' to the queue.")

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty. Nothing to dequeue.")
            return None
        item = self.queue.pop(0)
        print(f"Dequeued '{item}' from the queue.")
        return item

    def display(self):
        if self.is_empty():
            print("The queue is empty.")
        else:
            print("Queue contents (front to rear):")
            for item in self.queue:
                print(item)

    def is_empty(self):
        return len(self.queue) == 0


queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.display()
queue.dequeue()
queue.display()
queue.dequeue()
queue.display()

11.

class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number, initial_balance=0):
        if account_number in self.accounts:
            print(f"Account with number {account_number} already exists.")
        else:
            self.accounts[account_number] = initial_balance
            print(f"Account {account_number} created with balance ${initial_balance:.2f}.")

    def deposit(self, account_number, amount):
        if account_number not in self.accounts:
            print(f"Account {account_number} does not exist.")
        elif amount <= 0:
            print("Deposit amount must be positive.")
        else:
            self.accounts[account_number] += amount
            print(f"Deposited ${amount:.2f} into account {account_number}. Current balance: ${self.accounts[account_number]:.2f}")

    def withdraw(self, account_number, amount):
        if account_number not in self.accounts:
            print(f"Account {account_number} does not exist.")
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
        elif self.accounts[account_number] < amount:
            print("Insufficient funds.")
        else:
            self.accounts[account_number] -= amount
            print(f"Withdrew ${amount:.2f} from account {account_number}. Current balance: ${self.accounts[account_number]:.2f}")

    def check_balance(self, account_number):
        if account_number not in self.accounts:
            print(f"Account {account_number} does not exist.")
        else:
            print(f"Account {account_number} balance: ${self.accounts[account_number]:.2f}")

    def transfer(self, from_account, to_account, amount):
        if from_account not in self.accounts or to_account not in self.accounts:
            print("One or both accounts do not exist.")
        elif amount <= 0:
            print("Transfer amount must be positive.")
        elif self.accounts[from_account] < amount:
            print("Insufficient funds for transfer.")
        else:
            self.accounts[from_account] -= amount
            self.accounts[to_account] += amount
            print(f"Transferred ${amount:.2f} from account {from_account} to account {to_account}.")
            print(f"New balance of {from_account}: ${self.accounts[from_account]:.2f}")
            print(f"New balance of {to_account}: ${self.accounts[to_account]:.2f}")


bank = Bank()
    
bank.create_account(101, 500)
bank.create_account(102, 1000)

bank.deposit(101, 200)
bank.deposit(102, 300)

bank.check_balance(101)
bank.check_balance(102)

bank.withdraw(101, 100)
bank.withdraw(102, 500)

bank.transfer(101, 102, 150)
    
bank.check_balance(101)
bank.check_balance(102)






