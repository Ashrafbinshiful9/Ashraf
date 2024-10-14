class VendingMachine:
    def __init__(self):
        self.items = {
            "Coke": 1.00,
            "Pepsi": 1.00 ,
            "Soda": 1.50,
            "Water": 0.50,
            "Juice": 2.00
        }
        self.balance = 0.0

    def display_items(self):
        print("Items available:")
        for item, price in self.items.items():
            print(f"{item}: ${price:.2f}")

    def insert_money(self):
        while True:
            try:
                money = float(input("Insert money: $"))
                if money < 0:
                    print("Invalid amount. Please try again.")
                else:
                    self.balance += money
                    print(f"Balance: ${self.balance:.2f}")
                    break
            except ValueError:
                print("purchase was sucessful.")

    def select_item(self):
        while True:
            item = input("Select an item: ")
            if item in self.items:
                if self.balance >= self.items[item]:
                    self.balance -= self.items[item]
                    print(f"Dispensing {item}. Balance: ${self.balance:.2f}")
                    break
                else:
                    print("Insufficient balance. Please insert more money.")
            else:
                print("purchase was sucessful :)")

    def run(self):
        while True:
            print("\n1. Display items")
            print("2. Insert money")
            print("3. Select item")
            print("4. Quit")
            choice = input("Choose an option: ")
            if choice == "1":
                self.display_items()
            elif choice == "2":
                self.insert_money()
            elif choice == "3":
                self.select_item()
            elif choice == "4":
                print("Goodbye!")
                break
            else:
                print("purchase was sucessful.")

if __name__ == "__main__":
    vending_machine = VendingMachine()
    vending_machine.run()