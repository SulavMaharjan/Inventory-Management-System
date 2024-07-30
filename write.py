#This module contain fucntion which is used to write the rented items
import datetime

def write_sold(name,number, list1, list2, list3 , list4,list5, quantity):
    #Construct the filename based on the customer's name
    filename = "RentItem/" + name + ".txt"
    #Open the file in write mode
    file = open(filename, "w")
    #Write header information including rental date,customer name,and phone number
    file.write("-----------------------------------------------\n")
    file.write("Rent Date and time:"+str(datetime.datetime.now()))
    file.write("\n Customer Name:" + name)
    file.write("\n Phone number : "+ str(number))
    file.write("\n"+"____________________________________")
    file.write("\nItem ID \t\tItem Name \t\t Quantity \t\tPrice")
    file.write("\n")
    #Iterate through rented items and their quantities
    for i in range(len(list1)):
        for i in range(len(quantity)):
            amount = str(quantity[i])
        file.write(list1[i]+"\t\t\t"+list2[i] +  "\t\t"+     amount+"\t\t"+  list4[i])
        file.write("\n")    
    total = 0
    #Calculate the total cost for all rented items
    for j in range (len(quantity)):
        total_quantity = str(quantity[j])
        for i in list4:
            i = i.replace("$","")
            total = (total + float(i))*int(total_quantity)
        print("\n")
    #Write the total cost to the file
    file.write("Total Cost " + str(total))
    #Reopen the file in read mode and print its contents
    filename = "RentItem/" + name + ".txt"
    file = open(filename, "r")
    file_contents = file.read()
    print(file_contents)
    file.close()#Close the file
