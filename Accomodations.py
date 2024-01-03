class AccommodationClass:

    totalAccommodations = 0
    allAccommodations = []

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
        for accommodation in AccommodationClass.allAccommodations:
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
        for accommodation in AccommodationClass.allAccommodations:
            for title, details in accommodation.items():
                print(f"{title}: {details['Location']}, ", end="")
            print()

    def removeAccommodation(self, name):
        for index, accommodation in enumerate(AccommodationClass.allAccommodations):
            if name in accommodation:
                del AccommodationClass.allAccommodations[index]
                return
        print("This accommodation does not exist.")


def Main():
    # Example usage:
    accommodation_instance = AccommodationClass()
    accommodation_instance.publish("House 34b", "Köln", 34, "apartment", 10, 1, 3, "None", "None")
    accommodation_instance.publish("House 33b", "Central Münich", 125, "apartment", 15, 1, 7, "None", "None")
    accommodation_instance.publish("Room 311a", "Stockholm", 34, "apartment", 10, 1, 2, "None", "None")
    accommodation_instance.viewAccommodations()
    accommodation_instance.editAccommodation("House 33b")
    accommodation_instance.displayInformation(accommodation_instance.findAccommodation("House 33b"), "House 33b")
    accommodation_instance.viewAccommodations()
    print()
    accommodation_instance.removeAccommodation("House 34b")
    accommodation_instance.viewAccommodations()


if __name__ == "__main__":
    Main()