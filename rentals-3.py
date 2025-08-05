# -*- coding: utf-8 -*-

"""
Created on Sun Aug  3 11:33:40 2025

@author: yashoda.mp
"""
import os
import csv
from simple_colors import *
import time
import webbrowser

admin_file = 'admins.csv'
car_file = 'cars.csv'
b_file = 'bookings.csv' 

# l = ["car_id","car_name","no_plate","price","seats","type","category","fuel","engine\\battery_cap","mileage","availability","car_image"]
owner = "Ramesh"




# [[username1,pass1],[username2,pass2],[username3,pass3]]

def a_login(username):
    with open(admin_file,'r') as file:
        obj = csv.reader(file)
        for i in obj:
            if username in i:
                password = input('enter the password: ')
                if password == i[1]:
                    for i in '...':
                        print(i,end = '')
                        time.sleep(1)
                    
                    print(f'Welcome { username }')
                    print('\n','_'*35,sep = '')
                    print('\n\n','='*35,'\n\n',sep = '')
                    return True
                
                else:
                    print(red('incorrect password','bold'))
                    print('\n','_'*35,sep = '')
                    print('\n\n','='*35,'\n\n',sep = '')
                    return False
                   
        else:
            print(red(f'username { username } not found...','bold'))
            print('\n','_'*35,sep = '')
            print('\n\n','='*35,'\n\n',sep = '')
            
            return False
def add_admin(username):
    with open(admin_file,"a+",newline = '') as file :
         file.seek(0)
         obj = csv.reader(file)
         for i in obj:
             if username == i[0] :
                 print(green("admin already exist...","bold"))
                 break
         else:
             password = input("enter passowrd:")
             wobj = csv.writer(file)
             wobj.writerow([username,password])
             print(green(f"admin {username} registered...",'bold'))
             print()
def rem_admins(username):
    with open(admin_file,"r",newline = "") as file :
        obj = csv.reader(file)
        flag = 0
        for i in obj:
            if username == i[0] :
                flag = 1
            else :
                with open("temp.csv","a",newline = "") as temp :
                    tempobj = csv.writer(temp)
                    tempobj.writerow(i)
    if flag == 0 :
        print(red(f"admin {username} not registered",'bold'))
    else :
        print(green(f"admin {username} successfully removed",'bold'))
    os.remove(admin_file)
    os.rename("temp.csv",admin_file)
def add_cars():
    n = int(input("how many cars to add: "))
    print('enter the car details in the form \n(["car_id","car_name","no_plate","price","seats","type","category","fuel","engine\\battery_cap","mileage","availability","car_image"])')
    for i in range(n) :
        with open(car_file,"a",newline = '') as file :
            car = eval(input(f"Enter car {i + 1}: "))
            obj = csv.writer(file)
            obj.writerow(car)
    print(green("cars successfully added... ",'bold'))
            
def disp_cardetails():
    os.startfile(car_file)
                
def disp_availcar():

    with open(car_file,'r') as file:
        obj = csv.reader(file)
        print(black('  Car_id   |            Car_name             |   Price   |  Seats  |  Mileage |','bold'))
        print('='*79)
        for i in obj:
            if i[10] == 'yes':
                print(f'    {i[0]}   |{i[1]} {" " * (30 - len(i[1]))}  |    {i[3]}   |    {i[4]}    |  {i[9]}{ " " * (6 - len(i[9]))}  |')
                print('-'*79)
        
