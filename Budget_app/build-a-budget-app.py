** start of main.py **

class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=''):
        d = {'amount': amount, 'description': description}
        self.ledger.append(d)

    def withdraw(self, amount, description=''):
        if self.check_funds(amount):
            d = {'amount': -amount, 'description': description}
            self.ledger.append(d)
            return True
        return False

    def get_balance(self):
        balance = 0
        for elem in self.ledger:
            balance += elem['amount']
        return balance

    def check_funds(self, amount):
        if amount > self.get_balance():
            return False
        return True

    def transfer(self, amount, category):
        if self.withdraw(amount, f"Transfer to {category.name}"):
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def __str__(self):
        output = f"{self.name:*^30}\n"
        for elem in self.ledger:
            # Format: Description (first 23 chars) + Amount (7 chars right aligned, 2 decimals)
            output += f"{elem['description'][0:23]:<23}{elem['amount']:>7.2f}\n"
        output += f"Total: {self.get_balance():.2f}"
        return output


def create_spend_chart(categories):
    spent = []

    # Calculate total spent per category
    for category in categories:
        total = 0
        for elem in category.ledger:
            if elem['amount'] < 0:
                total += -elem['amount']
        spent.append({'name': category.name, 'amount': total})

    overall = sum(cat['amount'] for cat in spent)

    # Percentages rounded down to nearest 10
    for cat in spent:
        percent = (cat['amount'] / overall) * 100 if overall > 0 else 0
        cat['percentage'] = int(percent // 10) * 10

    output = "Percentage spent by category\n"

    # Bars
    for i in range(100, -1, -10):
        output += f"{i:>3}| "
        for cat in spent:
            output += "o  " if cat['percentage'] >= i else "   "
        output += "\n"

    # Horizontal line (two chars past final bar)
    output += "    " + "-" * (3 * len(categories) + 1) + "\n"

    # Vertical names
    max_len = max(len(cat['name']) for cat in spent)
    for i in range(max_len):
        output += "     "
        for cat in spent:
            output += (cat['name'][i] if i < len(cat['name']) else " ") + "  "
        output += "\n"

    return output.rstrip("\n")



food = Category('Food')
food.deposit(1000, 'deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
print(food)
print(create_spend_chart([food]))

** end of main.py **

