** start of main.py **

class Category:
    """
    Instantiates objects based on different budget categories like food, clothing, and entertainment.
    """
    def __init__(self, name: str):
        self.name = name
        self.ledger: list = []

    def deposit(self, amount: float, description: str = '') -> None:
        """
        Adds a deposit to the ledger list.
        """
        d = {'amount': amount, 'description': description}
        self.ledger.append(d)

    def withdraw(self, amount: float, description: str = '') -> bool:
        """
        Adds a withdrawal to the ledger list if there are enough funds.
        Returns True if the withdrawal took place, and False otherwise.
        """
        if self.check_funds(amount):
            d = {'amount': -amount, 'description': description}
            self.ledger.append(d)
            return True
        return False

    def get_balance(self) -> float:
        """
        Returns the current balance of the budget category.
        """
        # Pythonic approach: Using sum() with a generator expression is cleaner and more efficient
        return sum(elem['amount'] for elem in self.ledger)

    def check_funds(self, amount: float) -> bool:
        """
        Checks if the amount is greater than the balance.
        Returns False if the amount is greater, True otherwise.
        """
        # Simplified boolean return instead of a full if/else block
        return amount <= self.get_balance()

    def transfer(self, amount: float, category: "Category") -> bool:
        """
        Transfers funds from the current category to another category object.
        """
        if self.withdraw(amount, f"Transfer to {category.name}"):
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def __str__(self) -> str:
        """
        Returns a formatted string representation of the category object.
        """
        # Title line: centered string with '*' padding (30 characters total)
        output = f"{self.name:*^30}\n"
        
        for elem in self.ledger:
            # Format: Description truncated to first 23 chars + Amount right-aligned to 7 chars (2 decimals)
            output += f"{elem['description'][0:23]:<23}{elem['amount']:>7.2f}\n"
            
        output += f"Total: {self.get_balance():.2f}"
        return output


def create_spend_chart(categories: list) -> str:
    """
    Generates a bar chart showing the percentage spent in each category passed in the list.
    """
    spent = []

    # Calculate total spent per category (only negative amounts indicate spending)
    for category in categories:
        total = 0
        for elem in category.ledger:
            if elem['amount'] < 0:
                total += -elem['amount']
        spent.append({'name': category.name, 'amount': total})

    # Calculate the overall spending across all categories
    overall = sum(cat['amount'] for cat in spent)

    # Calculate percentages rounded down to the nearest 10
    for cat in spent:
        percent = (cat['amount'] / overall) * 100 if overall > 0 else 0
        cat['percentage'] = int(percent // 10) * 10

    output = "Percentage spent by category\n"

    # Build the y-axis and bars (from 100 down to 0)
    for i in range(100, -1, -10):
        output += f"{i:>3}| "
        for cat in spent:
            output += "o  " if cat['percentage'] >= i else "   "
        output += "\n"

    # Add the horizontal dashed line (length based on number of categories)
    output += "    " + "-" * (3 * len(categories) + 1) + "\n"

    # Build the vertical names below the x-axis
    max_len = max(len(cat['name']) for cat in spent)
    for i in range(max_len):
        output += "     "
        for cat in spent:
            output += (cat['name'][i] if i < len(cat['name']) else " ") + "  "
        output += "\n"

    # rstrip() removes the trailing newline character from the final loop iteration
    return output.rstrip("\n")


# --- Testing block ---
if __name__ == "__main__":
    food = Category('Food')
    food.deposit(1000, 'deposit')
    food.withdraw(10.15, 'groceries')
    food.withdraw(15.89, 'restaurant and more food for dessert')
    print(food)
    print("\n")
    print(create_spend_chart([food]))

** end of main.py **

