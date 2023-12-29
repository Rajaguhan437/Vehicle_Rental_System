#!/usr/bin/env python
# coding: utf-8

# In[3]:

import getpass
import re
from datetime import datetime
import rich
from rich.console import Console
from rich.table import Table
from rich import print as rprint
from rich import box
from rich.progress import Progress

class Account():
    
    def sign_up(self):

        name = input("Enter Your Name | Q to EXIT :  ")
        if name.lower() == 'q':
            return False
        
        x3 = 1
        while x3:
            date_str = input("Enter the date in the format DD-MM-YYYY | Q to EXIT  :  ")
            if date_str == 'Q'or date_str == 'q':
                return False
            date_lst = re.findall(r"(\d+)",date_str)
            date_str = '-'.join([i for i in date_lst])
            try:
                date_of_birth = datetime.strptime(date_str, "%d-%m-%Y")
                x3 = 0
                date = date_of_birth.date()
            except:
                rprint("Invalid date format. Please enter the date in the format DD-MM-YYYY.")
                
        x2 = 1
        while x2:
            rprint("Choose Your Gender:")
            rprint("1. MALE")
            rprint('2. FEMALE')
            rprint('3. OTHER')
            gender_choice = int(input("Select Your Gender | Q to EXIT :  "))
            if gender_choice == 'Q'or gender_choice =='q':
                return False
            if gender_choice == 1:
                gender = "M"
                x2 = 0
            elif gender_choice == 2:
                gender = "F"
                x2 = 0
            elif gender_choice == 3:
                gender = "O"
                x2 = 0
            else:
                rprint("Invalid Choice")
                rprint("Select Again")
                
        x4 = False
        while not x4:
            email = input("Enter your Email | Q to EXIT :  ")
            if email == 'Q'or email == 'q':
                return False
            valid = re.findall(r"([\w.]+@[\w.]+\.[a-z]+)",email)
            if valid!=[] and len(valid[0]) == len(email):
                x4 = True
            else:
                rprint("Invalid EMAIL",email)  
                
        username = input("Enter Your USERNAME | Q to EXIT  :  ")
        if username == 'Q'or username ==  'q':
            return False
        
        password, confirm_password = 0, 1
        while not (password == confirm_password):
            password = getpass.getpass("Enter Your Password | Q to EXIT  :  ")
            if password == 'Q'or password =='q':
                return False
            confirm_password = getpass.getpass("Confirm Your Password | Q to EXIT  :  ")
            if confirm_password == 'Q'or confirm_password =='q':
                return False
            if password!=confirm_password:
                print("Passwords Do Not Match!")
                
            
        x5 = False
        while not x5:
            no = (input("Enter your Phone Number | Q to EXIT  :  "))
            if no == 'Q'or no == 'q':
                return False
            phone_no = ''
            for i in no:
                if i in '1234567890':
                    phone_no+=i
            if len(phone_no) == 10:
                x5 = True
            else:
                rprint("Invalid Phone Number",phone_no)
        
        
        ID = 'C'+gender[0]+phone_no[:5]
        x1 = 1
    
        return [ID, name, date, gender, email, username, password, phone_no]
    
    def login(self):
        
        username = input("Enter your USERNAME or EMAIL :  ")
        if username == 'Q'or username ==  'q':
            return False
        password = getpass.getpass("Enter your password :  ")
        
        return [username, password]   
                
            


# %%
