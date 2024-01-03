import os
import platform
import time
import random

user_database = {}

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
    def __init__(self, name, surname, account_type, email, address, password, hostid, bank_details=None):
        super().__init__(name, surname, account_type, email, address, password)
        self.bank_details = bank_details
        self.hostid = hostid

    def update_bank_details(self, bank_details):
        self.bank_details = bank_details

    def __str__(self):
        bank_details_str = f"\nBank Details: {self.bank_details}" if self.bank_details else ""
        return super().__str__() + bank_details_str

    def view_profile(self):
        print(f"\n{self}\nHost ID: {self.hostid}\n")

class RenterClass(UserClass):
    def __init__(self, name, surname, account_type, email, address, password, renterid):
        super().__init__(name, surname, account_type, email, address, password)
        self.renterid = renterid

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

    def view_profile(self):
        print(f"\n{self}\nRenter ID: {self.renterid}\n")

    def viewRequests(self):
        if len(requests) == 0:
            print("No Requests")

        else:
            count = 1
            print("\n Your current requests")
            for req in requests:
                print(f"{count}: Request for: {req}\n")


pre_existing_host = UserClass(
    name="host",
    surname="test",
    account_type="host",
    email="test@gmail.com",
    address="eskilstuna1",
    password="host"
)

pre_existing_renter = UserClass(
    name="renter",
    surname="test",
    account_type="renter",
    email="test@gmail.com",
    address="eskilstuna2",
    password="renter"
)

user_database[pre_existing_renter.name] = pre_existing_renter
user_database[pre_existing_host.name] = pre_existing_host

