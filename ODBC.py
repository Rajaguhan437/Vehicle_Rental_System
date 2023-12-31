#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pyodbc
pyodbc.drivers()
from typing import List, Tuple

import rich
from rich.console import Console
from rich.table import Table
from rich import print as rprint
from rich import box

# In[1]:



class ODBC():
    
    def __init__(self) -> None:
        
        connection_string = """
                        DRIVER={MySQL ODBC 8.2 Unicode Driver};
                        SERVER=127.0.0.1;
                        PORT=3306;
                        DATABASE=VRS;
                        USER=root;
                        PASSWORD=admin;
                        trusted_connection=Yes;
                    """
        self.conn = pyodbc.connect(connection_string)

        self.cursor = self.conn.cursor()  
    
    def s_no_max(self):
        
        query = 'SELECT MAX(S_NO) FROM VEHICLE'
        self.cursor.execute(query)
        result = self.cursor.fetchone()
        
        return result[0]+1
    
    
    def insert_account_details(self, details):
        
        query = 'INSERT INTO PERSON (PERSON_ID, NAME, DOB, GENDER, EMAIL, USERNAME, PASSWORD, CONTACT_NO, ROLE) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)'
        values = tuple(details)  # Make sure `details` contains all the necessary values

        # Execute the query using the correct syntax
        self.cursor.execute(query, values)
        self.cursor.commit()
        
    def check_credentials(self, username, password):
        query = 'SELECT * FROM PERSON WHERE USERNAME = ?'
        values = (username,)

        self.cursor.execute(query, values)
        result = self.cursor.fetchone()

        if result:
            query = 'SELECT * FROM PERSON WHERE USERNAME = ? and PASSWORD = ?'
            values = (username, password)

            self.cursor.execute(query, values)
            result = self.cursor.fetchone()

            if result:
                self.cursor.commit()
                return list(result)
            else:
                rprint('Invalid Password! Try Again')
                return False

        rprint('Invalid Username! Try Again')
        return False
        
    def add_vehicle_db(self, details):
        
        query = 'INSERT INTO VEHICLE (S_NO, VEHICLE_NAME, VEHICLE_TYPE, VEHICLE_NO, VEHICLE_KMS, VEHICLE_SERVICED, VEHICLE_AVAILABILTY, VEHICLE_RENT_PRICE, VEHICLE_RENT_COUNT) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)'
        values = tuple(details) 
        self.cursor.execute(query, values)
        self.cursor.commit()
        return True
    
    def view_vehicle(self, details: List[str], order: str = 'VEHICLE_NAME', desc: bool = False) -> List[List[str]]:
        
        query = f"SELECT S_NO, VEHICLE_NAME, VEHICLE_TYPE, VEHICLE_NO, VEHICLE_KMS, VEHICLE_RENT_PRICE,  VEHICLE_RENT_COUNT, VEHICLE_SERVICED, VEHICLE_AVAILABILTY  FROM VEHICLE ORDER BY {order} {'DESC' if desc else ''}"
        self.cursor.execute(query)
        veh_rows = list(self.cursor.fetchall())
        
        return veh_rows
    
    def view_vehicle_by(self, choice):
        d = {1:'VEHICLE_SERVICED', 2:'VEHICLE_AVAILABILTY'}
        if choice == 1:
            query = f"SELECT S_NO, VEHICLE_NAME, VEHICLE_TYPE, VEHICLE_NO, VEHICLE_KMS, VEHICLE_RENT_PRICE,  VEHICLE_RENT_COUNT, VEHICLE_SERVICED, VEHICLE_AVAILABILTY FROM VEHICLE WHERE {d[choice]} = TRUE"
        elif choice == 2:
            query = f"SELECT S_NO, VEHICLE_NAME, VEHICLE_TYPE, VEHICLE_NO, VEHICLE_KMS, VEHICLE_RENT_PRICE,  VEHICLE_RENT_COUNT, VEHICLE_SERVICED, VEHICLE_AVAILABILTY FROM VEHICLE WHERE {d[choice]} = FALSE"
            
        self.cursor.execute(query)
        veh_rows = list(self.cursor.fetchall())
        
        return veh_rows
    
    def search_vehicle(self, choice, name_number):
        d = {1:'VEHICLE_NAME', 2:'VEHICLE_NO', 3:'S_NO'}
        query = f"SELECT S_NO, VEHICLE_NAME, VEHICLE_TYPE, VEHICLE_NO, VEHICLE_KMS, VEHICLE_RENT_PRICE,  VEHICLE_RENT_COUNT, VEHICLE_SERVICED, VEHICLE_AVAILABILTY FROM VEHICLE WHERE {d[choice]} = '{name_number}'"

        self.cursor.execute(query)
        veh_rows = list(self.cursor.fetchall())
        
        return veh_rows
    
    def remove_vehicle(self, name_number):
        
        query = f"DELETE FROM VEHICLE WHERE VEHICLE_NO  = '{name_number}'"

        self.cursor.execute(query)
        self.cursor.commit()
        
    def update_vehicle(self, choice, name_number):
        d = {1:'VEHICLE_NAME', 2:'VEHICLE_NO'}
        
        query = f"SELECT S_NO, VEHICLE_NAME, VEHICLE_TYPE, VEHICLE_NO, VEHICLE_KMS, VEHICLE_RENT_PRICE,  VEHICLE_RENT_COUNT, VEHICLE_SERVICED, VEHICLE_AVAILABILTY FROM VEHICLE WHERE {d[choice]} = '{name_number}'"

        self.cursor.execute(query)
        veh_rows = list(self.cursor.fetchall())
        
        return veh_rows
        
    def modify_vehicle(self, col_name, val, veh_no):
        
        query = f"UPDATE VEHICLE SET {col_name} =  {val} WHERE S_NO = {veh_no}"
        try:
            self.cursor.execute(query)
            self.cursor.commit()
            return True
        except:
            return False
        
    def view_vehicle_rentals(self):
        
        query = f"SELECT S_NO, VEHICLE_NAME, VEHICLE_TYPE, VEHICLE_NO, VEHICLE_KMS, VEHICLE_RENT_PRICE,  VEHICLE_RENT_COUNT  FROM VEHICLE WHERE VEHICLE_AVAILABILTY = TRUE AND VEHICLE_SERVICED = TRUE"

        self.cursor.execute(query)
        veh_rows = list(self.cursor.fetchall())
        
        return veh_rows

# In[ ]:




