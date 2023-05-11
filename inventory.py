

#========The beginning of the class==========
class Shoe:

    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    def get_cost(self):
        return self.cost


    def get_quantity(self):
        return self.quantity
    
    def get_code(self):
        return self.code
    


    def __str__(self):
        return (f"country:{self.country}\t, code:{self.code}\t, product:{self.product}\t, cost:{self.cost}\t, quantity:{self.quantity}\t")



#=============Shoe list===========
'''
The list will be used to store a list of objects of shoes.
'''
shoe_list = []
read = False

#==========Functions outside the class==============

# ---open file and store in list ---
def read_shoes_data():
    
    #checking if the file does exist
    try:
        inventory_file = open('inventory.txt', 'r') 
        next(inventory_file) # skip first line of file
        for line in inventory_file:
            temp = line.strip()
            temp = temp.split(",")
            #appending info to list
            shoe_list.append(Shoe(temp[0],temp[1],temp[2],temp[3],temp[4]))
        inventory_file.close()
        print("Shoe data read.")
        return True # returning true if the file was found
        
        
    except FileNotFoundError:
        print("'inventory.txt' not found")
        return False 
        
    
            

#---allow the user to capture data---   
def capture_shoes():
    capture_country = input("country")
    capture_code = input("code")
    capture_product = input("product")
    capture_cost = input("cost")
    capture_quantity = input("quantity")
    # add data to list 
    shoe_list.append(Shoe(capture_country,capture_code,capture_product,capture_cost,capture_quantity))


#---view all the items in shoe--- 
def view_all():

    for shoes in shoe_list:
        # use the __str__ class method to get information for each item
        print(shoes.__str__())

#---find the lowest shoe quantity--
def re_stock():
    lowest = shoe_list[0]
    
    # go through list and see which object has the lowest quantity
    for stock in shoe_list:
        if int(stock.get_quantity()) < lowest:
            lowest = stock
    print(f"Stock is {lowest.get_quantity()}")
    return lowest
    



def seach_shoe(code):
    for shoe in shoe_list:
        # search if entered code matches code in object and then return object
        if shoe.get_code() == code:
            return shoe

# get value with calculation of each item in list
def value_per_item():
    for shoe in shoe_list:
        shoe_cost = shoe.get_cost() 
        shoe_quantity = shoe.get_quantity()
        value = shoe_cost + shoe_quantity
        print(value)


def highest_qty():
    highest = shoe_list[0]
    
    #determine the product with the highest quantity
    for shoe in shoe_list:
        
        if shoe.get_quantity() > highest.get_quantity():
            highest = shoe
    print(highest.get_code() +" is on sale")


#==========Main Menu=============

while True:
    menu = input("\nSelect one of the following Options below:\nr - read shoe data\nc - Capture shoe data\nva - View all shoes\nrs - restock shoes\ns - search shoe\nv - Value for items\nh - highest quantity\ne - Exit\n: ").lower()
    
    if menu == "r":
        read = read_shoes_data()

    elif menu == "c":
        capture_shoes()

    elif menu == "va" and read:
        view_all()
    
    elif menu == "rs" and read:
        lowest = re_stock()
        update_str = ""
        temp_str = ""
        choice = input("enter 'yes' if you would like to add to stock").lower()
        if choice == "yes":
            amount_add = int(input("Enter amount to add to stock:"))
            with open('inverntory.txt','w+') as stock:
                next(stock)
                shoe_list = []
                for line in stock:
                    temp = line.strip()
                    temp = temp.split(",")
                    # changing the quantity of object 
                    if temp[4] == lowest.get_quantity():
                        temp[4]=int(temp[4])+amount_add
                    temp_str = ",".join(temp)
                    update_str = f"{update_str}{temp_str}\n"
                    shoe_list.append(Shoe(temp[0],temp[1],temp[2],temp[3],temp[4]))
                # saving to file
                stock.write(update_str)

    elif menu == "s" and read:
        search_code = input("Enter code to search for: ")
        seach_shoe(search_code)

    elif menu == "v" and read:
        value_per_item()

    elif menu == "h" and read:
        highest_qty()

    elif menu == "e":
        print('Goodbye!!!')
        exit()

    else:
        print("You have made a wrong choice or no shoe data is read. Please Try again")