class AccommodationClass:

    totalAccommodations = 0

    def publish(self, name:str, location:str, size:int, AccommodationType:str, price:float, floor:int, rooms:int, otherFeatures:str, availability=None, host=None):
        """ Publishes an accomodation to be browsed and request to be rented.
        Name  - Title of Accomodation
        Location - City of Accomodation
        Size - Square Meters
        Accomodation Type - Appartment, Villa, Rowhouse, Shed, Room, Student Room, Yacht, etc
        Price - Price per week
        Floor - What floor the accomodation is located (if appartment) or how many floors that is rented if Villa or rowhouse
        Rooms - Number of rooms rented out
        Other Features - Lake view, Sunset, Forest, etc
        Availability - What week (out of 52) is the property to be rented out?
        """

        self.name = name.lower()
        self.AccommodationID = name + str(AccommodationClass.totalAccommodations + 1)
        self.host_id = host
        self.location = location
        self.size = size
        self.AccommodationType = AccommodationType
        self.price_p_day = price
        self.floor = floor
        self.rooms = rooms
        self.otherFeatures = otherFeatures
        self.availability = [None]*53

        # Save the Accommodations to a list which contains a dictionary within a dictionary.
        AccommodationClass.totalAccommodations += 1
        allAccommodations.append(
            {self.name: {
                "Name"              : self.name,
                "AccommodationID"   : self.AccommodationID,
                "Host_ID"           : self.host_id,
                "Location"          : self.location,
                "Size"              : self.size,
                "Accomodation Type" : self.AccommodationType,
                "Price"             : self.price_p_day,
                "Floor"             : self.floor,
                "Rooms"             : self.rooms,
                "Features"          : self.otherFeatures,
                "Availability"      : self.availability,
                "Rented"            : False
            }
            })
        if availability != None or availability != '':
            self.availability = self.set_availability(self.name, str(availability))


    def addAccomodation(self, host):
        while True:
            try:
                name        = input("Property Name > ").lower()
                location    = input("Property Location (city) > ")
                size        = int(input("Property Size (in sqm) > "))
                acc_type    = input("Property Type (villa, appartment, etc) > ")
                price       = int(input("Property Price (per week) > "))
                floor       = int(input("Property Floor (appartment floor, or total floors of house) > "))
                rooms       = int(input("Number of rooms of Accomodation > "))
                features    = input("Any special features? > ")
                avail       = input("What weeks do you want it available? Leave blank if you"
                                    " want to decide later. ex: (20-22) > ")
                return self.publish(name, location, size, acc_type, price, floor, rooms, features, avail, host)
            except ValueError:
                print("Nono. Some of these require numbers: Size, Price, Floor, and Rooms.")


    def displayInformation(self, accommodation, name):
        """ Prints out all necessary information about an accommodation """
        name = name.lower()
        print("Name: " + accommodation[name]["Name"].capitalize())
        print("Location: " + accommodation[name]["Location"])
        print("Floor: " + str(accommodation[name]["Floor"]))
        print("# of Rooms: " + str(accommodation[name]["Rooms"]))
        print("Price: " + str(accommodation[name]["Price"]) + "€ per day")
        print("Features: " + accommodation[name]["Features"])
        print("Availability weeks: " + self.find_availability(name, accommodation)[:-2])

    def find_availability(self, name, method=False, accommodation=None):
        """ Finds the weeks an accommodation is available. If not, it returns a string that says so. """
        if accommodation == None:
            accommodation = self.findAccommodation(name)
        availability_weeks = ""
        for index, available in enumerate(accommodation[name]['Availability']):
            if accommodation[name]['Availability'][index] == method:
                availability_weeks += f"{index}, "
        if availability_weeks == '':
            return "No Available Dates"
        return availability_weeks

    def set_availability(self, name, weeks, method="add"):
        """ Sets the availability of an accomodation, and changes it accordingly in the list. """
        name = name.lower()
        if method.lower() == "remove":
            method = None
        elif method.lower() == "add":
            method = False
        Accomodation = self.findAccommodation(name)
        try:
            for ind, av in enumerate(Accomodation[name]['Availability']):
                if ind+1 == int(weeks):
                    if av != method:
                        Accomodation[name]["Availability"][ind] = method
                        return
        except:
            week_span = weeks.strip(' ')
            start_week, end_week = map(int, week_span.split('-'))
            weeks_list = list(range(start_week, end_week + 1))
            for week in weeks_list:
                if Accomodation[name]["Availability"][week] != method:
                    Accomodation[name]["Availability"][week] = method

    def findAccommodation(self, name):
        """ Searches for an accomodation with the name """
        for accommodation in allAccommodations:
            if name.lower() in accommodation:
                return accommodation

    def book_accomodation(self, name, weeks):
        name = name.lower()
        accomodation = self.findAccommodation(name)
        available = self.find_availability(name, accomodation)
        try:
            week_span = weeks.strip(' ')
            start_week, end_week = map(int, week_span.split('-'))
            weeks = list(range(start_week, end_week + 1))
        except:
            pass
        if available == "No Available Dates":
            print("Cannot book any dates.")
            return
        available = available.strip(' ').split(',')
        for date in available[:-1]:
            for week in weeks:
                if int(date) == week:
                    accomodation[name]['Availability'][week] = True


    def editAccommodation(self, name):
        name = name.lower()
        accommodation = self.findAccommodation(name)
        if accommodation:
            self.displayInformation(accommodation, name)

            change = input("What to change? > ").capitalize()
            if change.lower() == 'availability':
                while True:
                    method = input("Remove or add availability? > ").lower()
                    if method.lower().strip(' ') == "add" or method.lower().strip(' ') == 'remove':
                        weeks = input("What weeks? > ")
                        self.set_availability(name, weeks, method)
                        return
                    else:
                        print("Type only [remove] or [add].")
            else:
                new_value = input("New " + change + " > ").capitalize()

                # Update the specific value in the accommodation dictionary
                accommodation[name][change] = new_value
        else:
            print("This accommodation does not exist.")

    def viewAccommodations(self, host=False):
        if host:
            method = True
            print("These are your properties")
            for accommodation in allAccommodations:
                for title, details in accommodation.items():
                    if details["Host_ID"] == host:
                        print(f"{title.capitalize()}: {details['Location']}. "
                              f"Booked: {self.find_availability(title, method, accommodation)}")
        else:
            for accommodation in allAccommodations:
                for title, details in accommodation.items():
                    if details["Rented"] == True:
                        continue
                    print(f"{title.capitalize()}: {details['Location']}, ", end="")
                print()
            print("\n")

    def removeAccommodation(self, name, host):
        name = name.lower()
        for index, accommodation in enumerate(allAccommodations):
            if name in accommodation and host == accommodation[name]["Host_ID"]:
                del allAccommodations[index]
                AccommodationClass.totalAccommodations -= 1
                return
        print("This accommodation does not exist.")


