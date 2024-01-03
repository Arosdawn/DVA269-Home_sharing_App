import time

class AccommodationClass:

    totalAccommodations = 0
    allAccommodations = []

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
        AccommodationClass.allAccommodations.append(
            {self.name: {
                "Name"              : self.name,
                "AccommodationID"   : self.AccommodationID,
                "Host ID"           : self.host_id,
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
        if availability != None:
            self.availability = self.set_availability(self.name, str(availability))


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

    def find_availability(self, name, accommodation=None):
        """ Finds the weeks an accommodation is available. If not, it returns a string that says so. """
        if accommodation == None:
            accommodation = self.findAccommodation(name)
        availability_weeks = ""
        for index, available in enumerate(accommodation[name]['Availability']):
            if accommodation[name]['Availability'][index] == False:
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
        for accommodation in AccommodationClass.allAccommodations:
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

    def viewAccommodations(self):
        for accommodation in AccommodationClass.allAccommodations:
            for title, details in accommodation.items():
                if details["Rented"] == True:
                    continue
                print(f"{title}: {details['Location']}, ", end="")
            print()

    def removeAccommodation(self, name):
        name = name.lower()
        for index, accommodation in enumerate(AccommodationClass.allAccommodations):
            if name in accommodation:
                del AccommodationClass.allAccommodations[index]
                AccommodationClass.totalAccommodations -= 1
                return
        print("This accommodation does not exist.")


def Main():
    # Examples:
    accommodation_instance = AccommodationClass()
    accommodation_instance.publish("House 34b", "Köln", 34, "apartment", 10, 1, 3, "None", "30-31",  "None")
    print(accommodation_instance.totalAccommodations)
    accommodation_instance.publish("House 33b", "Central Münich", 125, "apartment", 15, 1, 7, "None", "30-32", "None")
    print(accommodation_instance.totalAccommodations)
    accommodation_instance.publish("Room 311a", "Stockholm", 34, "apartment", 10, 1, 2, "None", "45-50", "None")
    print(accommodation_instance.totalAccommodations)
    print("We have published a few accommodations.")
    time.sleep(3)

    accommodation_instance.viewAccommodations()
    accommodation_instance.editAccommodation("House 33b")
    accommodation_instance.displayInformation(accommodation_instance.findAccommodation("House 33b"), "House 33b")
    accommodation_instance.viewAccommodations()
    print()
    accommodation_instance.removeAccommodation("House 34b")
    accommodation_instance.viewAccommodations()
    print(accommodation_instance.totalAccommodations)
    accommodation_instance.displayInformation(accommodation_instance.findAccommodation("Room 311a"), "Room 311a")
    accommodation_instance.book_accomodation("Room 311a", "45-47")
    accommodation_instance.displayInformation(accommodation_instance.findAccommodation("Room 311a"), "Room 311a")



if __name__ == "__main__":
    Main()