class CircularNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self, max_size):
        self.head = None
        self.max_size = max_size
        self.size = 0

    def add_order(self, data):
        if self.size == self.max_size:
            print("Buffer full, removing oldest order...")
            self.remove_order()
        new_order = CircularNode(data)
        if not self.head:
            self.head = new_order
            new_order.next = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_order
            new_order.next = self.head
        self.size += 1

    def remove_order(self):
        if self.head:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            self.head = self.head.next
            temp.next = self.head
            self.size -= 1

    def remove_specific_order(self, order_to_remove):
        if not self.head:
            print("No orders to remove.")
            return
        temp = self.head
        prev = None
        while True:
            if temp.data == order_to_remove:
                if prev:  # Removing non-head node
                    prev.next = temp.next
                else:  # Removing the head node
                    self.head = temp.next
                self.size -= 1
                print(f"Removed order: {order_to_remove}")
                return
            prev = temp
            temp = temp.next
            if temp == self.head:
                break
        print(f"Order '{order_to_remove}' not found in the buffer.")

    def display_orders(self):
        if not self.head:
            print("No orders to display.")
            return
        temp = self.head
        while True:
            print(temp.data)
            temp = temp.next
            if temp == self.head:
                break

    def get_order_count(self):
        return self.size

# Main program loop with user input
def main():
    order_buffer = CircularLinkedList(3)  # Set maximum size of buffer

    while True:
        print("\nChoose an option:")
        print("1. Add Order")
        print("2. Display Orders")
        print("3. Get Number of Orders")
        print("4. Remove Specific Order")
        print("0. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            order = input("Enter order description: ")
            order_buffer.add_order(order)
            print(f"Added: {order}")

        elif choice == "2":
            print("\nCurrent Orders in Buffer:")
            order_buffer.display_orders()

        elif choice == "3":
            print(f"Number of orders in the buffer: {order_buffer.get_order_count()}")

        elif choice == "4":
            order_to_remove = input("Enter the order description to remove: ")
            order_buffer.remove_specific_order(order_to_remove)

        elif choice == "0":
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
