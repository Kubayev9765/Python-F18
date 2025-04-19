1.
from datetime import datetime


class Task:
    def __init__(self, title, description, due_date, status="Pending"):
        self.title = title
        self.description = description
        self.due_date = self._parse_due_date(due_date)
        self.status = status

    def _parse_due_date(self, due_date):
        if isinstance(due_date, str):
            try:
                return datetime.strptime(due_date, "%Y-%m-%d")
            except ValueError:
                raise ValueError("Due date must be in YYYY-MM-DD format")
        elif isinstance(due_date, datetime):
            return due_date
        else:
            raise TypeError("Due date must be a string or datetime object")

    def __str__(self):
        return f"Task(title='{self.title}', description='{self.description}', due_date='{self.due_date.date()}', status='{self.status}')"
    

task1 = Task(
    title="Complete Project Report",
    description="Write and submit the final project report to the manager.",
    due_date="2025-04-25",
    status="In Progress"
)

print(task1)

2.
class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        if isinstance(task, Task):
            self.tasks.append(task)
        else:
            raise TypeError("Only Task instances can be added.")

    def mark_task_complete(self, title):
        for task in self.tasks:
            if task.title == title:
                task.status = "Completed"
                return f"Task '{title}' marked as completed."
        return f"Task '{title}' not found."

    def list_all_tasks(self):
        return [str(task) for task in self.tasks]

    def list_incomplete_tasks(self):
        return [str(task) for task in self.tasks if task.status != "Completed"]
todo = ToDoList()

task1 = Task("Buy groceries", "Milk, eggs, bread", "2025-04-20")
task2 = Task("Call Alice", "Discuss the weekend plans", "2025-04-21")

todo.add_task(task1)
todo.add_task(task2)

print("All Tasks:")
for task in todo.list_all_tasks():
    print(task)

print("\nMarking 'Buy groceries' as complete:")
print(todo.mark_task_complete("Buy groceries"))

print("\nIncomplete Tasks:")
for task in todo.list_incomplete_tasks():
    print(task)

3.

from datetime import datetime

class Task:
    def __init__(self, title, description, due_date, status="Pending"):
        self.title = title
        self.description = description
        self.due_date = self._parse_due_date(due_date)
        self.status = status

    def _parse_due_date(self, due_date):
        if isinstance(due_date, str):
            try:
                return datetime.strptime(due_date, "%Y-%m-%d")
            except ValueError:
                raise ValueError("Due date must be in YYYY-MM-DD format")
        elif isinstance(due_date, datetime):
            return due_date
        else:
            raise TypeError("Due date must be a string or datetime object")

    def __str__(self):
        return f"[{self.status}] {self.title} (Due: {self.due_date.date()}) - {self.description}"

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        if isinstance(task, Task):
            self.tasks.append(task)
        else:
            raise TypeError("Only Task instances can be added.")

    def mark_task_complete(self, title):
        for task in self.tasks:
            if task.title.lower() == title.lower():
                task.status = "Completed"
                return f"Task '{title}' marked as completed."
        return f"Task '{title}' not found."

    def list_all_tasks(self):
        return [str(task) for task in self.tasks]

    def list_incomplete_tasks(self):
        return [str(task) for task in self.tasks if task.status != "Completed"]
def main():
    todo_list = ToDoList()

    while True:
        print("\n==== ToDo List Menu ====")
        print("1. Add a task")
        print("2. Mark task as complete")
        print("3. List all tasks")
        print("4. Show incomplete tasks")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            try:
                task = Task(title, description, due_date)
                todo_list.add_task(task)
                print("Task added successfully!")
            except Exception as e:
                print(f"Error adding task: {e}")

        elif choice == "2":
            title = input("Enter the title of the task to mark as complete: ")
            result = todo_list.mark_task_complete(title)
            print(result)

        elif choice == "3":
            print("\n--- All Tasks ---")
            tasks = todo_list.list_all_tasks()
            if tasks:
                for task in tasks:
                    print(task)
            else:
                print("No tasks found.")

        elif choice == "4":
            print("\n--- Incomplete Tasks ---")
            tasks = todo_list.list_incomplete_tasks()
            if tasks:
                for task in tasks:
                    print(task)
            else:
                print("No incomplete tasks.")

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

main()

