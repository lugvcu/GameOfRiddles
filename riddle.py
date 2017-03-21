"""This file is a module for the room.py to use. Contains the Riddle
objects.


Should be easily modified to work with 2.7.
Should work on Mac and Windows systems.

Tested with Python 3.5.
Tested on Linux systems.


Written by: Virginia Commonwealth University Linux Users Group"""


class Riddle:
    """A class of Riddle objects for the Room object to use.


    Created for collaborative and learning purposes."""

    def __init__(self, question, answers):
        """Creates some variables for easy access."""

        self.question = question
        self.answers = answers
