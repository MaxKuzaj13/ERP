""" Sales module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * title (string): Title of the game sold
    * price (number): The actual sale price in USD
    * month (number): Month of the sale
    * day (number): Day of the sale
    * year (number): Year of the sale
"""

# everything you'll need is imported:
# User interface modulexxx
import ui
# data manager module
import data_manager
# common module
import common


file_name = "sales/sales.csv"
table = data_manager.get_table_from_file(file_name)
title_list = "ID", "Title", "Price", "Month", "Day", "Year"
list_labels = "ID: ", "Title: ", "Price: ", "Month: ", "Day: ", "Year: "
test_lista_id = ["kH34Ju#&", "jH34Ju#&", "kH35Jr#&", "kH94Jw#&"]     #TYLKO DO TESOWANIA, MOZNA POTEM WYJEBAC

ID = 0
TITLE = 1
PRICE = 2
MONTH = 3
DAY = 4
YEAR = 5


def start_module():
    """
    Starts this module and displays its menu.
     * User can access default special features from here.
     * User can go back to main menu from here.

    Returns:
        None
    """
    while True:
        list_options = ["Show table",
                   "Add",
                   "Remove",
                   "Update",
                   "Get lowest price item",
                   "Get items sold between",
                   "Get title by id",
                   "Get title by id from table",
                   "Get item id sold last",
                   "Get_item_id_sold_last_from_table",
                   "Get item title sold last from table",
                   "Get_the_sum_of_prices",
                   "Get_the_sum_of_prices_from_table",
                   "Get_customer_id_by_sale_id",
                   "Get_customer_id_by_sale_id_from_table",
                   "Get_all_customer_ids",
                   "Get_all_customer_ids_from_table",
                   "Get_all_sales_ids_for_customer",
                   "Get_all_sales_ids_for_customer_ids_from_table",
                   "Get_num_of_sales_per_customer_ids",
                   "Get_num_of_sales_per_customer_ids_from_table"
                        ]

        #options = list_options
        ui.print_menu("Sales options:", list_options, "(0) Back to main menu")
        inputs = ui.get_inputs(["Please enter a number: "], "")
        option = inputs[0]
        if option == "1":
            show_table(table)
        elif option == "2":
            add(table)
        elif option == "3":
            id_ = ui.get_inputs(["PODAJ ID:"], 'Enter ID:')
            remove(table, id_)
        elif option == "4":
            id_ = ui.get_inputs(["PODAJ ID:"], 'Enter ID:')
            update(table,id_)
        elif option == "5":
            get_lowest_price_item_id(table)
        # elif option == '6':
        #     ui.print_result(get_items_sold_between(table, month_from, day_from, year_from, month_to, day_to, year_to))
        elif option == "7":
            id_ = input("PODAJ ID: ")
            ui.print_result(get_title_by_id(id_), 'TITLE BY ID')
        elif option == "8":
            id_ = input("PODAJ ID: ")
            # id_ = ui.get_inputs(["PODAJ ID: "], "")
            ui.print_result(get_title_by_id_from_table(table, id_), 'TITLE BY ID')
        elif option == '9':
            ui.print_result(get_item_id_sold_last(), 'SOLD LAST')
        elif option == '10':
            ui.print_result(get_item_id_sold_last_from_table(table), 'ID OF ITEM SOLD LAST TIME')
        elif option == '11':
            ui.print_result(get_item_title_sold_last_from_table(table), 'TITLE')
        elif option == "12":
            print(get_the_sum_of_prices(test_lista_id))  # TYLKO DO TESTOW
            #TODO ZAKOMENTOWAŁEM BO PRZEKAZUJESZ ZMIENNE zmień na ui print_result lub na print -
        # elif option == "13":
        #     get_the_sum_of_prices_from_table((table, item_ids))
        # elif option == '14':
        #     get_customer_id_by_sale_id(sale_id)
        # elif option == '15':
        #       get_customer_id_by_sale_id_from_table(table, sale_id)
        elif option == '16':
            print('CUSTOMERS ID: ', get_all_customer_ids())
        elif option == '17':
            print(get_all_customer_ids_from_table(table))
        elif option == '18':
            get_all_sales_ids_for_customer_ids()
        elif option == '19':
            get_all_sales_ids_for_customer_ids_from_table(table)
        elif option == '20':
            ui.print_result(get_num_of_sales_per_customer_ids(), '')
        elif option == '21':
            ui.print_result(get_num_of_sales_per_customer_ids_from_table(table), '')
        elif option == "0":
            break