4.
def test_application():
    print("=== Testing ToDoList Application ===")

    todo = ToDoList()

    task1 = Task("Finish Homework", "Math and science chapters", "2025-04-20")
    task2 = Task("Buy Groceries", "Milk, eggs, and bread", "2025-04-21")
    task3 = Task("Call Mom", "Check in and chat", "2025-04-22")

    print("\nAdding tasks...")
    todo.add_task(task1)
    todo.add_task(task2)
    todo.add_task(task3)

    print("\nAll Tasks:")
    for task in todo.list_all_tasks():
        print(task)

    print("\nMarking 'Buy Groceries' as complete:")
    print(todo.mark_task_complete("Buy Groceries"))

    print("\nAll Tasks After Update:")
    for task in todo.list_all_tasks():
        print(task)

    print("\nIncomplete Tasks:")
    for task in todo.list_incomplete_tasks():
        print(task)

test_application()


5.
class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author

    def __str__(self):
        return f"Title: {self.title}\nAuthor: {self.author}\nContent: {self.content}"


post1 = Post("My First Blog Post", "This is the content of the blog post.", "Alice")
print(post1)

6.
class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author

    def __str__(self):
        return f"Title: {self.title}\nAuthor: {self.author}\nContent: {self.content}\n"


class Blog:
    def __init__(self):
        self.posts = []

    def add_post(self, post):
        self.posts.append(post)

    def list_posts(self):
        if not self.posts:
            print("No posts available.")
        else:
            for post in self.posts:
                print(post)

    def display_posts_by_author(self, author_name):
        found = False
        for post in self.posts:
            if post.author == author_name:
                print(post)
                found = True
        if not found:
            print(f"No posts found by author: {author_name}")
blog = Blog()

post1 = Post("Python Basics", "Learn about variables and loops.", "Alice")
post2 = Post("Advanced Python", "Let's explore decorators.", "Bob")
post3 = Post("Python Tips", "Some useful Python tips.", "Alice")

blog.add_post(post1)
blog.add_post(post2)
blog.add_post(post3)

print("All Posts:")
blog.list_posts()

print("\nPosts by Alice:")
blog.display_posts_by_author("Alice")

7.
class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author

    def __str__(self):
        return f"Title: {self.title}\nAuthor: {self.author}\nContent: {self.content}\n"


class Blog:
    def __init__(self):
        self.posts = []

    def add_post(self, post):
        self.posts.append(post)

    def list_posts(self):
        if not self.posts:
            print("No posts available.\n")
        else:
            for post in self.posts:
                print(post)

    def display_posts_by_author(self, author_name):
        found = False
        for post in self.posts:
            if post.author.lower() == author_name.lower():
                print(post)
                found = True
        if not found:
            print(f"No posts found by author: {author_name}\n")


def main():
    blog = Blog()

    while True:
        print("=== Blog CLI ===")
        print("1. Add Post")
        print("2. List All Posts")
        print("3. Display Posts by Author")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            title = input("Enter post title: ")
            content = input("Enter post content: ")
            author = input("Enter author name: ")
            post = Post(title, content, author)
            blog.add_post(post)
            print("Post added successfully!\n")

        elif choice == "2":
            print("\nAll Posts:")
            blog.list_posts()

        elif choice == "3":
            author = input("Enter author name: ")
            print(f"\nPosts by {author}:")
            blog.display_posts_by_author(author)

        elif choice == "4":
            print("Exiting the Blog CLI. Goodbye!")
            break

        else:
            print("Invalid choice. Please select from 1 to 4.\n")


if __name__ == "__main__":
    main()

8.

from datetime import datetime


class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author
        self.timestamp = datetime.now()

    def __str__(self):
        return (f"Title: {self.title}\n"
                f"Author: {self.author}\n"
                f"Posted on: {self.timestamp.strftime('%Y-%m-%d %H:%M:%S')}\n"
                f"Content: {self.content}\n")


class Blog:
    def __init__(self):
        self.posts = []

    def add_post(self, post):
        self.posts.append(post)

    def list_posts(self):
        if not self.posts:
            print("No posts available.\n")
        else:
            for post in self.posts:
                print(post)

    def display_posts_by_author(self, author_name):
        found = False
        for post in self.posts:
            if post.author.lower() == author_name.lower():
                print(post)
                found = True
        if not found:
            print(f"No posts found by author: {author_name}\n")

    def delete_post(self, title):
        for post in self.posts:
            if post.title.lower() == title.lower():
                self.posts.remove(post)
                print(f"Post '{title}' deleted successfully.\n")
                return
        print(f"No post found with title: '{title}'\n")

    def edit_post(self, title):
        for post in self.posts:
            if post.title.lower() == title.lower():
                print("Leave field blank to keep current value.\n")
                new_title = input(f"New title (current: {post.title}): ").strip()
                new_content = input(f"New content (current: {post.content}): ").strip()
                new_author = input(f"New author (current: {post.author}): ").strip()

                if new_title:
                    post.title = new_title
                if new_content:
                    post.content = new_content
                if new_author:
                    post.author = new_author

                post.timestamp = datetime.now()
                print("Post updated successfully.\n")
                return
        print(f"No post found with title: '{title}'\n")

    def display_latest_posts(self, count=5):
        if not self.posts:
            print("No posts available.\n")
            return

        sorted_posts = sorted(self.posts, key=lambda p: p.timestamp, reverse=True)
        for post in sorted_posts[:count]:
            print(post)


