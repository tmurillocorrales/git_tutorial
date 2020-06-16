#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# team: Daniel, Elsa

import random
import time
import sys
import sth

def get_random_number(start, end):
    num = random.randint(start, end)
    return num


def write_log_file(outputfilename, data):
    f = open(outputfilename + ".log", "a")
    f.write("My randomly generated number is " + str(data) + " (" + time.strftime("%H:%M:%S") + ")\n")
    f.close()

def get_colour_by_dice_roll(spots):
    colors=['green','red','yellow','pink','black','blue']
    return colors[spots]

if __name__ == "__main__":
    outputfilename = "randomNumber_color"
    roll = get_random_number(1, 6)
    color = get_colour_by_dice_roll(roll)
    write_log_file(outputfilename, [roll, color])
    
