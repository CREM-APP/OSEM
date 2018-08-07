import difflib


def find_string(choice, options, cutoff=0.3):
    """
    This function find the closest match in a list of string and send warning of error if not found.

    :param choice: the string to match
    :param options: the list of options (in string)
    :param cutoff: float, a number between one and 0, if one the string must match perfectly the options, if 0 all pass
    :return: the closest match or None if nothing is found
    """
    name_found = difflib.get_close_matches(choice, options, cutoff=cutoff)

    if len(name_found) == 0:
        raise ValueError("No match found for {}".format(choice))

    name_found = name_found[0]
    return name_found