def show_table(table):
    """
    Display a table

    Args:
        table (list): list of lists to be displayed.

    Returns:
        None
    """
    title_list = "ID", "Title", "Price", "Month", "Day", "Year"
    ui.print_table(table, title_list)
    #ui.print_menu("Sales options:", list_options, "(0) Back to main menu")

def add(table):
    """
    Asks user for input and adds it into the table.

    Args:
        table (list): table to add new record to

    Returns:
        list: Table with a new record
    """

    list_labels = "Title: ", "Price: ", "Month: ", "Day: ", "Year: "
    id_record = common.generate_random(table)
    new_rec = ui.get_inputs(list_labels, "")
    new_record = []
    new_record.append(id_record)
    for row in new_rec:
        new_record.append(row)
    #new_record = [id_record, new_rec]
    table.append(new_record)
    file_name = "sales/dupa.csv"
    data_manager.write_table_to_file(file_name, table)
    return table


def remove(table, id_):
    """
    Remove a record with a given id from the table.

    Args:
        table (list): table to remove a record from
        id_ (str): id of a record to be removed

    Returns:
        list: Table without specified record.
    """
    for row in table:
        if id_[0] in row:
            table.remove(row)
    data_manager.write_table_to_file(file_name, table)

    return table


def update(table, id_):
    """
    Updates specified record in the table. Ask users for new data.

    Args:
        table (list): list in which record should be updated
        id_ (str): id of a record to update

    Returns:
        list: table with updated record
    """

    # your code
    labels = ["Title: ", "Price: ", "Month: ", "Day: ", "Year: "]
    updated_row=[]
    temp_list=[]
    counter=0
    ifWrong=True
    for row in table:

        if row[0] == id_[0]:
            ifWrong=False
            updated_row.append(id_[0])
            temp_list=ui.get_inputs(labels, "Please put new data:")
            for rec in temp_list:
                updated_row.append(rec)
            table[counter]=updated_row
        counter+=1

    if ifWrong == True:
        ui.print_error_message("Id doesn't exist")

    data_manager.write_table_to_file(file_name, table)
    return table


# special functions:
# ------------------

def get_lowest_price_item_id(table):
    """
    Question: What is the id of the item that was sold for the lowest price?
    if there are more than one item at the lowest price, return the last item by alphabetical order of the title

    Args:
        table (list): data table to work on

    Returns:
         string: id
    """
    price = 2
    id_price = 0
    name_game = 1
    # your code
    min_price = 100
    for row in table:
        if min_price > int(row[price]):
            min_price = int(row[price])
    for row in table:
        if int(row[price]) == min_price:
            print("\n\tID of cheapest game is: ",row[id_price],  " Name of this game is:", row[name_game], "\n ")


def get_items_sold_between(table, month_from, day_from, year_from, month_to, day_to, year_to):
    """
    Question: Which items are sold between two given dates? (from_date < sale_date < to_date)

    Args:
        table (list): data table to work on
        month_from (int)
        day_from (int)
        year_from (int)
        month_to (int)
        day_to (int)
        year_to (int)

    Returns:
        list: list of lists (the filtered table)
    """



def get_title_by_id(id_):

    """
    Reads the table with the help of the data_manager module.
    Returns the title (str) of the item with the given id (str) on None om case of non-existing id.

    Args:
        id (str): the id of the item

    Returns:
        str: the title of the item
    """


    name_game = 1
    id_column = 0

    for item in table:
        if item[id_column] == id_:
            return item[name_game]
    else:
        return 'ID NOT FOUND'


def get_title_by_id_from_table(table, id_):


    """
    Returns the title (str) of the item with the given id (str) on None om case of non-existing id.

    Args:
        table (list of lists): the sales table
        id (str): the id of the item

    Returns:
        str: the title of the item
    """


    name_game = 1
    id_column = 0


    for item in table:
        if item[id_column] == id_:
            return item[name_game]
    else:
        return 'ID NOT FOUND'

