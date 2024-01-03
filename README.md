# DVA269-Home_sharing_App
Group 4 Home Sharing App

We start with accomodations: We made it possible to publish and edit your accomodations that a host would want to share
with others.

The Publish feature allows the host to name their property, tell us where it's located, the size, type of accomodation 
and many other things. Among the most important parts: the price and availability weeks.

The class follows with many methods that allow us to handle the accomodations
through various means. Among which are simply the displayInformation method that
simply prints out everything interesting about the accomodation that a possible renter could want.

The find_availability method is a method that just looks at whether or not the accomodation is free to book or not.
It uses a for loop to go through a 53 item long list which represents the weeks of a yearly calendar.
If the statement within one of the indexes says "False", then it is available for booking. If it is "None", those dates 
are neither rented nor available for renting. True is when it is rented.

set_availability method simply sets the availability to the chosen weeks to either None or False. If False, it is 
available and if None then it is not.

findAccomodation is a method to make it simpler to look for the accomodation within the list.

book_accomodation is a method that utilizes other methods such as findAccomodation and find_availability to book the 
right weeks the accomodation is available at.

editAccomodation allows the user to change any of the accomodation variables to their desired values. You can chanve
the availability, the price, the size, and pretty much anything you want. Even the name.

ViewAccomodations gives an overview of all accomodations.

removeAccomodations removes an accomodation entirely from the list. It is not simply removing the entire accomodation 
from the application.

The Main function is simply a debugger. It does nothing exceptional save for trying out the various methods.