def create_account():
    name = input("Choose a username: ")
    surname = input("Enter your surname: ")
    while True:
        account_type = input("Account Type (renter/host): ").lower()

        if account_type == "renter" or account_type == "host":
            renterid = random.randint(1, 5)
            hostid = random.randint(1, 5)
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
        user_database[name] = HostClass(name, surname, account_type, email, address, password, hostid)
    else:
        user_database[name] = RenterClass(name, surname, account_type, email, address, password, renterid)

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


def main_menu(accommodation_instance):
    while True:
        print("\nWelcome! Please choose an option:")
        print("1. Login")
        print("2. Create Account")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            logged_in_user = login()

            if logged_in_user:

                user_instance = user_database.get(logged_in_user)
                accommodation_instance = AccommodationClass()

                while True:
                    print(f"Logged in as: {logged_in_user}")
                    print("1. View Profile")
                    print("2. View Accommodations")
                    print("3. Edit or Add Accomodation")
                    print("4. Remove Accomodation")
                    print("5. View requests")
                    print("6. Request Accommodation")
                    print("7. Update Profile")
                    print("8. Log out")
                    option = input("Your choice (1-8): ")

                    if option == "1":
                        user_instance.view_profile()

                    elif option == "2":

                        if isinstance(user_instance, HostClass):
                            accommodation_instance.viewAccommodations(user_instance.hostid)
                        else:
                            accommodation_instance.viewAccommodations()

                    elif option == "3":

                        if isinstance(user_instance, HostClass):

                            editoradd = input("Do you want to edit or add an accommodation? > ").lower()

                            if editoradd == 'add':
                                accommodation_instance.addAccomodation(user_instance.hostid)

                            elif editoradd == 'edit':
                                accommodation_instance.viewAccommodations()

                                editAccommodation = input("Enter name of accommodation to edit > ").capitalize()
                                accommodation_instance.editAccommodation(editAccommodation)

                        else:
                            print("You need to be a host to do this")

                    elif option == '4':

                        if isinstance(user_instance, HostClass):
                            accommodation_instance.viewAccommodations(user_instance.hostid)
                            removeAccommodation = input("Enter name of accommodation to remove > ").lower()

                            accommodation_instance.removeAccommodation(removeAccommodation, user_instance.hostid)


                    elif option == '5':

                        if isinstance(user_instance, RenterClass):

                            user_instance.viewRequests()
                        else:
                            print("Not renter")


                    elif option == '6':

                        if isinstance(user_instance, RenterClass):

                            accommodation_instance.viewAccommodations()

                            user_instance.requestAccommodation()
                        else:
                            print("User not found.")

                    elif option == "7":

                        if user_instance:
                            user_instance.update_user_profile()
                        else:
                            print("User not found.")

                    elif option == "8":
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
    accommodation_instance.publish("House 34b", "Köln", 34, "apartment", 10, 1, 3, "None", "30-31",  "None")
    accommodation_instance.publish("House 33b", "Central Münich", 125, "apartment", 15, 1, 7, "None", "30-32", "None")
    accommodation_instance.publish("Room 311a", "Stockholm", 34, "apartment", 10, 1, 2, "None", "45-50", "None")
    accommodation_instance.publish("Test", "Yep", 34, "apartment", 10, 1, 3, "None", "45-50", "None")
    accommodation_instance.publish("Wardrobe", "Nopp", 125, "apartment", 15, 1, 7, "None", "45-50", "None")
    accommodation_instance.publish("Chair", "TEST", 34, "apartment", 10, 1, 2, "None", "45-50", "None")
    main_menu(accommodation_instance)

