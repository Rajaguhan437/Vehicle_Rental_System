#!/usr/bin/env python
# coding: utf-8

#%load_ext rich

# In[23]:


from ODBC import ODBC
from Login import Account
from Vehicle import Vehicle

import getpass
import re
from datetime import datetime
import os

import rich
from rich.console import Console
from rich.table import Table
from rich import print as rprint
from rich import box


class View(Account, Vehicle, ODBC):
    
    def __init__(self) -> None:
        super().__init__()
        
    def startup(self):
        
        x1 = 1
        while x1: 
            rprint("Vehicle Rental System welcomes You".center(70,"-"))
            rprint("1. SignUP")
            rprint("2. Login")
            rprint("Press Q to quit")
            print()
            log_choice = (input("Enter your Choice :  "))
            self.clearScreen()
            if log_choice == '1':
                details = Account.sign_up(self)
                print(details)
                if details:
                    ODBC().insert_account_details( details)
                    self.clearScreen()
                    print('Succesfully Registered')
                else:
                    self.clearScreen()
                    print('Exited')
                
            elif log_choice == '2':
                result = Account.login(self)
                if result:
                    self.cred_chk = ODBC().check_credentials(result[0], result[1])
                    if self.cred_chk:
                        self.clearScreen()
                        print('logged In')
                        return self.cred_chk
                    else:
                        continue
                else:
                    self.clearScreen()
                    print('Exited')
                
            elif log_choice.lower() == 'q':
                self.clearScreen()
                print('THANK YOU')
                return False
            
            else:
                self.clearScreen()
                print('Invalid Choice!!! Try Again')    
    
    def renter(self):
        x = 1
        while x:
            print()
            print()
            rprint('1. View Rentals')
            rprint('2. ADD Vehicle')
            rprint('3. View Serviced Vehicle')
            rprint('4. View Rented Out Vehicle')
            
            choice = input('Enter your choice : ')
            print()
    
    
    def admin(self):
        
        #details = self.cred_chk
        x = 1
        while x:
            print()
            print()
            rprint('1. ADD Vehicle')
            rprint('2. View Vehicle')
            rprint('3. View Serviced Vehicle')
            rprint('4. View Rented Out Vehicle')
            rprint('5. Search Vehicle BY Name')
            rprint('6. Search Vehicle BY Number')
            rprint('7. Remove Vehicle')
            rprint('8. Modify Vehicle')
            rprint('9. Log Out')
            print()
            
            choice = input('Enter your choice : ')
            print()
            
            if choice == '1':
                details  = Vehicle().add_vehicle()
                if details:
                    res = ODBC().add_vehicle_db(details)
                    if res:
                        self.clearScreen()
                        print('Successfully Added')
                continue
            
            elif choice == '2':
                Vehicle().view_vehicle()
                
            elif choice == '3':
                Vehicle().view_vehicle_by(1)
                
            elif choice == '4':
                Vehicle().view_vehicle_by(2)
                
            elif choice == '5':
                veh_name = input('Enter the Vehicle_name | Q to back : ')
                if veh_name == 'Q'or veh_name ==  'q':
                    continue
                Vehicle().search_vehicle(1, veh_name)
                
            elif choice == '6':
                veh_no = input('Enter the Vehicle_Number | Q to back : ')
                if veh_no == 'Q'or veh_no ==  'q':
                    continue
                Vehicle().search_vehicle(2, veh_no)

            elif choice == '7':
                veh_no = input('Enter the Vehicle_Number | Q to back : ')
                if veh_no == 'Q'or veh_no ==  'q':
                    continue
                ODBC().remove_vehicle(veh_no)
                
            elif choice == '8':
                Vehicle().modify_vehicle()
                
            elif choice == '9':
                self.clearScreen()
                print('Logged OUT')
                break
                
    def clearScreen(self):
        print()
        console = Console()
        with Progress(console=console) as progress:
            task = progress.add_task("[red]Processing Pls Wait...", total=5)
            for i in range(3):
                time.sleep(1)
                progress.update(task, advance=1)
        os.system('cls' if os.name == 'nt' else 'clear')
            


1# In[24]:


x = View()
y = x.admin()


# %%
