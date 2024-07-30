# This module changes the list of the movies in
# suitable data structure Dictionary and list.
def read_item():
    file = open("equipmentdata.txt", "r")
    content = file.readlines()
    list_movie = []
    item_dictionary = {}
#converting movies data in 2d list.
    for i in content:
        list_movie.append(i.replace("\n", "").split(","))

#converting 2d list in Dictionary.
    for i in range(len(list_movie)):
        key = list_movie[i][0]
        value = []
        for j in range(1, len(list_movie[0])):
            value.append(list_movie[i][j])
            item_dictionary[key] = value
    return item_dictionary

item_dictionary = read_item()

#appending key into the list.
def itemid():
    item_id = []
    for key in item_dictionary.keys():
        item_id.append(key)
    return item_id
item_id = itemid()

#Function to display the list of the movie.
def display():
    print("Item Id" + "\t\t"+ "Item name"+ "\t" + "Brand" + "\t\t" +"Price" + "\t\t" +  "Quantity" + "\t" )
    for key,value in item_dictionary.items():
        print(key+"\t\t"+value[0]+"\t"+value[1]+"\t\t"+value[2]+"\t\t\t"+value[3])
