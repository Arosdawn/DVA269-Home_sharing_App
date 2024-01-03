import os
import platform
import time


user_database = {}

"""
accommodations = [
    {'title': 'TestTitel1',
     'location': 'TestPlats1',
     'size': 'Testkvm1'
     }, ]
"""
allAccommodations = []

requests = []

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

    def update_user_profile(self):

        print("Update profile information. Leave blank to keep the current value.")
        email = input(f"New email (current: {self.email}): ") or self.email
        address = input(f"New address (current: {self.address}): ") or self.address
        password = input("New password (leave blank to keep current): ") or self.password

        self.update_details(email=email, address=address, password=password)

        if isinstance(self, HostClass):
            bank_details = input(f"New bank details (current: {self.bank_details}): ") or self.bank_details
            self.update_bank_details(bank_details)

        print("Profile updated!")

    def view_profile(self):
        print(f"\n{self}\n")


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
    def __init__(self, name, surname, account_type, email, address, password):
        super().__init__(name, surname, account_type, email, address, password)

    def requestAccommodation(name):

        if len(allAccommodations) == 0:
            print("No accommodation available")

        else:
            while True:
                requestedAccomodation = input("Enter the name of accomodation to request > ").capitalize()

                if requestedAccomodation not in requests:
                    requests.append(requestedAccomodation)
                    print("Request sent")
                    break

                else:
                    again = input("Request already sent to chosen accomodation, try again? (y/n)").lower()

                    if again == 'y':
                        continue
                    else:
                        break


    def viewRequests(self):
        if len(requests) == 0:
            print("No Requests")

        else:
            count = 1
            print("\n Your current requests")
            for req in requests:
                print(f"{count}: Request for: {req}\n")


class AccommodationClass:

    totalAccommodations = 0


    def publish(self, name, location, size, AccommodationType, price, floor, rooms, otherFeatures, host=None):
        self.name = name
        self.AccommodationID = name
        self.host_id = host
        self.location = location
        self.size = size
        self.AccommodationType = AccommodationType
        self.price_p_day = price
        self.floor = floor
        self.rooms = rooms
        self.otherFeatures = otherFeatures

        # Save the Accommodation
        AccommodationClass.totalAccommodations += 1
        allAccommodations.append(
            {self.name: {
                "Name"              : self.name,
                "AccommodationID"   : self.AccommodationID,
                "Host ID"           : self.host_id,
                "Location"          : self.location,
                "Size"              : self.size,
                "Accomodation Type" : self.AccommodationType,
                "Price"             : self.price_p_day,
                "Floor"             : self.floor,
                "Rooms"             :self.rooms,
                "Features"          : self.otherFeatures
            }
            })

    @staticmethod
    def accommodation_types(accommodationType):
        types = ["apartment", "villa", "rowhouse", "shed", "room", "student room"]
        if accommodationType in types:
            return types.index(accommodationType)

    def displayInformation(self, accommodation, name):
        print("Name: " + accommodation[name]["Name"])
        print("Location: " + accommodation[name]["Location"])
        print("Floor: " + str(accommodation[name]["Floor"]))
        print("# of Rooms: " + str(accommodation[name]["Rooms"]))
        print("Price: " + str(accommodation[name]["Price"]) + "€ per day")
        print("Features: " + accommodation[name]["Features"])

    def findAccommodation(self, name):
        for accommodation in allAccommodations:
            if name in accommodation:
                return accommodation

    def editAccommodation(self, name):
        accommodation = self.findAccommodation(name)
        if accommodation:
            self.displayInformation(accommodation, name)

            change = input("What to change? > ").capitalize()
            new_value = input("New " + change + " > ").capitalize()

            # Update the specific value in the accommodation dictionary
            accommodation[name][change] = new_value
        else:
            print("This accommodation does not exist.")

    def viewAccommodations(self):
        count = 1
        print("\n")
        for accommodation in allAccommodations:
            for title, details in accommodation.items():
                print(f"{count}: {title}: {details['Location']} ", end="")
                count += 1
            print()
        print("\n")

    def removeAccommodation(self, name):
        for index, accommodation in enumerate(allAccommodations):
            if name in accommodation:
                del allAccommodations[index]
                return
        print("This accommodation does not exist.")


def create_account():
    name = input("Choose a username: ")
    surname = input("Enter your surname: ")
    while True:
        account_type = input("Account Type (renter/host): ").lower()

        if account_type == "renter" or account_type == "host":
            break
        else:
            print("You need to put 'renter' or 'host'")

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
                    print("3. Edit Accomodation")
                    print("4. View requests")
                    print("5. Request Accommodation")
                    print("6. Update Profile")
                    print("7. Log out")
                    option = input("Your choice (1-7): ")

                    if option == "1":
                        user_instance = user_database.get(logged_in_user)
                        user_instance.view_profile()

                    elif option == "2":
                        accommodation_instance = AccommodationClass()
                        accommodation_instance.viewAccommodations()

                    elif option == "3":

                        user_instance = user_database.get(logged_in_user)

                        if isinstance(user_instance, HostClass):

                            accommodation_instance = AccommodationClass()
                            accommodation_instance.viewAccommodations()
                            editAccommodation = input("Enter name of accommodation to edit > ").capitalize()

                            accommodation_instance.editAccommodation(editAccommodation)

                    elif option == '4':
                        user_instance = user_database.get(logged_in_user)

                        if isinstance(user_instance, RenterClass):

                            user_instance.viewRequests()
                        else:
                            print("Not renter")

                    elif option == '5':
                        user_instance = user_database.get(logged_in_user)
                        if isinstance(user_instance, RenterClass):

                            accommodation_instance = AccommodationClass()
                            accommodation_instance.viewAccommodations()

                            user_instance = user_database.get(logged_in_user)
                            user_instance.requestAccommodation()
                        else:
                            print("User not found.")

                    elif option == "6":
                        user_instance = user_database.get(logged_in_user)
                        if user_instance:
                            user_instance.update_user_profile()
                        else:
                            print("User not found.")

                    elif option == "7":
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
    accommodation_instance = AccommodationClass()
    accommodation_instance.publish("House 34b", "Köln", 34, "apartment", 10, 1, 3, "None", "None")
    accommodation_instance.publish("House 33b", "Central Münich", 125, "apartment", 15, 1, 7, "None", "None")
    accommodation_instance.publish("Room 311a", "Stockholm", 34, "apartment", 10, 1, 2, "None", "None")
    main_menu()