def car_booking():
    print('Do you know what to buy?[y/n]:')
    ch = input('Enter your choice:')
    if ch.lower() == 'y':
        disp_availcar()

        
    elif ch.lower() == 'n':
        seats = input('Please enter how many seater car are you looking for[5,7]')
        category = input("enter which category of car are you looking for ['economy','standard','luxury']: ")
        type_car = input('please enter the type of car your looking for ["suv","sedan","sports","van"]')
        with open(car_file,'r') as file:
            obj = csv.reader(file)
            rcars = []
            for i in obj:
                if seats.lower() in i and category.lower() in i and type_car.lower() in i:
                    rcars.append(i)
                
        if rcars == []:
            print(red('\nwe are really sorry....No cars at this moment',"bold"))
            return False
                
        else:
            print(black('  Car_id   |            Car_name             |   Price   |  Seats  |  Mileage |','bold'))
            print('='*79)
            for i in rcars:
                if i[10] == 'yes':
                    print(f'    {i[0]}   |{i[1]} {" " * (30 - len(i[1]))}  |    {i[3]}   |    {i[4]}    |  {i[9]}{ " " * (6 - len(i[9]))}  |')
                    print('-'*79)
                    
    print('\n\n')
    car_id = input(yellow("please enter the car id to buy: ",'bold'))
    with open(car_file,'r') as file:
        obj = csv.reader(file)
        for i in obj :
            if car_id in i :
                print("=" * 50)
                print(blue('CAR DETAILS','bold'))
                print('_' * 50)
                print('Car_id',' ' * (20 - len('car_id')),":",i[0],sep = '')
                print('Car_name',' ' * (20 - len('car_name')),":",i[1],sep = '')
                print('No_Plate',' ' * (20 - len('no_plate')),':',i[2],sep = '')
                print('Price',' ' * (20 - len('price')),":",i[3],sep = '')
                print('Type',' ' * (20 - len('type')),":",i[5],sep = '')
                print('Seats',' ' * (20 - len('seats')),":",i[4],sep = '')
                print('Fuel',' ' * (20 - len('fuel')),":",i[7],sep = '')
                print('Engine/battery_cap',' ' * (20 - len('engine/battery_cap')),":",i[8],sep = '')
                print('Mileage',' ' * (20 - len('milege')),":",i[0],sep = '')
                time.sleep(2)
                print("_" * 50)
                print()
                print("=" * 50)

                    
                print()
                ch = input("enter do you want to see the pic of the car[y/n]?")
                if ch.lower() == 'y':
                    webbrowser.open(i[11])
                    break
                else:
                    break
                        
        else:
            print('car_id not found')
            return False
                        
        confirm_order = input('Confirm order[y/n]: ')
        if confirm_order.lower() == "y":
            return car_id
        elif confirm_order.lower() == 'n':
            return False
        else:
            print('Invalid choice')
            return False     
            
def billing(car_id):
    with open(b_file,'r') as file:
        obj = csv.reader(file)
        for i in obj:
            pass
        cust_id = "CUST" + str(int(i[0][4:8]) + 1)
    
    name = input('enter your name: ')
    ph_no = input('enter your ph.no: ')
    address = input('enter your address please: ')
    email = input('enter your email: ')
    d_o_buying = "'" + input('enter the date of buying[dd/mm/yyyy]: ') + "'"
    d_o_return = "'" + input('enter date of returning: ') + "'"
    print('please wait')
    for i in '......':
        print(i,end = '')
        time.sleep(1)
    print()
    #making the availability of car as no
    with open(car_file,'r') as file:
        obj = csv.reader(file)
        for i in obj:
            if car_id == i[0]:
                price = int(i[3])
                i[10] = 'no'
                car_name = i[1]
            with open('temporary.csv',"a",newline='') as temp :
                tempobj = csv.writer(temp)
                tempobj.writerow(i)
    os.remove(car_file)
    os.rename('temporary.csv',car_file)

    with open(b_file,'a',newline = '') as file :
        obj = csv.writer(file)
        l = [cust_id,name,address,ph_no,car_id,d_o_buying,d_o_return,'nil',0]
        obj.writerow(l)

    t_duration = (int(d_o_return[1:3]) - int(d_o_buying[1:3]) ) + 30 * (int(d_o_return[4:6]) - int(d_o_buying[4:6])) + 365 * (int(d_o_return[7:11]) - int(d_o_buying[7:11]))

    transaction_id = payment(t_duration * price)
    print('\n\n')
    print(time.sleep(1))
    print('=' * 120)
    print(yellow("\t\t\t\t\t\t\t\t\t\t\t\t\t\t  INVOICE",'bold'))
    print('_' * 120)
    print('\n\n')
    print(f'\t123 Main street manglore,                                              Customer ID  :{cust_id}')
    print(f'\tCA12345                                                                Invoice date :{time.strftime("%d-%m-%Y")}')
    print('\t5555-5555-555')
    print('\tinfo@carrental.com')
    print()
    print('='*120,sep = '')
    print()
    print(f'\tNAME:     {name}'," " * (60 - len(name)) ,f'Phone Number :{ph_no}')
    print(f'\tadress:   {address}'," " * (60 - len(address)),f'Email        :{email}')
    print()
    print(black("\tRental Details:",'bold'))
    print('\t','-' * 86,sep = '')
    print('\t|          Car Descrition           |      Rental Period      |  Price  |  Duration  |')
    print('\t','-' * 86,sep = '')
    print(f'\t|{car_name}{" " * (35 - len(car_name))}|{d_o_buying}-{d_o_return}|  ₹{price}  |{t_duration}{" "* (12 - len(str(t_duration)))}|')
    print('\t','-' * 86,sep = '')
    print(black(f'\t|{" " * 35}|{" " * 25}|Total    |₹{int(price) * t_duration}{" " * (11 - len(str((int(price) * t_duration))))}|','bold'))
    print('\t','-' * 86,sep = '')
    print('\n\n')
    print(black('\tPayment Details','bold'))
    print('\tPayment mode     :Online Payment')
    print('\tTransaction ID   :',transaction_id,sep = '')
    print('\n\n')
    print('=' * 120)

