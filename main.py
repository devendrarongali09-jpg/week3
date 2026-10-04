#Billing System (OOPS Based)
class Product:
    def __init__(self, name: str, price: float, quantity: int):
        self.name = name
        self.price = float(price)
        self.quantity = int(quantity)

    def get_total_price(self) -> float:
        return self.price * self.quantity


class Bill:
    def __init__(self, customer_name: str, tax_rate: float = 0.05):
        self.customer_name = customer_name
        self.tax_rate = float(tax_rate)  # e.g., 0.05 for 5% tax
        self.items: list[Product] = []

    def add_product(self, product: Product) -> None:
        self.items.append(product)

    def calculate_subtotal(self) -> float:
        return sum(item.get_total_price() for item in self.items)

    def calculate_tax(self) -> float:
        return self.calculate_subtotal() * self.tax_rate

    def calculate_grand_total(self) -> float:
        return self.calculate_subtotal() + self.calculate_tax()

    def display_bill(self) -> None:
        subtotal = self.calculate_subtotal()
        tax_amount = self.calculate_tax()
        grand_total = self.calculate_grand_total()

        print("=" * 60)
        print(f"{'INVOICE':^60}")
        print("=" * 60)
        print(f"Customer Name: {self.customer_name}")
        print("-" * 60)
        # Table Header
        print(f"{'Item':<25}{'Price':>10}{'Qty':>10}{'Total':>15}")
        print("-" * 60)

        # Table Rows
        for item in self.items:
            item_total = item.get_total_price()
            print(f"{item.name:<25}{item.price:>10.2f}{item.quantity:>10}{item_total:>15.2f}")

        print("-" * 60)
        # Summary
        tax_percent = self.tax_rate * 100
        print(f"{'Subtotal:':<45}{subtotal:>15.2f}")
        print(f"{f'Tax ({tax_percent:.1f}%):':<45}{tax_amount:>15.2f}")
        print("=" * 60)
        print(f"{'Grand Total:':<45}{grand_total:>15.2f}")
        print("=" * 60)


# Demonstration
if __name__ == "__main__":
    my_bill = Bill(customer_name="John Doe", tax_rate=0.08)

    my_bill.add_product(Product("Wireless Mouse", 25.50, 2))
    my_bill.add_product(Product("Mechanical Keyboard", 75.00, 1))
    my_bill.add_product(Product("USB-C Cable", 8.99, 3))

    my_bill.display_bill()