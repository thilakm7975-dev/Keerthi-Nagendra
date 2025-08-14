# Passbook-style Bank Customer Details Program

customers = []

def add_customer(name, account_number, balance):
    customer = {
        "Name": name,
        "Account Number": account_number,
        "Balance": balance
    }
    customers.append(customer)

def display_passbook():
    print("\n==================== BANK PASSBOOK ====================")
    for i, customer in enumerate(customers, start=1):
        print("-------------------------------------------------------")
        print(f"Customer ID     : {i}")
        print(f"Account Holder  : {customer['Name']}")
        print(f"Account Number  : {customer['Account Number']}")
        print(f"Current Balance : ₹{customer['Balance']:.2f}")
        print("-------------------------------------------------------")
    print("=======================================================\n")

# Taking input
n = int(input("Enter number of customers: "))
for _ in range(n):
    name = input("Enter customer name: ")
    account_number = input("Enter account number: ")
    balance = float(input("Enter account balance: "))
    add_customer(name, account_number, balance)

# Display in passbook format
display_passbook()
