#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# team: Daniel, Elsa
# expert of exercise block 1: Daniel V

import random
import time
import sys
import matplotlib.pyplot as plt

def get_random_number(start, end):
    num = random.randint(start, end)
    return num


def write_log_file(outputfilename, data):
    f = open(outputfilename + ".log", "a")
    f.write("Your randomly generated number is " + str(data) + " (" + time.strftime("%H:%M:%S") + ")\n")
    f.close()


if __name__ == "__main__":
    
    roll_list=[]
    for i in range(6):
        roll = get_random_number(1, 6)
        roll_list.append(roll)
    print(roll_list)
    sys.stdout.flush()
    
    outputfilename = "randomNumber"
    #roll = get_random_number(1, 100)
    write_log_file(outputfilename, roll)
    plt.bar(range(6),roll_list)
    plt.show()
