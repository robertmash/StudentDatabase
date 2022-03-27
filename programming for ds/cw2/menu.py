#using gui enabling the user to navigate and access specific student 
#information. 

#importing the tkinter packages

import tkinter as tk
root = tk.Tk()
import tkinter.font

#importing the rest of the .py files so we can call the functions.

from testResults import *
from StudentPerformance import *
from underperformingStudents import *
from hardworkingStudents import *
from DAFunction import *

#creating my own custom font

NewFont = tkinter.font.Font(family = "MS Sans Serif",
                            size = 15,
                            weight = "bold")

#create a titlte and making the screen non resizable. 
root.title("Student Monitoring Menu")
root.resizable(False, False) 

#initally creating a canvas background
canvas = tk.Canvas(root, height = 600, width = 800, bg = "#34568B")
canvas.pack()

#creating a frame in which buttons and entries will be stored within.
frame = tk.Frame(root, bg = "white")
frame.place(relx = 0.1, rely = 0.1, relwidth = 0.8, relheight= 0.8)

#creating a title for the menu
Menu = tk.Label(root, text = "Welcome to the menu!", font = NewFont,
                  bg = "#34568B", fg = "white")
Menu.place(x = 290, y = 15)

#creates a drop down for the user pick the correct test they'd like to see. 


TestNames = ["dfCleanFormattedMockTest", "dfCleanFormattedTest1", 
                  "dfCleanFormattedTest2", "dfCleanFormattedTest3",
                  "dfCleanFormattedTest4",
                  "dfCleanFormattedSumTest"]

Test_txt = tk.StringVar()
Test_txt.set('Select a Test')
Test = tk.StringVar()
Test = tk.OptionMenu(frame, Test_txt, *TestNames)
Test.place(x = 20, y = 85)

#asks the user to input a valid student id to find their respective test.

StudentID = tk.Label(frame, text = "Enter a Student ID:",
                     fg = "white", bg ="#34568B")
StudentID.place(x = 20, y = 120)

StudentEntry = tk.Entry(frame)
StudentEntry.place(x = 20, y = 150)

#once the user clicks this button, runs the student performance function.
studentPerformance = tk.Button(frame, text = "Student Performance",
                               padx = 10, pady = 5,
                        fg = "white", bg ="#34568B", 
                        command = lambda: studentperformance(int(StudentEntry.get()),str(Test_txt.get())))

studentPerformance.place(x =20, y = 20)
    


#once the user clicks this button, displays underperforming students table
underperforming = tk.Button(frame, text ="Click for underperforming students", 
                            padx = 10, pady = 5,
                        fg = "white", bg ="#34568B",
                        command = lambda: UnderperformingStu())

underperforming.place(x = 400, y = 300)




#once the usre clicks this button, displays students that are overperforming
overperforming = tk.Button(frame, text ="Click for Hardworking students ", padx = 10, pady = 5,
                        fg = "white", bg ="#34568B",
                        command = lambda: hardworkingStudents())
overperforming.place(x = 400, y = 50)


#once the user enters the relevant student id and clicks the test results button,
#displays the results graphical for the student. 

StudentEntry2 = tk.Entry(frame)
StudentEntry2.place(x = 20, y = 340)

TestResults = tk.Button(frame, text ="Test Results", padx = 10, pady = 5,
                        fg = "white", bg ="#34568B",
                        command = lambda: Testresults(int(StudentEntry2.get())))
TestResults.place(x = 20, y = 260)

Student2Label = tk.Label(frame, text = "Enter a Student ID:",
                         fg = "white", bg = "#34568B")

Student2Label.place (x = 20, y = 300)


root.mainloop()
