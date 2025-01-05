class DynamicInventory:
    def __init__(self):
        self.inventory = []

    def add_product(self, product_name):
        self.inventory.append(product_name)

    def remove_product(self, product_name):
        if product_name in self.inventory:
            self.inventory.remove(product_name)
        else:
            print(f"Product '{product_name}' not found in inventory.")

    def display_inventory(self):
        if not self.inventory:
            print("Inventory is empty.")
        else:
            print("Inventory:")
            for product in self.inventory:
                print(product)


def main():
    inventory = DynamicInventory()

    while True:
        print("\nChoose an option:")
        print("1. Add Product")
        print("2. Remove Product")
        print("3. Display Inventory")
        print("0. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            product_name = input("Enter product name to add: ")
            inventory.add_product(product_name)
            print(f"Product '{product_name}' added to inventory.")

        elif choice == "2":
            product_name = input("Enter product name to remove: ")
            inventory.remove_product(product_name)

        elif choice == "3":
            inventory.display_inventory()

        elif choice == "0": 
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
