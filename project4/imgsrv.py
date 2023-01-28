#Python Comment for prng service

import os
import random
import sys
import time


def main():
    while True:
        time.sleep(10)
        g = open("image-service.txt", "r+")
        textContents = g.read()
        
        if(textContents):
            numPicture = int(textContents) % 4 + 1
            path = "cs361-images/" + "cat_" + str(numPicture) + ".jpeg\n"
            g.seek(0)
            g.truncate(0)
            g.write(path)
            g.close()
            exit()
main()
