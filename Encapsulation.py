# File: encapsulation_example.py
# Description: A simple example demonstrating the concept of Encapsulation in OOPS using Python.

# Define a class named 'BankAccount'
class BankAccount:
    # Constructor method (initializes object attributes)
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder  # Public attribute
        self.__balance = balance              # Private attribute (encapsulated)

    # Public method to deposit money
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ${amount}. New balance: ${self.__balance}")
        else:
            print("Deposit amount must be positive.")

    # Public method to withdraw money
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.__balance}")
        else:
            print("Invalid withdrawal amount or insufficient balance.")

    # Getter method to access the private balance attribute
    def get_balance(self):
        return self.__balance

    # Setter method to modify the private balance attribute (with validation)
    def set_balance(self, balance):
        if balance >= 0:
            self.__balance = balance
            print(f"Balance set to ${self.__balance}")
        else:
            print("Balance cannot be negative.")

    # Magic method (string representation of the object)
    def __str__(self):
        return f"BankAccount(Account Holder: {self.account_holder}, Balance: ${self.__balance})"

# Main function to demonstrate encapsulation
if __name__ == "__main__":
    # Create an object (instance) of the BankAccount class
    account = BankAccount("John Doe", 1000)

    # Print account details using __str__ method
    print(account)

    # Access public attribute
    print(f"Account Holder: {account.account_holder}")

    # Attempt to access private attribute directly (will raise an error)
    try:
        print(account.__balance)  # This will fail
    except AttributeError as e:
        print(f"Error: {e}")

    # Use public methods to interact with private attributes
    account.deposit(500)    # Deposit $500
    account.withdraw(200)    # Withdraw $200
    account.withdraw(2000)   # Attempt to withdraw $2000 (insufficient balance)

    # Use getter method to access private balance
    print(f"Current Balance: ${account.get_balance()}")

    # Use setter method to modify private balance
    account.set_balance(1500)  # Set balance to $1500
    account.set_balance(-100)  # Attempt to set negative balance (invalid)
