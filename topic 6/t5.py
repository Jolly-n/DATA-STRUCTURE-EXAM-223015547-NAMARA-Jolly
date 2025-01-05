class Categoryprod:
    def __init__(self, name):
        self.name = name
        self.subcategories = []

    def add_subcategory(self, subcategory):
        self.subcategories.append(subcategory)

    def remove_subcategory(self, subcategory_name):
        self.subcategories = [subcategory for subcategory in self.subcategories if subcategory.name != subcategory_name]

    def display(self, level=0):
        print("  " * level + self.name)
        for subcategory in self.subcategories:
            subcategory.display(level + 1)


def main():
    # Ask user for the root category
    root_category_name = input("Enter the root category name: ")
    root_category = Categoryprod(root_category_name)

    while True:
        print("\nChoose an option:")
        print("1. Add Subcategory")
        print("2. Display Categories")
        print("3. Remove Subcategory")
        print("0. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            subcategory_name = input("Enter subcategory name: ")
            subcategory = Categoryprod(subcategory_name)

            # Ask if the user wants to add subcategories under the newly created subcategory
            while True:
                add_sub = input(f"Do you want to add subcategories under '{subcategory_name}'? (yes/no): ").lower()
                if add_sub == "yes":
                    sub_subcategory_name = input(f"Enter sub-subcategory name under '{subcategory_name}': ")
                    subcategory.add_subcategory(Categoryprod(sub_subcategory_name))
                elif add_sub == "no":
                    break
                else:
                    print("Invalid input, please enter 'yes' or 'no'.")
            
            # Add this subcategory to the root category
            root_category.add_subcategory(subcategory)
            print(f"Subcategory '{subcategory_name}' added.")

        elif choice == "2":
            # Display all categories and subcategories
            print("\nDisplaying Categories:")
            root_category.display()

        elif choice == "3":
            # Remove a subcategory
            subcategory_name = input("Enter the subcategory name to remove: ")
            root_category.remove_subcategory(subcategory_name)
            print(f"Subcategory '{subcategory_name}' removed.")

        elif choice == "0":
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