def get_item_id_sold_last():
    """
    Reads the table with the help of the data_manager module.
    Returns the _id_ of the item that was sold most recently.

    Returns:
        str: the _id_ of the item that was sold most recently.
    """

    #

    # id_column = 0
    # sum_date_table = []
    #
    # max_date = 0
    # dict = { key : value}

    # for data in table:
    #     sum_date_table.append(data[id_column])
    #     if(len(data[MONTH])) < 2:
    #         data[MONTH] = '0' + data[MONTH]
    #         sum_date = (data[YEAR] + data[MONTH] + data[DAY])
    #         sum_date_table.append(int(sum_date))
    #     elif(len(data[DAY])) < 2:
    #         data[DAY] = '0' + data[DAY]
    #         sum_date = (data[YEAR] + data[MONTH] + data[DAY])
    #         sum_date_table.append(int(sum_date))
    #     else:
    #         sum_date = (data[YEAR] + data[MONTH] + data[DAY])
    #         sum_date_table.append(int(sum_date))
    # print(sum_date_table)

    # get_item_id_sold_last_from_table(table)

    YEAR = 5
    MONTH = 3
    DAY = 4
    ID = 0

    latest_year = 0
    latest_month = 0
    latest_day = 0

    for row in table:
        if int(row[YEAR]) > latest_year:
            latest_year = int(row[YEAR])
    for row in table:
        if int(row[MONTH]) > latest_month and int(row[YEAR]) == latest_year:
            latest_month = int(row[MONTH])
    for row in table:
        if int(row[DAY]) > latest_day and int(row[YEAR]) == latest_year and int(row[MONTH]) == latest_month:
            latest_day = int(row[DAY])
            last_sold_id = row[ID]
    return last_sold_id



def get_item_id_sold_last_from_table(table):
    """
    Returns the _id_ of the item that was sold most recently.

    Args:
        table (list of lists): the sales table

    Returns:
        str: the _id_ of the item that was sold most recently.
    """

    YEAR = 5
    MONTH = 3
    DAY = 4
    ID = 0


    latest_year = 0
    latest_month = 0
    latest_day = 0

    for row in table:

        if int(row[YEAR]) > latest_year:
            latest_year = int(row[YEAR])
    for row in table:
        if int(row[MONTH]) > latest_month and int(row[YEAR]) == latest_year:
            latest_month = int(row[MONTH])
    for row in table:
        if int(row[DAY]) > latest_day and int(row[YEAR]) == latest_year and int(row[MONTH]) == latest_month:
            latest_day = int(row[DAY])

        if row[YEAR] > latest_year:
            latest_year = row[YEAR]
    for row in table:
        if row[MONTH] > latest_month and row[YEAR] == latest_year:
            latest_month = row[MONTH]
    for row in table:
        if row[DAY] > latest_day and row[YEAR] == latest_year and row[MONTH] == latest_month:
            latest_day = row[DAY]

            last_sold_id = row[ID]
    return last_sold_id


def get_item_title_sold_last_from_table(table):
    """
    Returns the _title_ of the item that was sold most recently.
    Args:
        table (list of lists): the sales table
    Returns:
        str: the _title_ of the item that was sold most recently.
    """

    YEAR = 5
    MONTH = 3
    DAY = 4
    TITLE = 1

    latest_year = 0
    latest_month = 0
    latest_day = 0

    for row in table:
        if int(row[YEAR]) > latest_year:
            latest_year = int(row[YEAR])
    for row in table:
        if int(row[MONTH]) > latest_month and int(row[YEAR]) == latest_year:
            latest_month = int(row[MONTH])
    for row in table:
        if int(row[DAY]) > latest_day and int(row[YEAR]) == latest_year and int(row[MONTH]) == latest_month:
            latest_day = int(row[DAY])
            last_sold_id = row[TITLE]
    return last_sold_id


    last_sold_id = get_item_id_sold_last_from_table(table)
    for row in table:
        if row[ID] == last_sold_id:
            return row[TITLE]



def get_the_sum_of_prices(item_ids):
    """
    Reads the table of sales with the help of the data_manager module.
    Returns the sum of the prices of the items in the item_ids.

    Args:
        item_ids (list of str): the ids

    Returns:
        number: the sum of the items' prices
    """

    i = 0
    id_column = 0
    price_column = 2
    price_sum = 0
    for row in table:
        if row[id_column] in item_ids:
            price_sum += int(row[price_column])
            #print(price_sum)
        i += 1
    return price_sum



