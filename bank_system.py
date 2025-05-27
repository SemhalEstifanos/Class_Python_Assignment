class Account:
    def __init__(self, name):
        self.name = name
        self.deposits = []
        self.withdrawals = []
        self.balance = 0
        self.loan = 0
        self.is_frozen = False
        self.min_balance = 0
        self.transactions = []
    def deposit(self, amount):
        if self.is_frozen:
            return "Account is frozen. Cannot deposit."
        if amount > 0:
            self.deposits.append(amount)
            self.balance += amount
            self.transactions.append(f"Deposited: {amount}")
            return f"Deposit successful. New balance: {self.balance}"
        return "Deposit amount must be positive."
    def withdraw(self, amount):
        if self.is_frozen:
            return "Account is frozen. Cannot withdraw."
        if amount <= 0:
            return "Withdrawal amount must be positive."
        if self.balance - amount >= self.min_balance:
            self.withdrawals.append(amount)
            self.balance -= amount
            self.transactions.append(f"Withdrew: {amount}")
            return f"Withdrawal successful. New balance: {self.balance}"
        return "Insufficient balance or below minimum balance."
    def transfer_funds(self, amount, other_account):
        if self.is_frozen:
            return "Account is frozen. Cannot transfer."
        if amount <= 0:
            return "Transfer amount must be positive."
        if self.balance - amount >= self.min_balance:
            self.balance -= amount
            other_account.balance += amount
            self.transactions.append(f"Transferred {amount} to {other_account.name}")
            other_account.transactions.append(f"Received {amount} from {self.name}")
            return f"Transferred {amount} to {other_account.name}"
        return "Transfer failed due to low balance or minimum balance restriction."
    def get_balance(self):
        return f"{self.name}'s balance is {self.balance}"
    def request_loan(self, amount):
        if self.is_frozen:
            return "Account is frozen. Cannot request loan."
        if amount > 0:
            self.loan += amount
            self.balance += amount
            self.transactions.append(f"Loan received: {amount}")
            return f"Loan of {amount} granted. New balance: {self.balance}"
        return "Loan amount must be positive."
    def repay_loan(self, amount):
        if self.is_frozen:
            return "Account is frozen. Cannot repay loan."
        if amount <= 0:
            return "Repayment amount must be positive."
        if amount > self.balance:
            return "Insufficient balance to repay loan."
        if amount > self.loan:
            return f"You only owe {self.loan}. Cannot overpay."
        self.balance -= amount
        self.loan -= amount
        self.transactions.append(f"Loan repaid: {amount}")
        return f"Repaid {amount}. Loan remaining: {self.loan}"
    def view_account_details(self):
        return f"Name: {self.name}, Balance: {self.balance}, Loan: {self.loan}, Frozen: {self.is_frozen}, Min Balance: {self.min_balance}"
    def change_account_owner(self, new_name):
        old_name = self.name
        self.name = new_name
        return f"Account owner changed from {old_name} to {new_name}"
    def account_statement(self):
        return [f"- {tx}" for tx in self.transactions]
    def apply_interest(self):
        if self.is_frozen:
            return "Account is frozen. Cannot apply interest."
        interest = self.balance * 0.05
        self.balance += interest
        self.transactions.append(f"Interest applied: {interest}")
        return f"Interest of {interest:.2f} applied. New balance: {self.balance:.2f}"
    def freeze_account(self):
        self.is_frozen = True
        return "Account has been frozen."
    def unfreeze_account(self):
        self.is_frozen = False
        return "Account has been unfrozen."
    def set_minimum_balance(self, amount):
        if amount >= 0:
            self.min_balance = amount
            return f"Minimum balance set to {self.min_balance}"
        return "Minimum balance must be zero or positive."
    def close_account(self):
        self.balance = 0
        self.loan = 0
        self.deposits.clear()
        self.withdrawals.clear()
        self.transactions.clear()
        return "Account closed. All balances cleared and transactions deleted."