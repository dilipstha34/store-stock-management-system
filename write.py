'''Function to write the products dictionary,
   back to the file'''
def write_products(products, data_product):

    """
    Write the products dictionary back to the file.

    This function overwrites the product data file with the current contents
    of the products dictionary.

    Parameters:
    products (dict): The dictionary containing product data.
    data_product (str): The filename of the product data file.

    Returns: None
    
    Raises: None
    """

    file = open(data_product, 'w')  # Open the product file in write mode (overwrites existing content)
    for id in products:  # each product ID in dictionary
        detail = products[id]  #  Get product details for this ID
        line = detail[0] + "," + detail[1] + "," + detail[2] + "," + detail[3] + "," + detail[4] + "\n"  # Construct a comma-separated line with a newline
        file.write(line)  # Write the line to the file
    file.close()  # Close the file

def write_purchase_invoice(supplier_name, date_str, items_list, net_cost, total_vat, total_cost):

    """
    Write a restock invoice to a file.

    This function generates a unique filename and writes a formatted restock
    invoice to it, including supplier details, purchase date, list of purchased
    items, and summary totals.

    Parameters:
    supplier_name (str): The name of the supplier.
    date_str (str): The date of the purchase in string format.
    items_list (list): A list of tuples, each containing details of a purchased item.
    net_cost (float): The total net cost of the purchase.
    total_vat (float): The total VAT amount.
    total_cost (float): The total cost including VAT.

    Returns: None
    
    Raises: None

    
    """

    import random
    inv_name = supplier_name + str(random.randint(1000, 9999)) + ".txt"  # Generate a unique invoice filename
    
    # Write the invoice to a file
    inv = open(inv_name, 'w')  # Open the invoice file in write mode
    inv.write("-" * 86 + "\n")
    inv.write("|                            WeCare Store (Restock Invoice )                          |\n")
    inv.write("-" * 86 + "\n")
    
    supplier_field = "Supplier name: " + supplier_name
    date_field = "Date: " + date_str
    spaces = 83 - len(supplier_field) - len(date_field)  # Calculate padding for alignment
    
    inv.write("| " + supplier_field + " " * spaces + date_field + " |\n")
    inv.write("-" * 86 + "\n")
    inv.write("| Id  |   Product Name       |    Brand        | Quantity   | Per Price  |  Amount    |\n")
    inv.write("-" * 86 + "\n")
    
    empty_id = " " * 3  # Empty space for ID
    empty_name = " " * 20
    empty_brand = " " * 15
    empty_quantity = " " * 10
    dashes_price = "-" * 10  # Dashes for price column
    dashes_amount = "-" * 10
    separator_row = "| " + empty_id + " | " + empty_name + " | " + empty_brand + " | " + empty_quantity + " | " + dashes_price + " | " + dashes_amount + " |"  # Construct separator
    
    for id, name, brand, quantity, cost, net in items_list:  # Loop through items
        id_str = id + " " * (3 - len(id))
        name_str = name + " " * (20 - len(name))
        brand_str = brand + " " * (15 - len(brand))
        quantity_str = " " * (10 - len(str(quantity))) + str(quantity)
        cost_str = " " * (10 - len(str(int(cost)))) + str(int(cost))
        net_str = " " * (10 - len(str(int(net)))) + str(int(net))
        row = "| " + id_str + " | " + name_str + " | " + brand_str + " | " + quantity_str + " | " + cost_str + " | " + net_str + " |"  # Construct row
        inv.write(row + "\n")  # Write row to file
        
    inv.write(separator_row + "\n")  # Write separator
    
    # Prepare summary data
    summaries = [
        ("Net Total", net_cost),  # Net total summary
        ("VAT%", total_vat),  # VAT summary
        ("Total Cost", total_cost)  # Total summary
    ]
    
    for i in range(len(summaries)):  # Loop through summaries
        label, value = summaries[i]
        label_str = label + " " * (10 - len(label))
        value_str = " " * (10 - len(str(int(value)))) + str(int(value))
        summary_row = "| " + empty_id + " | " + empty_name + " | " + empty_brand + " | " + empty_quantity + " | " + label_str + " | " + value_str + " |"  # Construct summary row
        inv.write(summary_row + "\n")  # Write summary row
        if i < len(summaries) - 1:  # Write separator between summaries (except after the last one)
            inv.write(separator_row + "\n")
    inv.write("-" * 86 + "\n")
    inv.close()  # Close the file

