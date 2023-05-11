# Object-Oriented-Programming
This is a program created for the hyperiondev bootcamp and it should include object-oriented programming. This programme looks at a companys inventory/stock txt file and allows
users to add, search and filter items from its txt file. The items are sorted in a specific order and need to be displayed in a specific/readable format. 
## Brief
- Must be able to search products by code.
- Determine the product with the lowest quantity and restock it.
- Determine the product with the highest quantity
- Calculate the total value of each stock item. The total value is calculated by
multiplying the cost by the quantity for each item entered into the system

### Key programe funtionality guide lines
- inside the class there needs to be 3 methods wiht functionality
  - get_cost - Returns the cost of the shoes.
  - get_quantity - Returns the quantity of the shoes.
  - __str__ - This method returns a string representation of a
class.
+ functions defined outside the class:
  + read_shoes_data - This function will open the file
inventory.txt and read the data from this file, then create a
shoes object with this data and append this object into the
shoes list.
  + capture_shoes - This function will allow a user to capture
data.
  + view_all - This function will iterate over the shoes list and
print the details of the shoes
  + re_stock - This function will find the shoe object with the
lowest quantity
  + seach_shoe - This function will search for a shoe from the list
using the shoe code and return this object so that it will be
printed.
  + value_per_item - This function will calculate the total value
for each item
  + highest_qty - Write code to determine the product with the
highest quantity and print this shoe as being for sale.