def main():
    blog = Blog()

    while True:
        print("=== Blog CLI ===")
        print("1. Add Post")
        print("2. List All Posts")
        print("3. Display Posts by Author")
        print("4. Delete Post")
        print("5. Edit Post")
        print("6. Display Latest Posts")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ").strip()

        if choice == "1":
            title = input("Enter post title: ")
            content = input("Enter post content: ")
            author = input("Enter author name: ")
            post = Post(title, content, author)
            blog.add_post(post)
            print("Post added successfully!\n")

        elif choice == "2":
            print("\nAll Posts:")
            blog.list_posts()

        elif choice == "3":
            author = input("Enter author name: ")
            print(f"\nPosts by {author}:")
            blog.display_posts_by_author(author)

        elif choice == "4":
            title = input("Enter the title of the post to delete: ")
            blog.delete_post(title)

        elif choice == "5":
            title = input("Enter the title of the post to edit: ")
            blog.edit_post(title)

        elif choice == "6":
            try:
                count = int(input("How many latest posts to show? (default is 5): ") or 5)
            except ValueError:
                count = 5
            print(f"\nShowing {count} Latest Posts:")
            blog.display_latest_posts(count)

        elif choice == "7":
            print("Exiting the Blog CLI. Goodbye!")
            break

        else:
            print("Invalid choice. Please select from 1 to 7.\n")


if __name__ == "__main__":
    main()

9.
from datetime import datetime
import time  # Used to simulate time between posts





    blog = Blog()

    print("▶ Adding Posts...")
    post1 = Post("First Post", "This is the first post!", "Alice")
    time.sleep(1)  # Simulate delay for timestamps
    post2 = Post("Second Post", "Another day, another post.", "Bob")
    time.sleep(1)
    post3 = Post("Python Tips", "Use list comprehensions!", "Alice")

    blog.add_post(post1)
    blog.add_post(post2)
    blog.add_post(post3)

    print("\n Listing All Posts:")
    blog.list_posts()

    print("\n Displaying Posts by Author 'Alice':")
    blog.display_posts_by_author("Alice")

    print("\n Editing Post 'Second Post':")
    blog.edit_post("Second Post")  # Try entering new values when prompted

    print("\n Deleting Post 'First Post':")
    blog.delete_post("First Post")

    print("\n Listing All Posts After Deletion:")
    blog.list_posts()

    print("\n Displaying Latest 2 Posts:")
    blog.display_latest_posts(2)


if __name__ == "__main__":
    test_blog_system()

10.
class Account:
    def __init__(self, account_number, account_holder_name, balance=0.0):
        self.account_number = account_number
        self.account_holder_name = account_holder_name
        self.balance = balance

    def display_account_info(self):
        print(f"Account Number: {self.account_number}")
        print(f"Account Holder: {self.account_holder_name}")
        print(f"Balance: ${self.balance:.2f}")
my_account = Account("123456789", "John Doe", 1000.00)


my_account.display_account_info()
11.
class Account:
    def __init__(self, account_number, owner, balance=0):
        self.account_number = account_number
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        return False

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return True
        return False

    def get_balance(self):
        return self.balance

class Bank:
    def __init__(self):
        self.accounts = {}

    def add_account(self, account_number, owner, initial_balance=0):
        if account_number not in self.accounts:
            self.accounts[account_number] = Account(account_number, owner, initial_balance)
            return True
        return False  # Account already exists

    def check_balance(self, account_number):
        account = self.accounts.get(account_number)
        if account:
            return account.get_balance()
        return None  # Account not found

    def deposit_money(self, account_number, amount):
        account = self.accounts.get(account_number)
        if account:
            return account.deposit(amount)
        return False  # Account not found

    def withdraw_money(self, account_number, amount):
        account = self.accounts.get(account_number)
        if account:
            return account.withdraw(amount)
        return False  # Account not found

