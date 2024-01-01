import os
import platform
import time

user_database = {}
accommodations = []

def clear_screen():
    if platform.system() == "Windows":
        os.system('cls')  # for Windows
    else:
        os.system('clear')  # for Unix/Linux

class UserClass:
    def __init__(self, name, surname, account_type, email, address, password):
        self.name = name
        self.surname = surname
        self.account_type = account_type
        self.email = email
        self.address = address
        self.password = password

    def __str__(self):
        return (f"Name: {self.name}\nSurname: {self.surname}\n"
                f"Account Type: {self.account_type}\nEmail: {self.email}\n"
                f"Address: {self.address}")

    def update_details(self, email=None, address=None, password=None):
        if email: self.email = email
        if address: self.address = address
        if password: self.password = password

class HostClass(UserClass):
    def __init__(self, name, surname, account_type, email, address, password, bank_details=None):
        super().__init__(name, surname, account_type, email, address, password)
        self.bank_details = bank_details

    def update_bank_details(self, bank_details):
        self.bank_details = bank_details

    def __str__(self):
        bank_details_str = f"\nBank Details: {self.bank_details}" if self.bank_details else ""
        return super().__str__() + bank_details_str

class RenterClass(UserClass):
    def request_accommodation(self, accommodation_title):
        global accommodations
        accommodation = next((acc for acc in accommodations if acc["title"].lower() == accommodation_title.lower()), None)
        if accommodation:
            accommodations.remove(accommodation)
            print(f"Accommodation '{accommodation['title']}' has been requested.")
        else:
            print("Accommodation not found.")

def create_account():
    name = input("Choose a username: ")
    surname = input("Enter your surname: ")
    account_type = input("Account type (host/renter): ")
    email = input("Enter your email: ")
    address = input("Enter your address: ")
    password = input("Choose a password: ")

    if name in user_database:
        print("Username already exists. Please choose another.")
        return

    if account_type.lower() == 'host':
        user_database[name] = HostClass(name, surname, account_type, email, address, password)
    else:
        user_database[name] = RenterClass(name, surname, account_type, email, address, password)

    print("Account created!")
    time.sleep(1)

def login():
    name = input("Enter username: ")
    password = input("Enter password: ")

    user = user_database.get(name)
    if user and user.password == password:
        print("Login successful!")
        return name
    else:
        print("Incorrect username or password. Please try again.")
        return None

def update_user_profile(name):
    user = user_database.get(name)
    if not user:
        print("User not found.")
        return

    print("Update profile information. Leave blank to keep the current value.")
    email = input(f"New email (current: {user.email}): ") or user.email
    address = input(f"New address (current: {user.address}): ") or user.address
    password = input("New password (leave blank to keep current): ") or user.password

    user.update_details(email=email, address=address, password=password)

    if isinstance(user, HostClass):
        bank_details = input(f"New bank details (current: {user.bank_details}): ") or user.bank_details
        user.update_bank_details(bank_details)

    print("Profile updated!")

def view_profile(name):
    user = user_database.get(name)
    if user:
        print(user)
    else:
        print("User not found.")

def handle_accommodation(name):
    user = user_database.get(name)
    if isinstance(user, HostClass):
        upload_accommodation()
    elif isinstance(user, RenterClass):
        request_accommodation(name)

def upload_accommodation():
    title = input("Title of the accommodation: ")
    location = input("Location of the accommodation: ")
    size = input("Size in sqm: ")
    accommodations.append({"title": title, "location": location, "size": size})
    print("Accommodation added!")

def request_accommodation(name):
    title = input("Enter the title of the accommodation you want to request: ")
    user = user_database.get(name)
    user.request_accommodation(title)

def view_accommodations():
    if accommodations:
        print("Available accommodations:")
        for accommodation in accommodations:
            print(f"{accommodation['title']} - {accommodation['location']} - {accommodation['size']}")
    else:
        print("No accommodations available at the moment.")

def market():
    products = {"Book": 20, "Coffee Mug": 15, "Workout Session": 30, "Concert Ticket": 50, "Gift Card": 40}
    print("Welcome to the market, here are the current prices:")
    for product, points in products.items():
        print(f"{product}: {points} points")

    while True:
        choice = input("Write `exit` to exit the market: ").lower()
        if choice == 'exit':
            break
        else:
            print("Undefined choice, try again.")

def main_menu():
    while True:
        print("\nWelcome! Please choose an option:")
        print("1. Login")
        print("2. Create Account")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            logged_in_user = login()
            if logged_in_user:
                while True:
                    print(f"Logged in as: {logged_in_user}")
                    print("1. View Profile")
                    print("2. View Accommodations")
                    print("3. Handle Accommodation")
                    print("4. Update Profile")
                    print("5. Market")
                    print("6. Log out")
                    option = input("Your choice (1-6): ")

                    if option == "1":
                        view_profile(logged_in_user)
                    elif option == "2":
                        view_accommodations()
                    elif option == "3":
                        handle_accommodation(logged_in_user)
                    elif option == "4":
                        update_user_profile(logged_in_user)
                    elif option == "5":
                        market()
                    elif option == "6":
                        break
                    else:
                        print("Invalid choice, please try again.")
        elif choice == "2":
            create_account()
        elif choice == "3":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    header = "Accommodations for Free"
    print(f"\033[1;34m{header.center(50)}\033[0m")
    main_menu()
