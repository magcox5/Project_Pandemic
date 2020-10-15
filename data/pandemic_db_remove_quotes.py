import sqlite3
import os

conn = sqlite3.connect('pandemic_data_final.db')
c = conn.cursor() # The database will be saved in the location where your 'py' file is saved

# pandemic_final table consists of the following fields:
# 'index','Pandemic', 'Country', 'Year', 'Cases', 'Deaths', 'Lon', 'Lat', 'population'
c.execute('''select REPLACE(index,'"','')''')
                          
conn.commit()
