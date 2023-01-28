# Scalability - Can have different tabs open and close easily 
# Accessability - Layout uses simple colors for people who are colorblind 
# Simplicity - Simple main menu and an Instructions tab for sleek design 
import collections
import math
import os

import PySimpleGUI as sg


# def menu():
#     print("Here are the options for you to see your GPA over time\n")
#     print("1.Instructions ")
#     print("2.Add new file")
#     print("3.Display Graph ")
#     print("4.Display Averages")
#     print("5.Quit")
    
# Add graphs using https://www.geeksforgeeks.org/how-to-embed-matplotlib-charts-in-tkinter-gui/

def main():
    print("Hello and Welcome to the GPA interface")

    
    layout = [[sg.Text("Hello from PySimpleGUI")], [sg.Button("Quit")], [sg.Button("Instructions")],[sg.Button("Display Graph")],[sg.Button("Display Averages")]],
    
    # Create the window
    window = sg.Window("Main Menu", layout,margins=(100, 100))
    
    # Create an event loop
    while True:
        event, values = window.read()
        # End program if user closes window or
        # presses the OK button
        if event == "Quit" or event == sg.WIN_CLOSED:
            break

    window.close()
    # choice = menu()
main()