import pandas as pd #alias
import functions
df5 = pd.DataFrame(columns=['column1','column2'], 
                   index=[10, 11, 12], 
                   data=[[10,20], [15,25], [33, 43]])
functions.print_it('Two columns and 10 rows', df5)
# create another dataframe from parts and print it <<< TO DO
df6 = pd.DataFrame(columns=['price','rating'], 
                   index=['grapes', 'berry', 'banana'], 
                   data=[[10,20], [15,25], [33, 43]])
functions.print_it('Furits', df6)
