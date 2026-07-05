'''Function to load products,
   from a file into the dict_product dictionary'''
def file_product(dict_product, data_product):
    
    """
    Load products from a file into the dict_product dictionary.

    This function clears the provided dictionary and populates it with product data
    from the specified file. Each line in the file is expected to contain product
    details separated by commas.

    Parameters:
        dict_product (dict): The dictionary to store product data, with product IDs as keys.
        data_product (str): The filename of the product data file.

    Returns:
        dict: The updated dictionary with product data loaded from the file.

    Notes:
        - The file is expected to have lines with at least 5 comma-separated fields:
          name, brand, stock, cost, origin.
        - Product IDs are generated sequentially starting from 1.
        - Empty lines or lines with fewer than 5 fields are ignored.
    """
    
    dict_product.clear()  # Clear the dictionary to start fresh
    file = open(data_product, 'r')  # Open the file in read mode
    
    for entry in file:  # Loop through each line in the file
        clean_line = entry.replace(" ", "").replace("\n", "")  # Remove spaces & newline
        if clean_line:  # Check if the line is not empty after cleaning
            parts = clean_line.split(',')  # Split the line into a list using comma 
            if len(parts) >= 5:  # Ensure the line has at least 5 fields (name, brand, stock, cost, origin)                 
                id = str(len(dict_product) + 1)  # Generate a product ID based on current dictionary size
                dict_product[id] = parts  # Store the product details in the dictionary with the ID as the key
                
    file.close()  # Close the file after reading
    return dict_product  # Return dictionary

'''Function to display,
   all products in a formatted table'''
def show_products(products):

    """
    Display all products in a formatted table.

    This function prints a table of all products in the provided dictionary,
    showing their ID, name, brand, stock, price, and origin.

    Parameters:
        products (dict): A dictionary containing product data with IDs as keys.

    Notes:
        - The price displayed is calculated as twice the cost price.
        - The table is formatted with fixed-width columns for readability.
    """
    
    print("\nAvailable Products:")  
    print("| ID  | Name               | Brand      | Stock    | Price  | Origin       |")  
    print("----------------------------------------------------------------------------")

    # For each product
    for id in products:         
        details = products[id]  # Get fields
        name = details[0]       # Name
        brand = details[1]      # Brand
        stock = details[2]      # Stock (string)
        cost = details[3]       # Cost (string)
        origin = details[4]     # Origin
        cost_price = float(cost) * 2    # Selling price
        
        # Calculate space using pre-defined width
        id_space = " " * (3 - len(id))  
        name_space = " " * (18 - len(name))  
        brand_space = " " * (10 - len(brand))  
        stock_space = " " * (8 - len(stock))  
        price_space = " " * (6 - len(str(int(cost_price))))  #(convert to int for display)
        origin_space = " " * (12 - len(origin))  

        # Construct the row string using concatenation
        row = (
            "| " + id + id_space + " | " +
            name + name_space + " | " +
            brand + brand_space + " | " +
            stock + stock_space + " | " +
            str(int(cost_price)) + price_space + " | " +
            origin + origin_space + " |"
        )
        print(row)

def display_purchase_invoice(supplier_name, date_str, items_list, net_cost, total_vat, total_cost):

    """
    Display a restock invoice in the terminal.

    This function prints a formatted restock invoice including supplier details,
    purchase date, list of purchased items, and summary totals in shell.

    Parameters:
        supplier_name (str): The name of the supplier.
        date_str (str): The date of the purchase in string format.
        items_list (list): A list of tuples, each containing details of a purchased item.
        net_cost (float): The total net cost of the purchase.
        total_vat (float): The total VAT amount.
        total_cost (float): The total cost including VAT.

    Return: none

    Raises: none
    """
    
    print("-" * 86)
    print("|                            WeCare Store (Restock Invoice )                          |")
    print("-" * 86)
    supplier_field = "Supplier name: " + supplier_name
    date_field = "Date: " + date_str
    spaces = 83 - len(supplier_field) - len(date_field)  # Calculate padding for alignment
    print("| " + supplier_field + " " * spaces + date_field + " |")
    print("-" * 86)
    print("| Id  |   Product Name       |    Brand        | Quantity   | Per Price  |  Amount    |")
    print("-" * 86)
    
    for id, name, brand, quantity, cost, net in items_list:  # Loop through purchased items
        id_str = id + " " * (3 - len(id))
        name_str = name + " " * (20 - len(name))
        brand_str = brand + " " * (15 - len(brand))
        quantity_str = " " * (10 - len(str(quantity))) + str(quantity)
        cost_str = " " * (10 - len(str(int(cost)))) + str(int(cost))
        net_str = " " * (10 - len(str(int(net)))) + str(int(net))
        row = "| " + id_str + " | " + name_str + " | " + brand_str + " | " + quantity_str + " | " + cost_str + " | " + net_str + " |"
        print(row)

    # Print row seperator    
    empty_id = " " * 3  # Empty space for ID
    empty_name = " " * 20
    empty_brand = " " * 15
    empty_quantity = " " * 10
    dashes_price = "-" * 10  # Dashes for price column
    dashes_amount = "-" * 10
    separator_row = "| " + empty_id + " | " + empty_name + " | " + empty_brand + " | " + empty_quantity + " | " + dashes_price + " | " + dashes_amount + " |"  # Construct separator
    print(separator_row)  # Print separator

    # Prepare summary data
    summaries = [
        ("Net Total", net_cost),  # Net total summary
        ("VAT%", total_vat),  # VAT summary
        ("Total Cost", total_cost)  # Total summary
    ]
    
    for i in range(len(summaries)):
        label, value = summaries[i]  # Loop through summaries
        label_str = label + " " * (10 - len(label))
        value_str = " " * (10 - len(str(int(value)))) + str(int(value))  # Right-align value
        summary_row = "| " + empty_id + " | " + empty_name + " | " + empty_brand + " | " + empty_quantity + " | " + label_str + " | " + value_str + " |"  # Construct summary row
        print(summary_row)  # Print summary row
        if i < len(summaries) - 1:  # Print separator between summaries (except after the last one)
            print(separator_row)
    print("-" * 86)