def payment(price) :
    payment_url = 'https://pbs.twimg.com/media/E3XaIcYWQAUvOAh.png'
    print('TO Pay:',price)
    time.sleep(2)
    webbrowser.open(payment_url)
    transaction_id = input('please enter the transaction id:')
    return transaction_id

def show_bookings():
    with open(b_file,'r',newline = '') as file:
        obj = csv.reader(file)
        next(obj)
        print('=' * 129)
        print(yellow('\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tBOOKINGS','bold'))
        print('=' * 129)
        time.sleep(2)
        print('\n\n')
        print('-' * 129)
        print('|Customer_id| Customername |      address       |Phone Number|  Car ID  |  d_o_purchase  |  d_o_return  |remaining days|  fine  |')
        print('-' * 129)
        for i in obj:
            
            print(f'| {i[0]}  |{i[1]}{" " * (14 - len(i[1]))}|{i[2]}{" " * (20 - len(i[2]))}|{i[3]}{" " * (12 - len(i[3]))}|{i[4]}{" " * (10 - len(i[4]))}|{i[5]}{" " * (16 - len(i[5]))}|{i[6]}{" " * (14 - len(i[6]))}|{i[7]}{" " * (14 - len(i[7]))}|{i[8]}{" " * (8 - len(i[8]))}|')
            print('-' * 129)
        print('\n\n')
        
def update_fine():
    t = time.localtime()
    with open(b_file,'r',newline = '') as file:
         obj = csv.reader(file)
         with open("update.csv","a",newline = "") as temp:
             tempobj = csv.writer(temp)
             for i in obj :
                 if i[0] == 'c_id':
                     pass
                 elif i[7] == "returned" :
                     pass
                 else :
                     
                     date = t.tm_mday
                     mon = t.tm_mon
                     year = t.tm_year
                     owned_time = (date - int(i[5][1:3]) ) + 30 * (mon - int(i[5][4:6])) + 365 * (year - int(i[5][7:11])) 
                     t_duration = (int(i[6][1:3]) - int(i[5][1:3]) ) + 30 * (int(i[6][4:6]) - int(i[5][4:6])) + 365 * (int(i[6][7:11]) - int(i[5][7:11]))
                     r_time = t_duration - owned_time
                    
                         
                         
                     if  r_time >= 0:
                         i[7] = r_time
                     else :
                         i[7] = f"{-(r_time)} overtime"
                         with open(car_file,"r") as file1:
                             obj1 = csv.reader(file1)
                             for j in obj1 :
                                 if j[0] == i[4]:
                                     price = int(j[3])
                         fine = (-(r_time))*(price + 500)
                         i[8] = fine
                 tempobj.writerow(i)
    os.remove(b_file)
    os.rename("update.csv",b_file)
