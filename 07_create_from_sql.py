import pandas as pd
import sqlite3 as db
import functions
file_name = 'ecars.db'
connection = db.connect(file_name)
my_cursor = connection.cursor()
countries = my_cursor.execute ('select * from countries')
rows= my_cursor.fetchall()
countries_df = pd.DataFrame(rows)
functions.print_it('df from query result: ', countries_df)
# create a dataframethat shows sales data from the sales table <<< TO DO
coutries = my_cursor.execute('select * from countries')
