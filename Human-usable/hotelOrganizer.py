"""Hotel Organizer Library created by Ethan Hanlon. Avalible online at GitHub at https://github.com/Uberlyuber/Hotel-Organizer-Library/. Please, if you have an idea, do not hesitate to make a branch and start contributing!"""

guests = {}

def intro():
    print("Welcome to the Hotel Organizer software!")
def addGuest(guestAdd,guestAddRoom):
    if isinstance(guestAdd,str):
        if isinstance(guestAddRoom,int):
            guests[guestAdd] = guestAddRoom
        else:
            guestAddRoomProper = int(guestAddRoom)
            guests[guestAdd] = guestAddRoomProper
    else:
        guestAddProper = str(guestAdd)
        if isinstance(guestAddRoom,int):
            guests[guestAddProper] = guestAddRoom
        else:
            guestRoomProper = int(guestAddRoom)
            guests[guestAddProper] = guestRoomProper
def guestRemove(guestRemove):
   for i in guests:
       if i == guestRemove:
           del guests[guestRemove]
           break
def guestList():
    print("Guests | Room")
    for k,v in guests.iteritems():
        print str(k) + " | " + str(v)
def guestExistanceCheck(guest):
  for i,v in guests.iteritems():
    if i == guest:
      return True
      break

#Use import hotelOrganizer to include this library
