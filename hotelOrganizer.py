"""Hotel Organizer Library created by Ethan Hanlon. Avalible online at GitHub at (insert link here). Please, if you have an idea, do not hesitate to make a branch and start contributing!"""

def intro(self):
    print("Welcome to the Hotel Organizer software!")
def addGuest(self,guestAdd,guestAddRoom):
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
def guestRemove(self,guestRemove):
   for i in guests:
       if i == guestRemove:
           del guests[guestRemove]
def guestList(self):
    print("Guests | Room")
    for k,v in guests:
        print k + " | " + v

        #Use import hotelOrganizer to include this library
