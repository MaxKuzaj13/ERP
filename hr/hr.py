""" Human resources module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * name (string)
    * birth_year (number)
"""

# everything you'll need is imported:
# User interface module
import ui
# data manager module
import data_manager
# common module
import common
file_name = "hr/persons.csv"
table = data_manager.get_table_from_file(file_name)

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
        list_options = ['Show list of employees',
                        'Add new employee',
                        'Remove employee',
                        'Update employee',
                        'Get oldest employee',
                        'Get employee with age closest to average']
        # printing menu
        ui.print_menu("Human resources manager", list_options, "(0) Main menu")
        # Dict of available option to start equal function
        dic_function = {'1': show_table,
                        '2': add,
                        '3': remove,
                        '4': update,
                        '5': get_oldest_person,
                        '6': get_persons_closest_to_average,
                        '0': exit}
        # Start option
        common.choose_by_dic(dic_function, table)
    # your code


def show_table(table):
    """
    Display a table

    Args:
        table (list): list of lists to be displayed.

    Returns:
        None
    """

    title_list = ['ID', 'Name', 'Year of birth']
    ui.print_table(table, ('ID', 'Name', 'Year of birth'))


def add(table):
    """
    Asks user for input and adds it into the table.

    Args:
        table (list): table to add new record to

    Returns:
        list: Table with a new record
    """

    global file_name

    employee_id = generate_random(table)
    employee_name = input('Enter the new employee\'s full name: ')
    employee_year = input('Enter the new employee\'s year of birth: ')
    table.append([employee_id, employee_name, employee_year])

    write_table_to_file(file_name, table)

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

    # your code

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

    return table


# special functions:
# ------------------

def get_oldest_person(table):
    """
    Question: Who is the oldest person?

    Args:
        table (list): data table to work on

    Returns:
        list: A list of strings (name or names if there are two more with the same value)
    """

    # your code


def get_persons_closest_to_average(table):
    """
    Question: Who is the closest to the average age?

    Args:
        table (list): data table to work on

    Returns:
        list: list of strings (name or names if there are two more with the same value)
    """

    # your code
