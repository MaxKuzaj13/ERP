""" Common module
implement commonly used functions here
"""

import random
import string
import ui
import main


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

    Lletters = string.ascii_lowercase
    Uletters = string.ascii_uppercase
    Specials = ["#", "$", "%", "&", "?", "@"]
    Numbers = string.digits
    generated = random.choice(Lletters) + random.choice(Uletters) + random.choice(Numbers) + random.choice(Numbers) + random.choice(Uletters)+ random.choice(Lletters) + random.choice(Specials) + random.choice(Specials)

    return generated

def choose_by_dic(dic_function, table, *args):
    inputs = ui.get_inputs(["Choose option: "], " ")
    option = inputs[0]
    exit_code = 0
    if option == "1":
        dic_function["1"](table)
        print('tap 1')
    elif option == "2":
        dic_function["2"](table)
        print('tap 2')
        #hr.start_module()
    elif option == "3":
        print('tap 3')
        id_ = ui.get_inputs(["Which ID do you want to remove? "],"")
        dic_function["3"](table, id_)
        #inventory.start_module()
    elif option == "4":
        print('tap 4')
        #accounting.start_module()
    elif option == "5":
        print('tap 5')
        #sales.start_module()
    elif option == "6":
        print('tap 6')
        #crm.start_module()
    elif option == "0":
        main.main()
        #sys.exit(0)
    else:
        raise KeyError("There is no such option.")

    return exit_code


def add_universal(table, title_list):
    new_record = []
    add_index_start_for_name_rows = 1
    list_labels = title_list[add_index_start_for_name_rows:]
    id_record = generate_random(table)
    inputs_list = ui.get_inputs(list_labels, "")
    # Add input to list with nessery attributes
    # Add new ID - random
    new_record.append(id_record)
    # Iteration by rows
    for row in inputs_list:
        new_record.append(row)
    # Append new row to the table.
    table.append(new_record)

    return table

def ID_error():
    ui.print_result("ID Error: ", "The ID doesn't exist.")