def alert():
    with open(b_file,'r',newline = '') as file:
        obj = csv.reader(file)
        next(obj)
        print('=' * 129)
        print(red('\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tALERTS!!','bold'))
        print('=' * 129)
        time.sleep(2)
        print('\n\n')
        print('-' * 129)
        print('|Customer_id| Customername |      address       |Phone Number|  Car ID  |  d_o_purchase  |  d_o_return  |remaining days|  fine  |')
        print('-' * 129)
        for i in obj:
            if int(i[8]) > 0 and i[7] != "returned":
                print(f'| {i[0]}  |{i[1]}{" " * (14 - len(i[1]))}|{i[2]}{" " * (20 - len(i[2]))}|{i[3]}{" " * (12 - len(i[3]))}|{i[4]}{" " * (10 - len(i[4]))}|{i[5]}{" " * (16 - len(i[5]))}|{i[6]}{" " * (14 - len(i[6]))}|{i[7]}{" " * (14 - len(i[7]))}|{i[8]}{" " * (8 - len(i[8]))}|')
                print('-' * 129)
        print('\n\n')
  
def return_car():
    cus_id = input("enter customer id: ")
    t = time.localtime()
    date = t.tm_mday
    mon = t.tm_mon
    year = t.tm_year
    with open(b_file,"r",newline = '') as file:
        obj=csv.reader(file)
        flag = 0
        for i in obj:
            if i[0] == 'c_id':
                pass
            else:
                owned_time = (date - int(i[5][1:3]) ) + 30 * (mon - int(i[5][4:6])) + 365 * (year - int(i[5][7:11])) 
                t_duration = (int(i[6][1:3]) - int(i[5][1:3]) ) + 30 * (int(i[6][4:6]) - int(i[5][4:6])) + 365 * (int(i[6][7:11]) - int(i[5][7:11]))
                
                if i[0] == cus_id:
                    if i[7] == 'returned':
                        print(red("you have already returned the car...",'bold'))
                        print()
                        flag = 2
                        
                    elif owned_time < t_duration:
                        print(red(f'You still have {i[7]} days to return...','bold'))
                        print()
                        flag = 2
                    else:
                        
                        car_id = i[4]
                        i[7] = 'returned'
                        flag = 1
            with open("temp1.csv",'a',newline = '') as temp:
                obj = csv.writer(temp)
                obj.writerow(i)
                
    os.remove(b_file)
    os.rename("temp1.csv",b_file)        
                                
            
    if flag == 0:
        print(red('Customer Id not found...','bold'))
        print()
        return
    elif flag == 2:
        return
        

    #making car available
    with open(car_file,'r') as file:
        obj = csv.reader(file)
        for i in obj:
            if car_id == i[0]:
                i[10] = 'yes'
            with open('temporary.csv',"a",newline='') as temp :
                tempobj = csv.writer(temp)
                tempobj.writerow(i)
    os.remove(car_file)
    os.rename('temporary.csv',car_file)
    
    with open(b_file,'r') as file1:
        obj1 = csv.reader(file1)
        next(obj1)
        for i in obj1:
            
            if i[0] == cus_id:
                with open(car_file,'r') as file2:
                    obj2 = csv.reader(file2)
                    for j in obj2:
                        if j[0] == i[4]:
                            print('\n\n')
                            print(time.sleep(1))
                            print('=' * 120)
                            print(yellow("\t\t\t\t\t\t\t\t\t\t\t\tFINAL INVOICE",'bold'))
                            print('_' * 120)
                            print('\n\n')
                            print(f'\t123 Main street manglore,                                              Customer ID  :{cus_id}')
                            print(f'\tCA12345                                                                Invoice date :{time.strftime("%d-%m-%Y")}')
                            print('\t5555-5555-555')
                            print('\tinfo@carrental.com')
                            print()
                            print('='*120,sep = '')
                            print()
                            print(f'\tNAME:     {i[1]}'," " * (60 - len(i[1])) ,f'Phone Number :{i[3]}')
                            print(f'\tadress:   {i[2]}'," " * (60 - len(i[2])),f'Car ID        :{i[4]}')
                            print()
                            print(black("\tRental Details:",'bold'))
                            print('\t','-' * 86,sep = '')
                            print('\t|          Car Descrition           |      Rental Period      |  Price  |  Duration  |')
                            print('\t','-' * 86,sep = '')
                            print(f'\t|{j[1]}{" " * (35 - len(j[1]))}|{i[5]}-{i[6]}|  ₹{j[3]}  |{owned_time}{" "* (12 - len(str(owned_time)))}|')
                            print('\t','-' * 86,sep = '')
                            print(f'\t|{" " * 35}|{" " * 25}|Subtotal |₹{(int(j[3]) * t_duration)}{" " * (11 - len(str((int(j[3]) * t_duration))))}|')
                            print('\t','-' * 86,sep = '')
                            print(f'\t|{" " * 35}|{" " * 25}|Fine     |₹{i[8]}{" " * (11 - len(i[8]))}|')
                            print('\t','-' * 86,sep = '')
                            print(black(f'\t|{" " * 35}|{" " * 25}|Total    |₹{(int(j[3]) * t_duration) + int(i[8])}{" " * (11 - len(str((int(j[3]) * t_duration) + int(i[8]))))}|','bold'))
                            print('\t','-' * 86,sep = '')
                            print('\n\n')
                            print(black('Payment Details','bold'))
                            print('Payment mode     :Online Payment')
                            if i[8] != '0':
                                transaction_id = payment(int(i[8]))
                                print('Transaction ID   :',transaction_id,sep = '')
                            else:
                                print('Not eligible')
                            print('\n\n')
                            print('=' * 120)
                            break
