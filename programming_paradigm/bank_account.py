#Create a simple bank account class
#Use of OOP fundamentals to implement a BankAccount class
#to encapsulates banking operations

#Class definition
class BankAccount:
	def __init__(self, initial_balance=0.0):
		self.account_balance = initial_balance

	def deposit(self, amount):
		if amount > 0:
			self.account_balance += amount
		else:
			print("Amount entered must be positive and greater than zero")

	def withdraw(self, amount):
		if amount <= 0:
			print("Amount withdrawal should be greater than 0")
			return False
		elif amount > self.account_balance:
			print("Insufficient account balance")
			return False
		else:
			self.account_balance -= amount
			return True

	def display_balance(self):
		print(f"Current Balance: ${self.account_balance:.2f}.")
