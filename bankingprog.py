# Simple Banking System in Python

balance = 0

def check_balance():
    print(f"Your current balance is: ₹{balance}")

def deposit():
    global balance
    amount = float(input("Enter amount to deposit: ₹"))
    if amount > 0:
        balance += amount
        print(f"₹{amount} deposited successfully!")
    else:
        print("Invalid amount!")

def withdraw():
    global balance
    amount = float(input("Enter amount to withdraw: ₹"))
    if 0 < amount <= balance:
        balance -= amount
        print(f"₹{amount} withdrawn successfully!")
    else:
        print("Insufficient balance or invalid amount!")

def main():
    while True:
        print("\n===== Welcome to Python Bank =====")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            check_balance()
        elif choice == '2':
            deposit()
        elif choice == '3':
            withdraw()
        elif choice == '4':
            print("Thank you for using Python Bank!")
            break
        else:
            print("Invalid choice! Please try again.")

# Run the program
main()
