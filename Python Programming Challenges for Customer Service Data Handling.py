# Initial ticket data
service_tickets = {
    "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
}
# Function to open a new service ticket
def open_ticket():
    customer = input("Enter customer name: ")
    issue = input("Describe the issue: ")
    ticket_id = "Ticket" + str(len(service_tickets) + 1).zfill(3)  # Generate new ticket ID
    service_tickets[ticket_id] = {"Customer": customer, "Issue": issue, "Status": "open"}
    print("\nTicket opened successfully.")
    print(f"New Ticket ID: {ticket_id}")

# Function to update the status of a ticket
def update_ticket_status(ticket_id, new_status):
    if ticket_id in service_tickets:
        service_tickets[ticket_id]["Status"] = new_status
        print(f"Ticket {ticket_id} status updated to {new_status}")
    else:
        print(f"Ticket {ticket_id} not found.")

# Function to display all tickets or filter by status
def display_tickets(status=None):
    if status:
        filtered_tickets = {tid: ticket for tid, ticket in service_tickets.items() if ticket["Status"] == status}
        if filtered_tickets:
            print(f"\nTickets with status '{status}':")
            for tid, ticket in filtered_tickets.items():
                print(f"Ticket ID: {tid}, Customer: {ticket['Customer']}, Issue: {ticket['Issue']}")
        else:
            print(f"No tickets found with status '{status}'.")
    else:
        print("\nAll tickets:")
        for tid, ticket in service_tickets.items():
            print(f"Ticket ID: {tid}, Customer: {ticket['Customer']}, Issue: {ticket['Issue']}, Status: {ticket['Status']}")
            
# Example usage:
if __name__ == "__main__":
    while True:
        print("\n======= Customer Service Ticket Tracker =======")
        print("1. Open a new ticket")
        print("2. Update ticket status")
        print("3. Display all tickets")
        print("4. Display open tickets")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")
        if choice == "1":
            open_ticket()
        elif choice == "2":
            ticket_id = input("Enter Ticket ID to update: ")
            new_status = input("Enter new status (open/closed): ")
            update_ticket_status(ticket_id, new_status)
        elif choice == "3":
            display_tickets()
        elif choice == "4":
            display_tickets("open")
        elif choice == "5":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")