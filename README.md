# DVA269-Home_sharing_App
FINALSOURCECODE IS THE FINISHED PRODUCT
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

There is then a parent- or super class called UserClass. Everyone that is using the system is either a Host or a Renter we have two children classes called HostClass and RenterClass.

UserClass is the super class of the two different Users and takes in simple information such as name, password and account type. UserClass has three methods which are update_details, update_user_profile and a tiny view_profile. The update_user_profile is responsible for retrieving information from either a renter or host, and this method is reliant on update_details that actually store the new information. The third methods is only responsible for printing and is extremely simple.

The HostClass has access to another variable called bank_details that is meant to act as a security measure if the system was more developed, it also features host-id that is used to attach an accommodation to a specific host. Also has a small print to also be able to print the host-id when using the methods in UserClass view_profile(self).

The RenterClass has access to a similar variable called renter-id that is supposed to attach that renters id to their requests. 
requestAccommodation is responsible for allowing a user to send a request to a particular property, if a request already exist from that user to the accomodation then try again.
Same tiny view_profile(self) which works the same as for Host and allows the UserClass function to also print the Renters ID.

viewRequests is responsible for showing all the current requests to the renter that has issued them.

Then we have two pre_existing_host/renter that is a simple version of two different users that can be used to access the basics of the system however making your own account is advised.

create_account is responsible allowing a user to create their own account and put in necessary information like name and password but also their account type which is important for the functionality of the system.
When prompted with enough information it creates either a host or renter account depending on the inputted account_type.

login is responsible for allowing a user to access the rest of the system by checking if a there is a matching account in the user_database.

The Main function is simply a debugger. It does nothing exceptional save for trying out the various methods.
There are also a couple of example accommodations that way we dont always have to create new ones to try the functionalies.


