#holds the function that calls the combined database created in the first
#coursework.

import sqlite3 as sql
import pandas as pd

def Datacall(Database):

#creating a connection to the sql database created in coursework 1

    results = sql.connect(Database)

# Selecting each test to create a new table that stores all the tests together 

    MockTest = pd.read_sql(""" SELECT research_id, grade AS Mocktest
                   FROM dfCleanFormattedMockTest""",results)

    Test1 = pd.read_sql(""" SELECT research_id, grade AS Test1
                   FROM dfCleanFormattedTest1""",results)

    Test2 = pd.read_sql(""" SELECT research_id, grade AS Test2
                   FROM dfCleanFormattedTest2""",results)

    Test3 = pd.read_sql(""" SELECT research_id, grade AS Test3
                   FROM dfCleanFormattedTest3""",results)

    Test4 = pd.read_sql(""" SELECT research_id, grade AS Test4
                   FROM dfCleanFormattedTest4""",results)

    SumTest = pd.read_sql(""" SELECT research_id, grade AS SumTest
                   FROM dfCleanFormattedSumTest""",results)
           
     
    TotalTable= pd.merge(MockTest, Test1, on = 'research_id', how = 'outer')\
                    .merge(Test2, on = 'research_id', how = 'outer')\
                    .merge(Test3, on = 'research_id', how = 'outer')\
                    .merge(Test4, on = 'research_id', how = 'outer')\
                    .merge(SumTest, on = 'research_id', how = 'outer')
                                                
    results.close()
    
    return TotalTable