def write_sell_invoice(customer_name, date_str, items_list, total_amount):

    """
    Write a sell invoice to a file.

    This function generates a unique filename and writes a formatted 
    invoice to it, including customer details, sale date, list of sold items,
    and the total amount.

    Parameters:
    customer_name (str): The name of the customer.
    date_str (str): The date of the sale in string format.
    items_list (list): A list of tuples, each containing details of a sold item.
    total_amount (float): The total amount of the sale.
    
    Returns: None
    
    Raises: None
    """
    
    import random
    inv_name = customer_name + str(random.randint(1000, 9999)) + ".txt"  # Generate a unique invoice filename
    
    # Write the invoice to a file
    inv = open(inv_name, 'w')  # Open the invoice file in write mode
    inv.write("-" * 86 + "\n")
    inv.write("|                            WeCare Store (Sell Invoice)                              |\n")
    inv.write("-" * 86 + "\n")
    
    customer_field = "Customer name: " + customer_name  # Prepare customer info
    date_field = "Date: " + date_str  # Prepare date info
    spaces = 83 - len(customer_field) - len(date_field)  # Calculate space for alignment
    
    inv.write("| " + customer_field + " " * spaces + date_field + " |\n")
    inv.write("-" * 86 + "\n")
    inv.write("| Id  |   Product Name       |    Brand        | Quantity   | Per Price  |  Amount    |\n")
    inv.write("-" * 86 + "\n")
    
    empty_id = " " * 3  # Empty space for ID
    empty_name = " " * 20
    empty_brand = " " * 15
    empty_quantity = " " * 10
    dashes_price = "-" * 10  # Dashes for price column
    dashes_amount = "-" * 10
    separator_row = "| " + empty_id + " | " + empty_name + " | " + empty_brand + " | " + empty_quantity + " | " + dashes_price + " | " + dashes_amount + " |"  # Construct separator
    empty_row = "| " + empty_id + " | " + empty_name + " | " + empty_brand + " | " + empty_quantity + " | " + " " * 10 + " | " + " " * 10 + " |"  # Construct empty row
    
    for id, name, brand, quantity, free, price, total in items_list:  # Loop through sold items
        id_str = id + " " * (3 - len(id))
        name_str = name + " " * (20 - len(name))
        brand_str = brand + " " * (15 - len(brand))
        quantity_str = " " * (10 - len(str(quantity))) + str(quantity)
        price_str = " " * (10 - len(str(int(price)))) + str(int(price))
        amount_str = " " * (10 - len(str(int(total)))) + str(int(total))
        row = "| " + id_str + " | " + name_str + " | " + brand_str + " | " + quantity_str + " | " + price_str + " | " + amount_str + " |"  # Construct row
        inv.write(row + "\n")  # Write row to file
    
    inv.write(separator_row + "\n")  # Write separator
    inv.write(empty_row + "\n")  # Write empty row
    inv.write("-" * 86 + "\n")  # Write line
    
    # Print total cost row
    label_str = "Total Cost" + " " * (10 - len("Total Cost"))
    total_str = " " * (10 - len(str(int(total_amount)))) + str(int(total_amount))
    total_row = "| " + empty_id + " | " + empty_name + " | " + empty_brand + " | " + empty_quantity + " | " + label_str + " | " + total_str + " |"
    inv.write(total_row + "\n")  # Write total row
    inv.write("-" * 86 + "\n")  # Write line
    
    # Write total free products
    total_free = sum(i[4] for i in items_list)  # Sum the free items from all sales
    free_text = "Total free products: " + str(total_free)
    inv.write("| " + free_text + " " * (83 - len(free_text)) + " |\n")  # Write free products
    inv.write("-" * 86 + "\n")  # Write closing line
    inv.close()  # Close the file
