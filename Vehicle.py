# %%

import getpass
import re
from datetime import datetime

import rich
from rich.console import Console
from rich import print as rprint
from rich.table import Table, box
from rich.box import SQUARE
from rich.live import Live
from rich.progress import Progress

from ODBC import ODBC
import os
import time
class Vehicle(ODBC):
    
    def __init__(self):
        ODBC.__init__(self)
        
    def add_vehicle(self):
        
        self.clearScreen()
        veh_name = input('Enter the vehicle_name | Q to Quit  :  ')
        if veh_name.lower() == 'q':
            return False
        x1 = 1
        while x1:
            self.clearScreen()
            rprint('1. Bike')
            rprint('2. Car')
            type_choice = input('Choose Vehicle Type | Q to Quit  :  ')
            if type_choice.lower() == 'q':
                return False
            if type_choice == '1':
                type = 'Bike'
                x1 = 0
            elif type_choice == '2' :
                type = 'Car'
                x1 = 0
            else:
                self.clearScreen()
                rprint('Invalid Vehicle Choice ! Try Again ')
                
        self.clearScreen()
        no = input('Enter the vehicle_Number | Q to Quit  :  ')
        if no.lower() == 'q':
            return False
                
        x7 = 1
        while x7:
            try:
                self.clearScreen()
                veh_kms = (input('Distance Travelled by vehicle in kms | Q to Quit  :  '))
                if veh_name.lower() == 'q':
                    return False
                veh_kms = int(veh_kms)
                x7 = 0
            except ValueError as e:
                rprint('Enter distance in kms in integer format only')
                continue
        
        x2 = 1
        while x2:
            self.clearScreen()
            rprint('1. Seriviced')
            rprint('2. Yet to Service')
            serv_choice = input('Choose Vehicle Serviced status | Q to Quit  :  ')
            if serv_choice.lower() == 'q':
                return False
            if type_choice == '1':
                serv = 1
                x2 = 0
            elif type_choice == '2' :
                serv = 0
                x2 = 0
            else:
                print('Invalid Service Choice ! Try Again ')
                
        veh_availability = 1
        
        x8 = 1
        while x8:
            try:
                self.clearScreen()
                veh_rent_price = (input('Enter the Rent Price Amount (rupees) | Q to Quit  :  '))
                if veh_rent_price.lower() == 'q':
                    return False
                veh_rent_price = int(veh_rent_price)
                x8 = 0
            except:
                rprint('Enter Rent Price in rupees in integer format only')
                continue
            
        s_no = ODBC().s_no_max()
        return [s_no, veh_name, type, no, veh_kms, serv, veh_availability, veh_rent_price, 0]
    
    def view_vehicle(self):
        
        x1 = 1
        while x1:
            self.clearScreen()
            rprint('1. Vehicle_id')
            rprint('2. Vehicle_Name')
            rprint('3. Vehicle_Type')
            rprint('4. Vehicle_Number')
            rprint('5. Vehicle_KMS_Travelled')
            rprint('6. Vehicle_Serviced_Status')
            rprint('7. Vehicle_Rent_Status')
            rprint('8. Vehicle_Rent_Price')
            rprint('9. Vehicle_Rent_Count')
            print()
            choice_name = input("Enter your choice to view Info BY COLUMN NAME | Q to Quit  :  ")
            if choice_name.lower() == 'q':
                return False
            if choice_name == '1':
                name = 'VEHICLE_ID'
                x1 = 0
            elif choice_name == '2' :
                name = 'VEHICLE_NAME'
                x1 = 0
            elif choice_name == '3':
                name = 'VEHICLE_TYPE'
                x1 = 0
            elif choice_name == '4':
                name = 'VEHICLE_NUMBER'
                x1 = 0
            elif choice_name == '5':
                name = 'VEHICLE_KMS_TRAVELLED'
                x1 = 0
            elif choice_name == '6':
                name = 'VEHICLE_SERVICED_STATUS'
                x1 = 0
            elif choice_name == '7':
                name = 'VEHICLE_AVAILABILTY'
                x1 = 0
            elif choice_name == '8':
                name = 'VEHICLE_RENT_PRICE'
                x1 = 0
            elif choice_name == '9':
                name = 'VEHICLE_RENT_COUNT'
                x1 = 0
            else:
                rprint('Invalid Service Choice ! Try Again ')
                
        x2 = 1
        while x2:
            rprint('1. Ascending Order')
            rprint('2. Descending Order')
            print()
            order_choice = input('Enter your choice to view Info BY COLUMN Order type | Q to Quit  :  ')
            if order_choice.lower() == 'q':
                return False
            if order_choice == '1':
                order = False
                x2 = 0
            elif order_choice == '2' :
                order = True
                x2 = 0
            else:
                rprint('Invalid Service Choice ! Try Again ')
        
        self.clearScreen()
        res = ODBC().view_vehicle(name, order)
        if res:
            self.table_display(res)
    def table_display(self, res):
        
        print()
        table = Table(title="VEHICLE DETAILS", row_styles=["","bold"],header_style="bold",box=SQUARE)
        table.add_column("ID", style="magenta", no_wrap=True, justify="center")
        table.add_column("NAME", justify="center", style="green", no_wrap=True)
        table.add_column("TYPE", justify="center", style="yellow", no_wrap=True)
        table.add_column("NUMBER", justify="center", style="magenta", no_wrap=True)
        table.add_column("KMS_TRAVELLED", justify="center", style="green", no_wrap=True)
        table.add_column("RENT_PRICE", justify="center", style="magenta", no_wrap=True)
        table.add_column("RENT_COUNT", justify="center", style="green", no_wrap=True)
        table.add_column("SERVICED", justify="center", style="green", no_wrap=True)
        table.add_column("RENT_AVAIL", justify="center", style="green", no_wrap=True)
        c = 0
        for z,i in enumerate(res):
            c += 1
            temp = []
            for j in range(len(i)):
                if i[j] == 1 and j>5:
                    temp.append("✅")
                elif i[j] == 0 and j>5:
                    temp.append("❌")
                else:
                    temp.append(i[j])
            if c % 2 == 0:
                table.add_row(*[str(value) for value in temp])
            else:
                table.add_row(*[str(value) for value in temp])
        console = Console()
        console.print(table,no_wrap=True)
    def clearScreen(self):
        print()
        console = Console()
        with Progress(console=console) as progress:
            task = progress.add_task("[red]Processing Pls Wait...", total=5)
            for i in range(3):
                time.sleep(1)
                progress.update(task, advance=1)
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def search_vehicle(self, choice ,input_value):
        d = {1:'VEHICLE_NAME', 2:'VEHICLE_NO', 3:'S_NO'}
        res = ODBC().search_vehicle(choice, input_value)
        if res:
            self.table_display(res)
            return True
        else:
            print()
            rprint('No Vehicle Available with',d[choice] ,input_value)
            return False
    def view_vehicle_by(self, choice):
        
        res = ODBC().view_vehicle_by(choice)
        if res:
            self.table_display(res)
        else:
            rprint('No Vehicle Available')
    
    def modify_vehicle(self):
        
        while True:
            self.clearScreen()
            
            veh_no = input('Enter the Vehicle_ID | Q to back : ')
            if veh_no.lower() == 'q':
                return False
            print()
            veh_chk = self.search_vehicle(3,veh_no)
            if not veh_chk:
                break
            d =  {'1':'VEHICLE_NAME', '2':'VEHICLE_NO','3':'VEHICLE_TYPE', '4':'VEHICLE_KMS', '5':'VEHICLE_SERVICED', '6':'VEHICLE_AVAILABILTY', 
            '7':'VEHICLE_RENT_PRICE', '8':'VEHICLE_RENT_COUNT'}
            print()
            rprint('1. Vehicle_Name')
            rprint('2. Vehicle_Number')
            rprint('3. Vehicle_Type')
            rprint('4. Vehicle_KMS_Travelled')
            rprint('5. Vehicle_Serviced_Status')
            rprint('6. Vehicle_Rent_Status')
            rprint('7. Vehicle_Rent_Price')
            rprint('8. Vehicle_Rent_Count')
            print()
        
            while True:
                mod_choice = input('Enter the Column to MODIFY | Q to back : ')
                if mod_choice.lower() == 'q':
                    break
                elif mod_choice not in d:
                    print('Invalid Choice!!! Try Again')     
                    continue
                new_val = input("Enter the new Value to modify | Q to back :")
                if  new_val.lower() ==  'q':
                    break
                res = ODBC().modify_vehicle(d[mod_choice], new_val, int(veh_no))
                if res:
                    self.clearScreen()
                    print()
                    ODBC().search_vehicle(3,veh_no)
                    print('\nSuccessfully Modified')
                    break
                else:
                    print('Modification failed. Please try again with a correct value.')
                    break
# %%
