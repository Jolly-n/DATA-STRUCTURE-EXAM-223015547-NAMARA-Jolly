# Order class to hold the order details
class Order:
    def __init__(self, order_id, priority):
        self.order_id = order_id
        self.priority = priority

    def __str__(self):
        return f"Order ID: {self.order_id}, Priority: {self.priority}"

# Function to implement Radix Sort based on priority
def radix_sort(orders):
    # Find the maximum priority value to determine the number of digits
    max_priority = max(order.priority for order in orders)
    
    # Apply counting sort for every digit (place value) in the priority number
    exp = 1
    while max_priority // exp > 0:
        counting_sort_by_digit(orders, exp)
        exp *= 10

# Function to perform counting sort by digit
def counting_sort_by_digit(orders, exp):
    # Initialize the output array and count array
    output = [None] * len(orders)
    count = [0] * 10
    
    # Count occurrences of each digit in the specified place
    for order in orders:
        index = order.priority // exp % 10
        count[index] += 1
    
    # Modify the count array to store the actual position of digits
    for i in range(1, 10):
        count[i] += count[i - 1]
    
    # Build the output array
    i = len(orders) - 1
    while i >= 0:
        order = orders[i]
        index = order.priority // exp % 10
        output[count[index] - 1] = order
        count[index] -= 1
        i -= 1
    
    # Copy the output array to orders, so that orders now contains sorted numbers
    for i in range(len(orders)):
        orders[i] = output[i]

# Main function to interact with the user
def main():
    orders = []

    while True:
        print("\nChoose an option:")
        print("1. Add New Order")
        print("2. View All Orders")
        print("3. View Sorted Orders")
        print("4. Remove an Order")
        print("5. Update Order Priority")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            # Get order details from user
            order_id = input("Enter Order ID: ")
            priority = int(input("Enter Order Priority (integer value): "))
            order = Order(order_id, priority)
            orders.append(order)
            print(f"Order with ID {order_id} and Priority {priority} added.")
        
        elif choice == "2":
            # View all orders
            if orders:
                print("\nAll Orders:")
                for order in orders:
                    print(order)
            else:
                print("No orders to display.")
        
        elif choice == "3":
            # Sort the orders using Radix Sort
            if orders:
                print("\nSorting orders by priority...")
                radix_sort(orders)
                print("\nSorted Orders:")
                for order in orders:
                    print(order)
            else:
                print("No orders to display.")
        
        elif choice == "4":
            # Remove an order by ID
            order_id = input("Enter Order ID to remove: ")
            order_to_remove = next((order for order in orders if order.order_id == order_id), None)
            if order_to_remove:
                orders.remove(order_to_remove)
                print(f"Order with ID {order_id} removed.")
            else:
                print(f"No order found with ID {order_id}.")
        
        elif choice == "5":
            # Update an existing order's priority
            order_id = input("Enter Order ID to update priority: ")
            order_to_update = next((order for order in orders if order.order_id == order_id), None)
            if order_to_update:
                new_priority = int(input("Enter new priority value: "))
                order_to_update.priority = new_priority
                print(f"Priority for Order ID {order_id} updated to {new_priority}.")
            else:
                print(f"No order found with ID {order_id}.")
        
        elif choice == "6":
            print("Exiting program.")
            break
        
        else:
            print("Invalid choice, please try again.")

# Run the program
if __name__ == "__main__":
    main()
