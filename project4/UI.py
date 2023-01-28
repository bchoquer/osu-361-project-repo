import os
import time


def main():
    while True:
        print("Enter 1 if you wish to see an image, 0 otherwise: ")
        userInput = input()
        
        if(userInput == "1"):
            # User chose option 1 to see an image
            #write run to prng service file
            f = open("prng-service.txt", "w")
            f.write("run")
            f.close()
            time.sleep(5)

            #read random number from prng service 
            f = open("prng-service.txt")
        
            #give random num to image service 
            g = open("image-service.txt", "r+")
            g.truncate(0)
            g.write(f.read())
            g.close()
            time.sleep(5)
            #read file path from img service 
            g = open("image-service.txt", "r+")
            textContents = g.read()
            print("\n file path" + textContents)
            
            g.close()
                
main()

