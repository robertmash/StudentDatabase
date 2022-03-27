#asks the user for their student id
#returns their grade from each test graphically
#function is called as Testresults

import sqlite3 as sql
import pandas as pd
import matplotlib.pyplot as plt
from DAFunction import *

def Testresults(student_id):
    
    global TotalTable

    TotalTable =  Datacall('ResultDatabase.db')
    
    #call totaltable which equates to the resultsdatabase
    

    TotalTable.fillna(0, inplace = True)
    TotalTable.sort_values(['research_id'], ascending = False)
    
    #sort the table by removing 0's and sorting research id 
    
    print(TotalTable)

    
    studentdf = pd.DataFrame(index = TotalTable.columns, columns = ['grades'])
    
    selection = TotalTable.drop(TotalTable.index[TotalTable['research_id'] != student_id])
    selection.set_index('research_id', inplace = True)
              
    # selection = TotalTable.filter(items = [student_id], axis = 0)
    # selection = selection.transpose()
    
    #create a data frame that selects the grades and the column headings
    
    x = list(selection.columns)
    y = list(selection.iloc[0,:])
    
    #set the x and y to be lists. 
    
    print(x)
    print(y)

    #plotting the x and y variables.  
    
    plt.bar(x, y)
    plt.title('Student ' + str(student_id) + ': Grades')
    plt.xlabel('Test Results')
    plt.ylabel('Percentage Scored')
    graph = plt.show()
    
    TotalTable.close
    
    return graph

    #returning the graph at the end 
    #Testresults("enter a student id")

    #un comment the above statement to test out of function. 



