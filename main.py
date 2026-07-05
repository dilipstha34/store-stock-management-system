import datetime  # Import the datetime
import random    # Import the random 

from read import file_product, show_products
from write import write_products
from operation import purchase_products, sell_products

dict_product = {}  # Empty dictionary to store product data
data_product = 'product.txt'  # Define the filename for storing product data
print("\nWelcome to WeCare Store!")  

''' Main function to run 
the store management system'''
def main():

    """
    This function run in a loop and serves as the entry point for the program, loading product data,
    displaying the menu, and handling user choices for buying, selling, or exiting from program.
    Loads product data from 'product.txt' into a dictionary.

    Parameters: None
    
    Returns: None

    Raises:
    ValueError: If number except 1,2,3 or characters are entered.
    """
    
    products = file_product(dict_product, data_product)  # Load products from the file into the dictionary
    while True:  # Start an infinite loop for the menu
        show_products(products)  # Display the current product list
        print("\nMenu options:")  
        print("1. Buy/Restock products")  
        print("2. Sell products to customer")  
        print("3. Exit the program")  
        choose = input("Choose from menu options: ").replace(" ", "")
        try:
            choice=int(choose)
        except:
            print("Invalid input! Please enter number only!")
            continue
        if choice == 1:
            purchase_products(products, data_product)
        elif choice == 2:
            sell_products(products, data_product)
        elif choice == 3:
            print("Thank you for using WeCare Store! Please visit again!")
            break
        else:
            print("Invalid choice! Please select 1, 2, or 3.")
#Call the main function
main()
