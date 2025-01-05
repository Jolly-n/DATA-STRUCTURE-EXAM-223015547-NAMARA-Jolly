import heapq

class Order:
    def __init__(self, order_id, priority):
        self.order_id = order_id
        self.priority = priority

    def __lt__(self, other):
        # Compare orders based on priority (lower value means higher priority)
        return self.priority < other.priority

    def __repr__(self):
        return f"Order ID: {self.order_id}, Priority: {self.priority}"

class OrderQueue:
    def __init__(self):
        self.orders = []

    def add_order(self, order):
        heapq.heappush(self.orders, order)

    def process_order(self):
        if self.orders:
            order = heapq.heappop(self.orders)
            print(f"Processing Order ID: {order.order_id}, Priority: {order.priority}")
        else:
            print("No orders to process.")

    def view_orders(self):
        if not self.orders:
            print("No orders in the queue.")
        else:
            print("\nCurrent orders in queue (sorted by priority):")
            for order in self.orders:
                print(order)

    def get_order_count(self):
        return len(self.orders)

def main():
    order_queue = OrderQueue()

    while True:
        print("\nChoose an option:")
        print("1. Add Order")
        print("2. Process Order")
        print("3. View Orders")
        print("5. Get Number of Orders")
        print("0. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            # Input order details
            try:
                order_id = int(input("Enter order ID: "))
                priority = int(input("Enter order priority (lower number = higher priority): "))
                order = Order(order_id, priority)
                order_queue.add_order(order)
                print(f"Order {order_id} added with priority {priority}.")
            except ValueError:
                print("Invalid input. Please enter valid integers for order ID and priority.")

        elif choice == "2":
            # Process the highest priority order
            print("Processing next order...")
            order_queue.process_order()

        elif choice == "3":
            # View the orders in the queue
            order_queue.view_orders()

        elif choice == "5":
            # Get the number of orders in the queue
            print(f"Total orders in queue: {order_queue.get_order_count()}")

        elif choice == "0":
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
