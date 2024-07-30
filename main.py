#Import necessary modules
import read
import operation
from read import item_dictionary
#Get the customer's name
name = input("Register your name to the shop's customer list: ")
print("\n")
#Print a welcome message

print("________________Welcome "  + name.upper()+" to the Event Rental Shop ______________ __" + "\n")

#Start an infinite loop for the main menu
while True:
    print("============Please choose your option==============")
    print("1: View the inventory of items.")
    print("2: Rent an item.")
    print("3: Return an item.")
    print("4: Exit the application.")
    print("\n")
    #Another loop to ensure valid input
    while True:
        try:
            print("-------------------------------------------------")
            option = int(input("Choose the option of your choice (1 to 4): "))
            break
        except:
            print("Entered option is invalid!!")
    #Check the chosen option and execute the corresponding action        
    if option == 1: 
        read.display()
        print("List of available items.")
    elif option == 2:
        operation.rent()
    elif option == 3:
        operation.return_()
    elif option == 4:
        print("________" + "Thank you for signing in. " + "________")
        #Open a file to write data
        file = open("equipmentdata.txt", "w")
        #Iterate through item_dictionary and write data to the file
        for key, value in item_dictionary.items():
            file.write(str(id) + ","+ value[0] + ","+ value[1] + ","+ value[2] + ","+ value[3])
            file.write("\n")
        file.close()
        break #exit the loop
    else:
        #Handle invalid input
        print("Please Enter the correct option!!!")
        print("Please choose the option again:" + "\n")

