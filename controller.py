"""This file uses a custom Riddle Game file, parses it, and prompts the user
with random rooms and a maximum of five random questions, until all rooms are
completed.


Should be easily modified to work with 2.7.
Should work on Mac and Windows systems.

Tested with Python 3.5.
Tested on Linux systems.


Written by: Virginia Commonwealth University Linux Users Group"""

# Start standard library injections.
from os.path import isfile
from platform import system
from random import randrange
if system != 'Windows':
    import readline
from subprocess import Popen
from time import sleep
from sys import exit
# End standard library injections.

# Start third party injections.
from room import Room
# End third party injections.


def start():
    """Call this to start the Riddle Game.


    Dependent on standard library modules:
        os.path: isfile
        platform: system
        random: randrange
        subprocess: Popen
        time: sleep"""

    while True:
        path = input('Enter the path of the game file: ')
        if isfile(path):
            break
        else:
            print('End the program by pressing Ctrl + C.')
    # Clear the screen now.
    if system() != 'Windows':
        Popen('clear')
    else:
        Popen('cls', shell=True)
    sleep(.01)
    roomobjlist = room_maker(path)
    count = 0
    while count < 5:  # Only five rooms per session.
        roomobj = roomobjlist.pop(randrange(len(roomobjlist)))
        print('You are in room: ')
        for line in range(len(roomobj.name)):
            print(roomobj.name[line])
        roomobj.start()
        if not roomobjlist:
            break
        count += 1
    print('You\'ve completed all the rooms!')


def room_maker(path):
    """Makes the rooms from the file found at the path given by the user.


    Returns a list of Room objects that are used and randomized by the start
    function.


    Dependent on standard library modules:
        sys: exit

    Dependent on custom modules:
        room: Room"""

    with open(path, 'r') as in_file:  # Might need to override file buffer.
        lines = in_file.readlines()
    nowroombool = False
    nowroomdict = dict()
    nowquestion = ''
    roomobjlist = []
    startbool = False
    questionbool = False
    # If true, expect the data type specified after #$Start [datatype].
    # If not true, expect end of room [#$End death message.].
    for nowline in lines:
        if nowline.endswith('\n'):
            nowline = nowline[:-1]
        if nowline.startswith('#$'):
            nowline = nowline[2:].lower()
            if nowline.startswith('start '):
                nowline = nowline[6:]
                if startbool:
                    print('\n[FAILURE TO READ FILE CORRECTLY]\n')
                    exit()
                else:
                    startbool = True
                nowmode = nowline
                if nowline == 'answers.':
                    continue
                elif nowline == 'question.':
                    nowquestion = ''
                    questionbool = True
                    continue
                nowroomdict[nowmode] = []
            elif nowline.startswith('end '):
                startbool = False
                if questionbool:
                    nowroomdict[nowquestion] = []
                    questionbool = False
                if nowline == 'end death message.':
                    nowroombool = True
            else:
                print('\n[FAILURE TO READ FILE CORRECTLY]\n')
                exit()
        else:
            try:
                if nowmode == 'answers.':
                    nowroomdict[nowquestion].append(nowline)
                    continue
            except KeyError:
                print('\n[FAILURE TO READ FILE CORRECTLY]\n')
                exit()
            if nowmode == 'question.':
                if not nowquestion:
                    nowquestion += nowline
                else:
                    nowquestion += ' ' + nowline
                continue
            nowroomdict[nowmode].append(nowline)
        if nowroombool:
            nowroombool = False
            room = Room(nowroomdict)
            nowroomdict = dict()
            roomobjlist.append(room)
    return roomobjlist


if __name__ == "__main__":
    start()
