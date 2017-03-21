"""This file is a module for the controller.py to use. Contains the Room
objects and handles them on a the room level.


Should be easily modified to work with 2.7.
Should work on Mac and Windows systems.

Tested with Python 3.5.
Tested on Linux systems.


Written by: Virginia Commonwealth University Linux Users Group"""

# Start standard library injections.
from random import randrange
# End standard library injections.


# Start custom injections.
from riddle import Riddle
# End custom injection.


class Room:
    """Creates Room objects for the Controller.py to use.


    Dependent on standard library modules:
        random: randrange

    Dependent on custom modules:
        riddle: Riddle"""

    def __init__(self, roomdict):
        """Create some Room object constants for easy access.


        Takes in the room dictionary for this purpose."""

        self.deathmsg = roomdict['death message.']
        self.entermsg = roomdict['enter message.']
        self.exitmsg = roomdict['exit message.']
        self.name = roomdict['room name.']
        self.roomdict = roomdict

    def riddler(self, riddleobj):
        """Uses the Riddle objects to prompt the user with questions and checks
        the input against the answers.


        Not to be called directly but by the start() function."""

        print('Riddle:')
        print(riddleobj.question)
        response = input('')
        if response.lower() in riddleobj.answers:
            print('You got it!')
        else:
            for line in range(len(self.deathmsg)):
                print(self.deathmsg[line])
            exit()
        return None

    def start(self):
        """Starts the room.


        Call this function from the controller and it will handle everything in
        the room."""

        count = 0
        riddlelist = []
        riddleobjlist = []
        for key in self.roomdict.keys():
            if key not in ['death message.', 'enter message.', 'exit message.',
                           'room name.']:
                riddlelist.append(key)
        for rid in riddlelist:
            nowriddleobj = Riddle(rid, self.roomdict[str(rid)])
            riddleobjlist.append(nowriddleobj)
        while count < 5:
            # Only 5 random riddles per room per session.
            self.riddler(riddleobjlist.pop(randrange(len(riddleobjlist))))
            if not riddleobjlist:
                break
            count += 1
        for line in range(len(self.exitmsg)):
            print(self.exitmsg[line])
        return None
