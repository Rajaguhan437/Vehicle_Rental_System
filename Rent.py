
from ODBC import ODBC
from Vehicle import Vehicle

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
            deposit = input('Pay Deposit ( Minimum to pay is 10,000 ) | Q to back ')
            if deposit.lower() == 'q':
                break
            if deposit<10000:
                print('Minimum Deposit is 10,000, Amount transacted Back')
    