print('='*140)
print(" " *62,cyan('CAR RENTALS','bold'))
print('=' * 140)
print()
    
while True:
    update_fine()
    print('\n1.Book car\n2.Check available car\n3.Return car\n4.Admin\n5.Exit:')
    ch = int(input('Enter the choice:'))
    
    
    if ch == 1:
        car_id = car_booking()
        if car_id == False:
            
            print('We are sorry if we couldnt fullfill your expectation....\n')
        else:
            billing(car_id)
    elif ch == 2:
        disp_availcar()
    elif ch == 3:
        return_car()
    elif ch == 4:
        print('='*35)
        print('\t\t\t ',yellow('LOGIN','bold'))
        print('_'*35,'\n\n')
        username = input('enter username: ')
        login = a_login(username)
        if login == True and username == owner:
            time.sleep(2)    
            while True:
                time.sleep(2)
                print('\n1.Display Bookings\n2.Add cars\n3.Add admins\n4.Remove admins\n5.Show alerts\n6.Car details\n7.Exit')
                cho = int(input('Enter the choice:'))
                if cho == 1:
                    show_bookings()
                elif cho == 2:
                    add_cars()
                elif cho == 3:
                    user_name = input("enter username: ")
                    add_admin(user_name)
                elif cho == 4:
                    rusername = input("enter the admin to remove: ")
                    rem_admins(rusername)
                elif cho == 5 :
                    alert()
                elif cho == 6:
                    disp_cardetails()
                elif cho == 7:
                    print()
                    break
                else:
                    print(red('INVALID CHOICE...',"bold"))
        elif login == True:
            time.sleep(2)    
            while True:
                time.sleep(2)
                print('\n1.Display Bookings\n2.Add cars\n3.Show alerts\n4.Car details\n5.Exit')
                cho = int(input('Enter the choice:'))
                if cho == 1:
                    show_bookings()
                elif cho == 2:
                    add_cars()
                elif cho == 3 :
                    alert()
                elif cho == 4:
                    disp_cardetails()
                elif cho == 5:
                    print()
                    break
                else:
                    print(red('INVALID CHOICE...',"bold"))
    elif ch == 5:
        break
    else:
        print(red('INVALID CHOICE...',"bold"))

print('=' * 140)
print(' ' * 63,cyan('THANK YOU','bold'))
print('=' * 140)
                
                        
                    
                