bank = Bank()
bank.add_account("123", "Alice", 1000)
bank.deposit_money("123", 500)
print("Balance:", bank.check_balance("123"))  # Output: Balance: 1500
bank.withdraw_money("123", 200)
print("Balance:", bank.check_balance("123"))  # Output: Balance: 1300

12.
class BankAccount:
    def __init__(self, account_number, account_holder):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = 0.0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}")

    def check_balance(self):
        print(f"Account Balance for {self.account_holder} (#{self.account_number}): ${self.balance:.2f}")


class BankingSystem:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number, account_holder):
        if account_number in self.accounts:
            print("Account already exists.")
        else:
            self.accounts[account_number] = BankAccount(account_number, account_holder)
            print(f"Account created for {account_holder} with account number {account_number}.")

    def get_account(self, account_number):
        return self.accounts.get(account_number, None)


def main():
    bank = BankingSystem()

    while True:
        print("\n=== Banking System Menu ===")
        print("1. Add Account")
        print("2. Check Balance")
        print("3. Deposit Money")
        print("4. Withdraw Money")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            acc_number = input("Enter account number: ")
            acc_holder = input("Enter account holder name: ")
            bank.create_account(acc_number, acc_holder)

        elif choice == '2':
            acc_number = input("Enter account number: ")
            account = bank.get_account(acc_number)
            if account:
                account.check_balance()
            else:
                print("Account not found.")

        elif choice == '3':
            acc_number = input("Enter account number: ")
            account = bank.get_account(acc_number)
            if account:
                try:
                    amount = float(input("Enter amount to deposit: "))
                    account.deposit(amount)
                except ValueError:
                    print("Invalid amount.")
            else:
                print("Account not found.")

        elif choice == '4':
            acc_number = input("Enter account number: ")
            account = bank.get_account(acc_number)
            if account:
                try:
                    amount = float(input("Enter amount to withdraw: "))
                    account.withdraw(amount)
                except ValueError:
                    print("Invalid amount.")
            else:
                print("Account not found.")

        elif choice == '5':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please select from 1 to 5.")


if __name__ == "__main__":
    main()
13.
class Account:
    def __init__(self, account_number, account_holder, balance=0.0, overdraft_limit=0.0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance
        self.overdraft_limit = overdraft_limit

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount:.2f} into account {self.account_number}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return False
        if self.balance - amount < -self.overdraft_limit:
            print("Insufficient funds: overdraft limit exceeded.")
            return False
        self.balance -= amount
        print(f"Withdrew ${amount:.2f} from account {self.account_number}")
        return True

    def transfer(self, target_account, amount):
        if self.withdraw(amount):
            target_account.deposit(amount)
            print(f"Transferred ${amount:.2f} to account {target_account.account_number}")
        else:
            print(f"Transfer of ${amount:.2f} to account {target_account.account_number} failed.")

    def display_details(self):
        print(f"Account Number: {self.account_number}")
        print(f"Account Holder: {self.account_holder}")
        print(f"Balance: ${self.balance:.2f}")
        print(f"Overdraft Limit: ${self.overdraft_limit:.2f}")
        print("-----------------------------")


if __name__ == "__main__":
    acc1 = Account("123456", "Alice", 1000.0, overdraft_limit=200.0)
    acc2 = Account("654321", "Bob", 500.0)

    acc1.display_details()
    acc2.display_details()

    acc1.transfer(acc2, 1100.0)  # Uses overdraft
    acc1.display_details()
    acc2.display_details()

    acc1.withdraw(200)  # Should fail due to overdraft exceeded

14.
# Define a basic Account class
class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{self.owner} deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"{self.owner} withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Insufficient funds or invalid amount.")

    def transfer(self, amount, other_account):
        if 0 < amount <= self.balance:
            self.balance -= amount
            other_account.balance += amount
            print(f"{self.owner} transferred ${amount} to {other_account.owner}.")
            print(f"{self.owner}'s balance: ${self.balance}")
            print(f"{other_account.owner}'s balance: ${other_account.balance}")
        else:
            print("Transfer failed. Check the amount and balance.")

    def __str__(self):
        return f"Account owner: {self.owner}, Balance: ${self.balance}"



if __name__ == "__main__":
    alice_account = Account("Alice", 1000)
    bob_account = Account("Bob", 500)

    print(alice_account)
    print(bob_account)

    alice_account.deposit(200)

    bob_account.withdraw(100)

    alice_account.transfer(300, bob_account)

    print(alice_account)







