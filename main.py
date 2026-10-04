#Bank Account Class
class BankAccount:
    def __init__(self, account_holder, balance=0.0):
        self.account_holder = account_holder
        self.balance = float(balance)

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Deposited: " + str(amount) + ". New balance: " + str(self.balance))
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount.")
        elif amount > self.balance:
            print("Insufficient funds! Balance is only: " + str(self.balance))
        else:
            self.balance -= amount
            print("Withdrew: " + str(amount) + ". New balance: " + str(self.balance))

    def display_balance(self):
        print("Account: " + str(self.account_holder) + " | Balance: " + str(self.balance))


# Test run
account = BankAccount("Alice", 100.0)
account.display_balance()
account.deposit(50.0)
account.withdraw(30.0)
account.withdraw(200.0)

print("-"*50)
#Library Management Class
class Book:
    def __init__(self, isbn: str, title: str, author: str):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.is_issued = False

    def __str__(self):
        status = "Issued" if self.is_issued else "Available"
        return f"'{self.title}' by {self.author} (ISBN: {self.isbn}) [{status}]"


class Library:
    def __init__(self, name: str):
        self.name = name
        self.books: dict[str, Book] = {}

    def add_book(self, book: Book) -> None:
        if book.isbn in self.books:
            print(f"Book with ISBN {book.isbn} already exists in catalog.")
            return
        self.books[book.isbn] = book
        print(f"Added: {book.title}")

    def remove_book(self, isbn: str) -> None:
        if isbn not in self.books:
            print(f"No book found with ISBN {isbn}.")
            return
        removed = self.books.pop(isbn)
        print(f"Removed: {removed.title}")

    def issue_book(self, isbn: str) -> None:
        book = self.books.get(isbn)
        if not book:
            print(f"No book found with ISBN {isbn}.")
            return
        if book.is_issued:
            print(f"'{book.title}' is currently checked out.")
            return
        book.is_issued = True
        print(f"Issued: '{book.title}'")

    def return_book(self, isbn: str) -> None:
        book = self.books.get(isbn)
        if not book:
            print(f"No record of book with ISBN {isbn}.")
            return
        if not book.is_issued:
            print(f"'{book.title}' was not marked as issued.")
            return
        book.is_issued = False
        print(f"Returned: '{book.title}'")


# Example usage:
lib = Library("City Public Library")
b1 = Book("978-0141439518", "Pride and Prejudice", "Jane Austen")
b2 = Book("978-0451524935", "1984", "George Orwell")

lib.add_book(b1)
lib.add_book(b2)
lib.issue_book("978-0141439518")
lib.issue_book("978-0141439518")  # Fails: already checked out
lib.return_book("978-0141439518")
lib.remove_book("978-0451524935")

print("-"*50)
#Calculator CLass With Exception Handling
class Calculator:
    @staticmethod
    def _validate_operands(a, b):
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Both operands must be numeric (int or float).")

    def add(self, a: float, b: float) -> float:
        self._validate_operands(a, b)
        return a + b

    def subtract(self, a: float, b: float) -> float:
        self._validate_operands(a, b)
        return a - b

    def multiply(self, a: float, b: float) -> float:
        self._validate_operands(a, b)
        return a * b

    def divide(self, a: float, b: float) -> float:
        self._validate_operands(a, b)
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return a / b

    def power(self, a: float, b: float) -> float:
        self._validate_operands(a, b)
        if a < 0 and not float(b).is_integer():
            raise ValueError("Negative base cannot be raised to a fractional exponent.")
        return a ** b

    def calculate(self, operation: str, a, b):
        """Unified runner with comprehensive exception handling."""
        ops = {
            "+": self.add,
            "-": self.subtract,
            "*": self.multiply,
            "/": self.divide,
            "^": self.power
        }

        try:
            if operation not in ops:
                raise ValueError(f"Unsupported operation '{operation}'. Use: {list(ops.keys())}")

            result = ops[operation](a, b)
            return result

        except ZeroDivisionError as err:
            print(f"Math Error: {err}")
        except TypeError as err:
            print(f"Type Error: {err}")
        except ValueError as err:
            print(f"Value Error: {err}")
        except Exception as err:
            print(f"Unexpected error: {err}")
        return None


# Example usage:
calc = Calculator()

print("10 / 2 =", calc.calculate("/", 10, 2))
calc.calculate("/", 10, 0)  # Triggers ZeroDivisionError
calc.calculate("+", 5, "ten")  # Triggers TypeError
calc.calculate("%", 10, 2)  # Triggers ValueError (unknown operator)
calc.calculate("^", -4, 0.5)  # Triggers ValueError (complex result)