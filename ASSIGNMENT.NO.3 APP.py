# Experiment No. 3
# Design Patterns in Python
# Strategy Pattern - Payment Processing System


# Strategy Interface
class PaymentStrategy:
    def pay(self, amount):
        raise NotImplementedError(
            "Subclasses must implement the pay() method"
        )


# Concrete Strategy 1: Credit Card
class CreditCardPayment(PaymentStrategy):

    def __init__(self, card_number):
        self.card_number = card_number

    def pay(self, amount):
        print("\nProcessing Credit Card Payment...")
        print(f"Card Number: **** **** **** {self.card_number[-4:]}")
        print(f"Amount Paid: ₹{amount}")
        print("Payment Successful!")


# Concrete Strategy 2: PayPal
class PayPalPayment(PaymentStrategy):

    def __init__(self, email):
        self.email = email

    def pay(self, amount):
        print("\nProcessing PayPal Payment...")
        print(f"PayPal Account: {self.email}")
        print(f"Amount Paid: ₹{amount}")
        print("Payment Successful!")


# Concrete Strategy 3: UPI
class UPIPayment(PaymentStrategy):

    def __init__(self, upi_id):
        self.upi_id = upi_id

    def pay(self, amount):
        print("\nProcessing UPI Payment...")
        print(f"UPI ID: {self.upi_id}")
        print(f"Amount Paid: ₹{amount}")
        print("Payment Successful!")


# Context
class PaymentProcessor:

    def __init__(self, strategy=None):
        self.strategy = strategy

    # Change strategy dynamically
    def set_strategy(self, strategy):
        self.strategy = strategy

    # Process payment
    def process_payment(self, amount):
        if self.strategy is None:
            print("Please select a payment method.")
        else:
            self.strategy.pay(amount)


# Main Program
print("===== Configurable Payment Processing System =====")

processor = PaymentProcessor()

while True:
    print("\n1. Credit Card")
    print("2. PayPal")
    print("3. UPI")
    print("4. Exit")

    choice = input("Select Payment Method: ")

    if choice == "1":
        card_number = input("Enter Credit Card Number: ")
        amount = float(input("Enter Amount: ₹"))

        processor.set_strategy(
            CreditCardPayment(card_number)
        )
        processor.process_payment(amount)

    elif choice == "2":
        email = input("Enter PayPal Email: ")
        amount = float(input("Enter Amount: ₹"))

        processor.set_strategy(
            PayPalPayment(email)
        )
        processor.process_payment(amount)

    elif choice == "3":
        upi_id = input("Enter UPI ID: ")
        amount = float(input("Enter Amount: ₹"))

        processor.set_strategy(
            UPIPayment(upi_id)
        )
        processor.process_payment(amount)

    elif choice == "4":
        print("Thank you for using the Payment Processing System.")
        break

    else:
        print("Invalid choice. Please try again.")

