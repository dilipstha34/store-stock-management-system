import datetime
import random
from read import display_purchase_invoice, display_sell_invoice
from write import write_products, write_purchase_invoice, write_sell_invoice

''' Function to handle purchasing products
    and generating a restock invoice'''
def purchase_products(products, data_product):

    """
    Handle purchasing products and generating a restock invoice.

    This function allows the user to purchase products, updates the product stock,
    calculates costs including VAT, displays the invoice, and writes it to a file.
    It validates input and handles errors for invalid IDs or quantities.

    Parameters:
    products (dict): The dictionary containing product data.
    data_product (str): The filename of the product data file.

    Return: none

    Raises: 
    KeyError: If the item id is not found in product file
    ValueError: If negative quantity or character is entered
    """
    
    supplier_name = input("Supplier name: ").replace(" ", "")
    items_list = []  # List to store purchased detail
    net_cost = 0
    total_vat = 0
    total_cost = 0
    
    while True:  # Start a loop to purchase multiple detail
        id = input("Product ID (1 - 8): ").replace(" ", "")
        # Check if the product ID exists
        if id not in products:
            print("Invalid product ID detected! Please enter Product ID between 1 and 8.")
            continue  # Restart the loop

        # Exception Handling
        try:
            quantity = int(input("Quantity: ").replace(" ", ""))
            if quantity <= 0:
                print("Invalid quantity! Quantity must be positive.")
                continue  # Restart the loop
        except ValueError:
            print("Invalid! Please enter numbers only.")
            continue  # Restart the loop
        
        detail = products[id]  # Get the product details list
        old_stock = int(detail[2])  # Convert current stock to integer
        detail[2] = str(old_stock + quantity)  # Update stock by adding purchased quantity and convert back to string
        cost = float(detail[3])  # Convert cost price to float
        net = cost * quantity  # Calculate net amount (cost * quantity)
        vat = net * 0.13  # Calculate VAT (13% of net)
        total = net + vat  # Calculate total (net + VAT)
        net_cost += net  # Add to running net cost
        total_vat += vat  # Add to running VAT total
        total_cost += total  # Add to running total cost
        items_list.append((id, detail[0], detail[1], quantity, cost, net))  #Add purchase details to item list(tuple)
        more = input("Do you want to purchase more products? (Y/N): ").replace(" ", "").upper()

        if more != 'Y':  # Exit loop if response is not 'Y'
            break
        
    DATE = datetime.datetime.now()
    date_str = str(DATE.year) + "-" + str(DATE.month) + "-" + str(DATE.day)  # Format date as string
    
    # Display the invoice in the terminal
    display_purchase_invoice(supplier_name, date_str, items_list, net_cost, total_vat, total_cost)
    
    # Call write function to write the invoice to a file
    write_purchase_invoice(supplier_name, date_str, items_list, net_cost, total_vat, total_cost)
    # Call write function to update products
    write_products(products, data_product)

''' Function to handle selling products
    and generating a sell invoice'''
def sell_products(products, data_product):

    """
    
    This function allows the user to sell products, updates the product stock,
    calculates the total amount, displays the invoice, and writes it to a file.
    It validates input and handles errors for invalid IDs, quantities, or insufficient stock.
    
    Parameters:
    products (dict): The dictionary containing product data.
    data_product (str): The filename of the product data file.

    Return: none
   
    Raises:
    KeyError: If the item id is not found in product file
    ValueError: If negative quantity or character is entered
    RuntimeError: If quantity is insufficient
    
    """
    
    customer_name = input("Customer name: ").replace(" ", "")
    items_list = []  # List to store sold items
    total_amount = 0
    
    while True:  # Start a loop to sell multiple items
        id = input("Product ID (1 - 8): ").replace(" ", "")
        if id not in products:  # Check if the product ID exists
            print("Invalid product ID detected! Please enter Product ID between 1 and 8.")
            continue
        # Exception handling
        try:
            quantity = int(input("Quantity: ").replace(" ", ""))
            if quantity <= 0:
                print("Invalid quantity! Quantity must be positive.")
                continue
        except ValueError:  # Handle non-numeric input
            print("Invalid! Please enter numbers only.")
            continue
        detail = products[id]  # Get the product details list
        stock = int(detail[2])  # Convert current stock to integer
        free = quantity // 3  # Calculate free items (1 free for every 3 purchased)
        inc_free = quantity + free  # Total items (purchased + free)
        if inc_free > stock:  # Check if enough stock is available
            print("Not enough stock")  
            continue  # Restart the loop
        
        cost = float(detail[3])  # Convert cost price to float
        sell_price = cost * 2  # Calculate selling price (twice the cost)
        total = quantity * sell_price  # Calculate total amount (quantity * selling price, free items not charged)
        detail[2] = str(stock - inc_free)  # Update stock by subtracting total items used
        total_amount += total  # Add to running total
        items_list.append((id, detail[0], detail[1], quantity, free, sell_price, total))  # Add sale details to items list(tuple)
        more = input("Do you want to sell more? (Y/N): ").replace(" ", "").upper()
        
        if more != 'Y':
            break
        
    DATE = datetime.datetime.now()
    date_str = str(DATE.year) + "-" + str(DATE.month) + "-" + str(DATE.day)  # Format date as string
    
    # Display the invoice in the terminal
    display_sell_invoice(customer_name, date_str, items_list, total_amount)
    
    # Call write function to write the invoice to a file
    write_sell_invoice(customer_name, date_str, items_list, total_amount)
    
    # Call write function to update products
    write_products(products, data_product)
