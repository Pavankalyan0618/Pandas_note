import pandas as pd #alias
import functions
grades_dict = {'Wally': [87, 96, 70],
               'Eva': [100, 87, 90],
               'Sam': [94, 77, 90],
               'Katie': [100, 81, 82],
               'Bob': [83, 65, 85]}
grades_df = pd.DataFrame(grades_dict)
grades_df.index = ['test1', 'test2', 'test3']
functions.print_it('Dictionary entries', grades_df)
# create a dataframe with 3-digit student numbers as index, 
# and data that stores three quiz grades  <<< TO DO
grades2_dictionary = {'name': ['Siri', 'bhnau', 'venkat'],
               'quiz1': [22, 87, 90],
               'quiz2': [94, 77, 90],
               'quiz3': [86, 81, 82],
               'quiz4': [83, 65, 85]}
grades2_df = pd.DataFrame(grades2_dictionary)
grades2_df.index = [355, 988, 102]
functions.print_it('Grade book 2', grades2_df)