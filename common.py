""" Common module
implement commonly used functions here
"""

import random
import string


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
