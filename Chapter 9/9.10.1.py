class ItemToPurchase:
   """
       Class that holds details about shopping cart
   """
   def __init__(self):
       """
           Default constructor
       """
       # Initializing values with default values
       self.item_name = "none";
       self.item_price = 0;
       self.item_quantity = 0;
      
   def print_item_cost(self):
       """
           Method that prints the item name, quantity and price
       """
       print(self.item_name + " " + str(self.item_quantity) + " @ $" + str(self.item_price) + " = $" + str( self.item_price * self.item_quantity ));
      

def main():
   """
       Main function
   """
  
   print("Item 1");
  
   # Creating an object
   item1 = ItemToPurchase();
  
   # Reading data for item 1
   item1.item_name = input('Enter the item name:');
   item1.item_price = int(input('\nEnter the item price:'));
   item1.item_quantity = int(input('\nEnter the item quantity:'));
  
   print("\n\nItem 2");
  
   # Creating an object
   item2 = ItemToPurchase();
  
   # Reading data for item 2
   item2.item_name = input(' Enter the item name:');
   item2.item_price = int(input('\n Enter the item price:'));
   item2.item_quantity = int(input('\n Enter the item quantity:'));
  
   print("\n\n TOTAL COST");
  
   # Printing details of each item
   item1.print_item_cost();
   item2.print_item_cost();
  
   # Calculating total cost
   total = (item1.item_price * item1.item_quantity) + (item2.item_price * item2.item_quantity);
  
   # Printing total cost
   print("\n\n Total: $" + str(total));
  
# Calling main method  
main();
