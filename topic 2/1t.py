class LinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = LinkedListNode(data)
        if not self.head:
            self.head = new_node
        else:
            last = self.head
            while last.next:
                last = last.next
            last.next = new_node

    def display(self):
        current = self.head
        if not current:
            print("No orders available.")
            return
        while current:
            print(current.data)
            current = current.next

    def remove(self, data):
        current = self.head
        prev = None
        while current:
            if current.data == data:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                print(f"Order '{data}' removed.")
                return
            prev = current
            current = current.next
        print(f"Order '{data}' not found.")

    def count(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

# Array Implementation

class ArrayOrders:
    def __init__(self):
        self.orders = []

    def append(self, data):
        self.orders.append(data)

    def display(self):
        if not self.orders:
            print("No orders available.")
        else:
            for order in self.orders:
                print(order)

    def remove(self, data):
        if data in self.orders:
            self.orders.remove(data)
            print(f"Order '{data}' removed.")
        else:
            print(f"Order '{data}' not found.")

    def count(self):
        return len(self.orders)

# Main Program

def main():
    linked_list_orders = LinkedList()  # Linked List for Orders
    array_orders = ArrayOrders()       # Array for Orders
    
    while True:
        print("\nChoose an option:")
        print("1. Add order.")
        print("2. View all orders.")
        print("3. Remove order.")
        print("4. View order count.")
        print("0. Exit.")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            order_item = input("Enter order item: ")
            # Add order to both Linked List and Array
            linked_list_orders.append(order_item)
            array_orders.append(order_item)
            print(f"Order '{order_item}' added.")

        elif choice == "2":
            print("\nOrders in Linked List:")
            linked_list_orders.display()
            print("\nOrders in Array:")
            array_orders.display()

        elif choice == "3":
            order_item = input("Enter the order item to remove: ")
            linked_list_orders.remove(order_item)
            array_orders.remove(order_item)

        elif choice == "4":
            print(f"Linked List Order Count: {linked_list_orders.count()}")
            print(f"Array Order Count: {array_orders.count()}")

        elif choice == "0":
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
