                                                
import datetime
import write
import read
from read import item_id
from read import item_dictionary
# Function to handle renting items
def rent():
    list1 = []
    list2 = []
    list3 = []
    list4 = []
    list5 = []
    quantity = []
    number = []
    name = input("Enter the name of a customer: ")

    ans = 'y'
    while ans == 'y':
        try: 
            itemid = input("Enter the item id: ")
            if itemid in item_id:
                number = int(input("Enter your contact number: "))
                item = item_dictionary[itemid][3]
                if int(item) > 0:
                    # Collect details of the rented item
                    list1.append(itemid)
                    list2.append(item_dictionary[itemid][0])
                    list3.append(item_dictionary[itemid][1])
                    list4.append(item_dictionary[itemid][2])
                    list5.append(item_dictionary[itemid][3])

                    while True:
                        try:
                            amount = int(input("Enter the number of items you want to rent: "))
                            quantity.append(amount)
                            break
                        except ValueError:
                            print("Quantity should be an integer.")

                    print("Selected item is available. Processing your rental...")
                    ans = input("Do you want to rent other items? (y/n)")
                    # Write rental information to a file
                    write.write_sold(name, number, list1, list2, list3, list4, list5, quantity)
                    # Update the quantity of items in item_dictionary
                    for i in range(len(quantity)):
                        quantitys = quantity[i]
                        for i in list1:
                            a = int(item_dictionary[i][3])
                            total = int(a) - quantitys 
                            item_dictionary[i][3] = str(total)
                    print("\n")
                    print("---------Items have been rented successfully-----------" + "\n")
                else:
                    print("Selected item is out of stock. Please choose another item.")
            else:
                print('Invalid Item Id')
                break

        except ValueError:
            print("Entered contact number should be an integer.")

    
# Function to handle returning rented items
def return_():
    name = input("Please register your name:")
    list1 = []
    list2 = []
    list3 = []
    list4 = []
    list5 = []
    quantity = []
    value = "y"
    while value == "y":
        itemid = input("Enter the item id of the item rented:")
        if itemid in item_id:
            # Collect details of the returned item
            list1.append(itemid)
            list2.append(item_dictionary[itemid][0])
            list3.append(item_dictionary[itemid][1])
            list4.append(item_dictionary[itemid][2])
            list5.append(item_dictionary[itemid][3])
            while True:
                try:
                    amount = int(input("Enter the quantity of item rented:"))
                    quantity.append(amount)
                    break
                except:
                    print("Enter a valid amount of items")
        else:
            print("Invalid item id!! Please choose item id correctly")
        value = input("Do you have any other items to return (y/n)")
    # Call function to handle returning items
    return_item(name, list1, list2, list3, list4, list5, quantity)
    for i in list1:
        a = int(item_dictionary[i][3])
        b = a + int(amount)
        item_dictionary[i][3] = str(b)
# Function to write returned item details to a file       
def return_item(name, list1, list2, list3, list4, list5, quantity):
    filename = "ReturnedItems/" + name + ".txt"
    file = open(filename, "w")
    file.write("___________________________________________________\n")
    file.write("Current Date and time:" + str(datetime.datetime.now()))
    file.write("\nCustomer Name:" + name)
    file.write("\nItem ID \t\tItem Name \t\tQuantity \t\tPrice")
    file.write("\n")
    for i in range(len(quantity)):
        amount = str(quantity[i])
        file.write(list1[i]+"\t\t\t\t"+list2[i] +  "\t\t\t"+  amount+"\t\t"+list4[i])
        file.write("\n")
    
    total = 0
    for i in range(len(quantity)):
        total_quantity = quantity[i]
        for i in list4:
            i = i.replace("$", "")
            total += float(i) * total_quantity
    file.write("Total refund:" + "$" + str(total) + "\n")
    print("Total Refund: $" + str(total) + "\n")
    
    # Reopen and print the contents of the returned items file
    filename = "ReturnedItems/" + name + ".txt"
    file = open(filename, "r")
    file_contents = file.read()
    print(file_contents)
    file.close()


# This function is used to display to return the item for user.
def rent_item(name, list1, list2, list3, list4, list5, quantity):

    filename = "RentItem/" + name + ".txt"
    file = open(filename, "w")
    file.write("___________________________________________________\n")
    file.write("Current Date and time:" + str(datetime.datetime.now()))
    file.write("\nCustomer Name:" + name)
    file.write("\nItem ID \t\tItem Name \t\tQuantity \t\tPrice")
    file.write("\n")
    for i in range(len(quantity)):
        amount = str(quantity[i])
        for i in range(len(list1)):
            file.write(list1[i]+"\t\t\t\t"+list2[i] +  "\t\t\t"+  amount+"\t\t"+list4[i])
            file.write("\n")
    total = 0
    for i in range(len(quantity)):
        total_quantity = quantity[i]
        for i in list4:
            i = i.replace("$", "")
            total =( total + float(i)) *total_quantity
        file.write("Total cost:" + "$" + str(total)+"\n")
        print("Total Cost : "+"$",total , "\n")
    # Reopen and print the contents of the rent items file
    filename = "RentItem/" + name + ".txt"
    file = open(filename, "r")
    file_contents = file.read()
    print(file_contents)
