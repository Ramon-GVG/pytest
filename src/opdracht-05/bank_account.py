"""
Opdracht 5: Bankrekening

Deze class is al af. Jij schrijft de tests in test_bank_account.py

Let op: deze class geeft bij een fout GEEN False terug, maar gooit
een error (raise). Dat is de gebruikelijke manier in Python.
"""


class InsufficientFundsError(Exception):
    """Wordt gegooid als er te weinig saldo is."""


class BankAccount:
    """Een simpele betaalrekening."""

    def __init__(self, owner, balance=0.0):
        if balance < 0:
            raise ValueError("Beginsaldo mag niet negatief zijn")
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        """Stort een bedrag op de rekening."""
        if amount <= 0:
            raise ValueError("Bedrag moet groter dan 0 zijn")
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        """Neemt een bedrag op van de rekening."""
        if amount <= 0:
            raise ValueError("Bedrag moet groter dan 0 zijn")
        if amount > self.balance:
            raise InsufficientFundsError("Saldo te laag")
        self.balance -= amount
        return self.balance

    def transfer_to(self, other_account, amount):
        """Maakt een bedrag over naar een andere rekening."""
        if not isinstance(other_account, BankAccount):
            raise TypeError("Kan alleen overmaken naar een BankAccount")
        self.withdraw(amount)
        other_account.deposit(amount)
        return self.balance
