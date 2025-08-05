'-*- coding: utf-8 -*-'
import csv
b_file = 'bookings.csv'
with open(b_file,'w',newline = '') as file:
    obj = csv.writer(file)
    l = ["Cust_ID","name","address","ph_no","car_id","d_o_buying","d_o_return","remaining","fine"]
    obj.writerow(l)