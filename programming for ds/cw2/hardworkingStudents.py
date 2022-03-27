#importing the relevant packages 
#as well as importing the student rate file to further filtering
#create a function to be accessed later on in the .menu file

import pandas as pd
import sqlite3 as sql
from DAFunction import *

student_rate = pd.read_csv("StudentRate.csv", index_col = (False))

student_rate.rename(columns = {'research id':'research_id',
        'What level programming knowledge do you have?':'knowledge'},
                    inplace = True)

student_rate = student_rate.loc[:,['research_id','knowledge']]

#create the student rate that just includes research id and the users skill level

student_rate.drop(student_rate.index[student_rate['knowledge'] != 'Beginner'] & 
          student_rate.index[student_rate['knowledge'] != 'Below beginner'],
          inplace = True)

beginners = list(student_rate.iloc[:,0])

#beginners is a list of all the ids related to being a beginner or below.

def hardworkingStudents():
    
    #creating a connection to the database.
    results = sql.connect('ResultDatabase.db')

    grades = []
    for x in range(0,len(beginners)):
    
        db_command = 'SELECT * FROM dfCleanFormattedSumTest'
        da_command = ' WHERE research_id == '
    
        table = pd.read_sql(db_command + da_command + str(beginners[x]),
                            results)
    
        if table.empty == True:
                grades.append(0)
        else:
            grades.append(table.loc[0,'grade'])
            
        #using the beginners list to filter the relevant users. 

    rate_grades = student_rate.assign(grade = grades)

    hardworking_students = rate_grades.drop(rate_grades.index[rate_grades['grade'] < 60])
    
    #drop all the values that are less than 60, to only keep grades above 60.
    
    hardworking_students.sort_values(['grade'],
                                     ascending = False, inplace = True)

    results.close()

    #close the connection. 
    
    print(hardworking_students)
    
# hardworkingStudents()





    