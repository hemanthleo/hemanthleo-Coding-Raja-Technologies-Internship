# expense.py
class Expense:
    def __init__(self, name, amount, category):
        self.name = name
        self.amount = amount
        self.category = category

    def __repr__(self):
        return f"Expense(name={self.name}, amount={self.amount}, category={self.category})"
