""" Common module
implement commonly used functions here
"""

import random
import ui


def generate_random(table):
    """
    Generates random and unique string. Used for id/key generation:
         - at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letter
         - it must be unique in the table (first value in every row is the id)

    Args:
        table (list): Data table to work on. First columns containing the keys.

    Returns:
        string: Random and unique string
    """

    generated = ''

    # your code

    return generated

def choose_by_dic(dic_function, table, *args):
    inputs = ui.get_inputs(["chouse option: "], " ")
    option = inputs[0]
    if option == "1":
        dic_function["1"](table)
        print('tap 1')
    elif option == "2":
        print('tap 1')
        #hr.start_module()
    elif option == "3":
        print('tap 1')
        #inventory.start_module()
    elif option == "4":
        print('tap 1')
        #accounting.start_module()
    elif option == "5":
        print('tap 1')
        #sales.start_module()
    elif option == "6":
        print('tap 1')
        #crm.start_module()
    elif option == "0":
        print('tap 2')
        #sys.exit(0)
    else:
        raise KeyError("There is no such option.")