def get_the_sum_of_prices_from_table(table, item_ids):
    """
    Returns the sum of the prices of the items in the item_ids.

    Args:
        table (list of lists): the sales table
        item_ids (list of str): the ids

    Returns:
        number: the sum of the items' prices
    """

    i = 0
    id_column = 0
    price_column = 2
    price_sum=0
    for row in table:
        if row[id_column] in item_ids:
            price_sum += int(row[price_column])
        i += 1
    return price_sum


def get_customer_id_by_sale_id(sale_id):
    """
    Reads the sales table with the help of the data_manager module.
    Returns the customer_id that belongs to the given sale_id
    or None if no such sale_id is in the table.

    Args:
         sale_id (str): sale id to search for
    Returns:
         str: customer_id that belongs to the given sale id
    """

    customer_id = []
    for items in table:
        if sale_id == items[0]:
            customer_id.append(items[6])
    return customer_id


def get_customer_id_by_sale_id_from_table(table, sale_id):
    """
    Returns the customer_id that belongs to the given sale_id
    or None if no such sale_id is in the table.

    Args:
        table: table to remove a record from
        sale_id (str): sale id to search for
    Returns:
        str: customer_id that belongs to the given sale id
    """

    customer_id = []
    for items in table:
        if sale_id == items[0]:
            customer_id.append(items[6])
    return customer_id


def get_all_customer_ids():
    """
    Reads the sales table with the help of the data_manager module.

    Returns:
         set of str: set of customer_ids that are present in the table
    """

    customer_id_table = []
    ID = 6

    for customer in table:
        customer_id_table.append(customer[ID])
    return customer_id_table


def get_all_customer_ids_from_table(table):
    """
    Returns a set of customer_ids that are present in the table.

    Args:
        table (list of list): the sales table
    Returns:
         set of str: set of customer_ids that are present in the table
    """


    customer_id_table = []
    ID = 6


    for customer in table:
        customer_id_table.append(customer[ID])
    return customer_id_table

def get_all_sales_ids_for_customer_ids():
    """
    Reads the customer-sales association table with the help of the data_manager module.
    Returns a dictionary of (customer_id, sale_ids) where:
        customer_id:
        sale_ids (list): all the sales belong to the given customer
    (one customer id belongs to only one tuple)

    Returns:
         (dict of (key, value): (customer_id, (list) sale_ids)) where the sale_ids list contains
            all the sales id belong to the given customer_id
    """

    dict_sale = {}
    ID_SALE = 0
    ID_CUSTOMER = 6



def get_all_sales_ids_for_customer_ids_from_table(table):
    """
    Returns a dictionary of (customer_id, sale_ids) where:
        customer_id:
        sale_ids (list): all the sales belong to the given customer
    (one customer id belongs to only one tuple)
    Args:
        table (list of list): the sales table
    Returns:
         (dict of (key, value): (customer_id, (list) sale_ids)) where the sale_ids list contains
         all the sales id belong to the given customer_id
    """

    dict_sale = {}
    ID_SALE = 0
    ID_CUSTOMER = 6


def get_add(list):
    sum = 0
    for items in list:
        sum += items
    return sum


def get_num_of_sales_per_customer_ids():
    """
     Reads the customer-sales association table with the help of the data_manager module.
     Returns a dictionary of (customer_id, num_of_sales) where:
        customer_id:
        num_of_sales (number): number of sales the customer made
     Returns:
         dict of (key, value): (customer_id (str), num_of_sales (number))
    """
    table = data_manager.get_table_from_file("sales/sales.csv")
    my_dict = {}
    for t in table:
        sum = 0
        if t[6] not in my_dict:
            my_dict.setdefault(t[6], []).append((sum+1))
        else:
            my_dict.setdefault(t[6], []).append((sum+1))
    result = {key: get_add(values) for key, values in my_dict.items()}
    return result
    


def get_num_of_sales_per_customer_ids_from_table(table):
    """
     Returns a dictionary of (customer_id, num_of_sales) where:
        customer_id:
        num_of_sales (number): number of sales the customer made
     Args:
        table (list of list): the sales table
     Returns:
         dict of (key, value): (customer_id (str), num_of_sales (number))
    """

    my_dict = {}
    for t in table:
        sum = 0
        if t[6] not in my_dict:
            my_dict.setdefault(t[6], []).append((sum+1))
        else:
            my_dict.setdefault(t[6], []).append((sum+1))
    result = {key: get_add(values) for key, values in my_dict.items()}
    return result
