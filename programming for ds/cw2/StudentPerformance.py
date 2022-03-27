# searches for relevant id and test
#visulises the speicifc test using matplotlib
#stored as a function studentperformance 

import sqlite3 as sql
import pandas as pd
import matplotlib.pyplot as plt
from DAFunction import *

#defining the function.

def studentperformance(student_id, test):
    
    results = sql.connect('ResultDatabase.db')
    
    #create the connection to the database. 
    #setting the list to be relative grade 
    
    relative_grade = []
    
    DataAll = pd.read_sql('''SELECT * FROM ''' + test, results)
    DataStudent = pd.read_sql('''SELECT * FROM ''' + test + 
                              ''' WHERE research_id == ''' + str(student_id),
                              results)
    
    #using sql query to select the correct data
    
    absolute_grade = DataStudent.loc[:, 'Q1':]
    mean_grade = DataAll.loc[:, 'Q1':].mean()

    for i in range(0, len(mean_grade)):
        relative_grade.append(absolute_grade.iloc[0,i] - mean_grade[i])
        
        
    #creating relative grade, which is absoulte minus the grade. 

    print(relative_grade)

    x = absolute_grade.columns
    y = absolute_grade.iloc[0,:]

    x1 = absolute_grade.columns
    y1 = relative_grade
    
    #setting the x and y variables for the relevant graphs. 

    graph = fig, (absolute_val, relative_val) = plt.subplots(1, 2)
    fig.suptitle('Student #' + str(student_id) + ' Performance for ' + test)
    absolute_val.set_title('Absolute Results')
    absolute_val.bar(x,y)
    
    absolute_val.set(xlabel='Question Number', ylabel='Percentage Scored')
    relative_val.set_title('Realtive Performance')
    relative_val.bar(x1,y1)
    relative_val.set(xlabel='Question', ylabel='Relative Score')

    return graph

    #studentperformance(23, dfCleanFormattedTest1)
    #can unhash the statement to test outside of the function. 
