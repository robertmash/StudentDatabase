#criteria for underperforming students: 

#1. removing those who scored > 70 in all tests
#2. remove disengaged students, this is individuals who have had 3 or more
# tests that havent been attempted or scored 0 in. 
#stored as a function to be accessed in my .menu file 

import sqlite3 as sql
import pandas as pd
import matplotlib.pyplot as plt
from DAFunction import *

def UnderperformingStu(): 

    underPerformingStudents =  Datacall('ResultDatabase.db')
    
    #calling our database function 
    
    underPerformingStudents.set_index('research_id', inplace = True)
    underPerformingStudents.sort_values(['research_id'], ascending = False)
    underPerformingStudents.fillna(0, inplace = True)
    
    #removing NA's, setting the index and sorting values in a decending order
    
    for cols in underPerformingStudents.columns:
        for s in underPerformingStudents.index:
            if underPerformingStudents.loc[s, cols] > 70:
                underPerformingStudents = underPerformingStudents.drop(index = s, axis = 0) 
                s += 1
            else:
                s+= 1
    underPerformingStudents.sort_values(['SumTest'], ascending = True, inplace = True)
    
    #removing research id based on criteria set above
    # Filtering out the disengaged students that havent attempted the tests. 
    
    count = []
    for i in underPerformingStudents.index:
        student_id = underPerformingStudents.loc[i, :]
        count.append((student_id == 0).sum())
        
    #setting a count to addition the amount of non-attempted tests
    
    underPerformingStudents = underPerformingStudents.assign(zeros = count)
    
    underPerformingStudents.drop(underPerformingStudents[underPerformingStudents.zeros > 3].index, 
                         inplace=True) 
    
    #from the column 'zeros' remove those with 'zeros' > 3
    
    underPerformingStudents.drop(['zeros'], axis = 1)
    
    #removing the column at the end of our filtering
    
    print(underPerformingStudents)
    
# UnderperformingStu() can add to call the function
    

    



    




    

    


