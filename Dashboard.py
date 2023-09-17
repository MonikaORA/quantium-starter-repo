#python Dashboard:
#Task 2 - preparing dataset for vizualization

import csv
import os

Directory="C:\\Users\\monika\\quantium-starter-repo\\data"
output_directory="C:\\Users\\monika\\output_file\\output_file.csv"

#opening output file
with open(output_directory,'w') as output_file:
     writer=csv.writer(output_file)
     #adding header
     header=["Sales","Date","Region"]
     writer.writerow(header)
     #iterating all files in data directory
     for file_name in os.listdir(Directory):
          #opening each file for reading
          with open(f"{Directory}\{file_name}","r") as input_file:
               reader=csv.reader(input_file)
               #iterating each row in csv file
               row_index=0
               for input_row in reader:
                    #process row other than csv header
                    if row_index > 0:
                         #collecting data from row
                         product=input_row[0]
                         raw_price=input_row[1]
                         quantity=input_row[2]
                         transaction_date=input_row[3]
                         region=input_row[4]
                         #if product is pinkmorsel ,processing it
                         if product=="pink morsel":
                              #formatting data
                              price=float(raw_price[1:])
                              sale= price * int(quantity)
                              #write to output file
                              output_row=[sale,transaction_date,region]
                              writer.writerow(output_row)
                    row_index+=1
