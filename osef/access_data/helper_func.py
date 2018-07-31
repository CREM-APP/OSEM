import difflib
# a list of useful function

#TODO DevMaster: no need to call it helper_func.py, helper.py is sufficient so this file will have all the helper functions
def find_string(choice, options, cutoff=0.3):
    """
    This function find the closest match in a list of string and send warning of error if not found.

    :param choice: the string to match
    :param options: the list of options (in string)
    :return: the closest match or None if nothing is found
    """

    name_found = difflib.get_close_matches(choice, options, cutoff=cutoff)
    if len(name_found) > 1:
        pass
        # print('Warning: More than one option match the query. The chosen option is ' + name_found[0] + '.')
    elif len(name_found) == 0:
        print('Error: no match found')
        return None
    name_found = name_found[0]
    return name_found