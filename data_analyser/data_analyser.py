"""
This module creates reports for the marketing department.
This module can run independently from other modules.
Has no own data structure but uses other modules.
Avoid using the database (ie. .csv files) of other modules directly.
Use the functions of the modules instead.
"""

# todo: importing everything you need

# importing everything you need
import ui
import common
from sales import sales
from crm import crm
import ui
# data manager module
import data_manager
# common module
import common
file_name = "crm/customers.csv"
table = data_manager.get_table_from_file(file_name)
title_list = ["ID", "Name", "Email", "Subscribed"]


def start_module():
    """
    Starts this module and displays its menu.
     * User can access default special features from here.
     * User can go back to main menu from here.

    Returns:
        None
    """
    while True:
        # List of available option
        list_options = ['get_the_last_buyer_name',
                        'get_the_last_buyer_id',
                        'Remove employee',
                        'Update employee',
                        'Get oldest employee',
                        'Get employee with age closest to average']
        # printing menu
        ui.print_menu("Human resources manager", list_options, "(0) Main menu")
        # Dict of available option to start equal function
        dic_function = {'1': get_the_last_buyer_name,
                        '2': get_the_last_buyer_id,
                        '3': print('nie zrobione'),
                        '4': print('nie zrobione'),
                        '5': print('nie zrobione'),
                        '6': print('nie zrobione'),
                        '0': exit}
        # Start option
        common.choose_by_dic(dic_function, table)
    # your code
    # your code

    pass


def get_the_last_buyer_name():
    """
    Returns the customer _name_ of the customer made sale last.

    Returns:
        str: Customer name of the last buyer
    """

    # your code


def get_the_last_buyer_id(table):
    print('udalo sie')
    """
    Returns the customer _id_ of the customer made sale last.

    Returns:
        str: Customer id of the last buyer
    """

    # your code


def get_the_buyer_name_spent_most_and_the_money_spent():
    """
    Returns the customer's _name_ who spent the most in sum and the money (s)he spent.

    Returns:
        tuple: Tuple of customer name and the sum the customer spent eg.: ('Daniele Coach', 42)
    """

    biggest_spender_id, most_money_spent = get_the_buyer_id_spent_most_and_the_money_spent()
    biggest_spender_name = crm.get_name_by_id(biggest_spender_id)
    return biggest_spender_name


def get_the_buyer_id_spent_most_and_the_money_spent():
    """
    Returns the customer's _id_ who spent more in sum and the money (s)he spent.

    Returns:
        tuple: Tuple of customer id and the sum the customer spent eg.: (aH34Jq#&, 42)
    """

    customer_ids = sales.get_all_customer_ids()
    sales_for_customer_dict = sales.get_all_sales_ids_for_customer_ids()
    most_money_spent = 0
    for customer_id in customer_ids:
        sum_of_prices = get_the_sum_of_prices(sales_for_customer_dict[customer_id])
        if sum_of_prices > most_money_spent:
            most_money_spent = sum_of_prices
            biggest_spender_id = customer_id
    return (biggest_spender_id, most_money_spent)


def get_the_most_frequent_buyers_names(num=1):
    """
    Returns 'num' number of buyers (more precisely: the customer's name) who bought most frequently in an
    ordered list of tuples of customer names and the number of their sales.

    Args:
        num: the number of the customers to return.

    Returns:
        list of tuples: Ordered list of tuples of customer names and num of sales
            The first one bought the most frequent. eg.: [('Genoveva Dingess', 8), ('Missy Stoney', 3)]
    """

    # your code


def get_the_most_frequent_buyers_ids(num=1):
    """
    Returns 'num' number of buyers (more precisely: the customer ids of them) who bought more frequent in an
    ordered list of tuples of customer id and the number their sales.

    Args:
        num: the number of the customers to return.

    Returns:
        list of tuples: Ordered list of tuples of customer ids and num of sales
            The first one bought the most frequent. eg.: [(aH34Jq#&, 8), (bH34Jq#&, 3)]
    """

    # your code
