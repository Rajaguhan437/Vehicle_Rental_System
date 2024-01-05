
from ODBC import ODBC
from Vehicle import Vehicle

from datetime import datetime
import os

import rich
from rich.console import Console
from rich.table import Table
from rich import print as rprint
from rich import box

import time

class Rent(ODBC, Vehicle):
    
    def book_rentals(self):
        
        while True:
            self.clearScreen()
            veh_no = input('Enter the Vehicle_ID | Q to back : ')
            if veh_no.lower() == 'q':
                return False
            print()
            veh_chk = Vehicle().search_vehicle(3,veh_no)
            if not veh_chk:
                break
            print()
            veh_type = veh_chk[0]
            
            x2 = 1
            while x2:
                
                rprint('Minimum to pay is 10,000 ')
                rprint('Maximum to pay is 30,000 ')

                deposit = input('Pay Deposit | Q to back ')
                if deposit.lower() == 'q':
                    break
                elif int(deposit)<10000:
                    rprint('Minimum Deposit is 10,000, Amount transacted Back')
                    rprint('Pay More than minimum to rent Vehicle')
                elif int(deposit)>30000:
                    rprint('Maximum Deposit is 30,000, Amount transacted Back')
                    rprint('Pay less than maximum to rent Vehicle')
                elif 10000<=int(deposit)<=30000:
                    rprint('Deposited Accepted')
                    x2 = 0
                else:
                    rprint('Invalid | Pay Again !!! ')
                    continue
                
                
                    
    