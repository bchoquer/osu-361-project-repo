
import os
import random
import sys
import time


def main():
    while True: 
        time.sleep(4)

        f = open("prng-service.txt", "r+")
        textContents = f.read()

        if(textContents == "run"):
            f.seek(0)
            f.truncate(0)
            ranNum = random.randint(0,50)
            f.write(str(random.randint(0,50)))
        f.close()

main()
