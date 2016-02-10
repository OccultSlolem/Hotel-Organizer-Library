import hotelOrganizer

def mainMenu():
  print("Main menu.")
  choice = raw_input("Please select an option.")
  if choice == "Help" or choice == "help":
    print("Type add to add a guest")
    print("Type remove to remove a guest")
    print("Type guests to see the guest list.")
    print("Type about to see credits.")
    print("Type help to see this help message")
    print("Type exit to exit this program")
    mainMenu()
  elif choice == "Add" or choice == "add":
    guestToAdd = raw_input("Who would you like to add?")
    guestToAddRoom = raw_input("What room will he be staying in?")
    hotelOrganizer.addGuest(guestToAdd,guestToAddRoom)
    print "Added!"
    mainMenu()
  elif choice == "Remove" or choice == "remove":
    guestToRemove = raw_input("Who would you like to remove?")
    if hotelOrganizer.guestExistanceCheck(guestToRemove):
      hotelOrganizer.guestRemove(guestToRemove)
    else:
      print("Sorry, this guest does not exist!")
    mainMenu()
  elif choice == "Guests" or choice == "guests":
    hotelOrganizer.guestList()
    mainMenu()
  elif choice == "About" or choice == "about":
    print("Hotel Organizer, version 1")
    print("(C) Ethan Hanlon, 2016. Copyrighted under CC-BY")
    print("AKA - Do whatever the hell you want with this code! It's even avalible on gitHub!")
    mainMenu()
  elif choice == "Exit" or choice == "exit":
      print("Thanks for using the Hotel Organizer program!")
      return("Closing.")
  else:
    print("Invalid command.")
    mainMenu()

mainMenu()