def display_sell_invoice(customer_name, date_str, items_list, total_amount):

    """
    Display a sell invoice in the terminal.

    This function prints a formatted sell invoice including customer details,
    sale date, list of sold items, and the total amount in shell.

    Parameters:
        customer_name (str): The name of the customer.
        date_str (str): The date of the sale in string format.
        items_list (list): A list of tuples, each containing details of a sold item.
        total_amount (float): The total amount of the sale.

    Return: none

    Raises: none
    """
    
    print("-" * 86)
    print("|                            WeCare Store (Sell Invoice)                              |")
    print("-" * 86)
    customer_field = "Customer name: " + customer_name  # Prepare customer info
    date_field = "Date: " + date_str  # Prepare date info
    spaces = 83 - len(customer_field) - len(date_field)  # Calculate space for alignment
    print("| " + customer_field + " " * spaces + date_field + " |")
    print("-" * 86)
    print("| Id  |   Product Name       |    Brand        | Quantity   | Per Price  |  Amount    |")
    print("-" * 86)
    
    for id, name, brand, quantity, free, price, total in items_list:  # Loop through sold items
        id_str = id + " " * (3 - len(id))
        name_str = name + " " * (20 - len(name))
        brand_str = brand + " " * (15 - len(brand))
        quantity_str = " " * (10 - len(str(quantity))) + str(quantity)
        price_str = " " * (10 - len(str(int(price)))) + str(int(price))
        amount_str = " " * (10 - len(str(int(total)))) + str(int(total))
        row = "| " + id_str + " | " + name_str + " | " + brand_str + " | " + quantity_str + " | " + price_str + " | " + amount_str + " |"  # Construct row
        print(row)

    # Print separator row    
    empty_id = " " * 3  # Empty space for ID
    empty_name = " " * 20
    empty_brand = " " * 15
    empty_quantity = " " * 10
    dashes_price = "-" * 10  # Dashes for price column
    dashes_amount = "-" * 10
    separator_row = "| " + empty_id + " | " + empty_name + " | " + empty_brand + " | " + empty_quantity + " | " + dashes_price + " | " + dashes_amount + " |"  # Construct separator
    print(separator_row)  # Print separator

    # Print empty row for spacing
    empty_row = "| " + empty_id + " | " + empty_name + " | " + empty_brand + " | " + empty_quantity + " | " + " " * 10 + " | " + " " * 10 + " |"  # Construct empty row
    print(empty_row)  # Print empty row
    print("-" * 86)

    # Print total cost row
    label_str = "Total Cost" + " " * (10 - len("Total Cost"))
    total_str = " " * (10 - len(str(int(total_amount)))) + str(int(total_amount))
    total_row = "| " + empty_id + " | " + empty_name + " | " + empty_brand + " | " + empty_quantity + " | " + label_str + " | " + total_str + " |"
    print(total_row)
    print("-" * 86)

    # Print total free products
    total_free = sum(i[4] for i in items_list)  # Sum the free items from all sales
    free_text = "Total free products: " + str(total_free)
    print("| " + free_text + " " * (83 - len(free_text)) + " |")  # Print free products
    print("-" * 86)
