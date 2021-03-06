"""
A set of functions for further use
"""
import os
import csv
import json


def get_route():
    """
    :return: a string with the root of the parent directory
    """
    # get the path of the current file
    here = os.path.dirname(os.path.realpath(__file__))
    # move one directory up
    root = os.path.dirname(here)
    return root


def get_csv(name):
    """
    :param name: the name of the csv file
    :return: Returns a dict with fields
    """
    root = get_route()
    # grab csv file path
    csv_path = os.path.join(root, name)

    # try to open csv and load it as a dict
    # if any error is encountered, raise an exception and stop the code
    try:
        file = open(csv_path, encoding='iso-8859-1')
        dict_reader = csv.DictReader(file)
        csv_data = list(dict_reader)
        return csv_data
    except FileNotFoundError:
        raise Exception('The file {0} was not found! Check the path and try again.').format(csv_path)
    except OSError:
        raise Exception('OS error occurred trying to open {0}').format(csv_path)


def get_json(name):
    """
    :param: name: the name of the JSON file
    :return: Returns a JSON object as a Python dictionary
    """
    root = get_route()
    # grab JSON file path
    json_path = os.path.join(root, name)

    # try to open JSON and load it as a dict
    # if any error is encountered, raise an exception and stop the code
    try:
        file = open(json_path, encoding='iso-8859-1')
        return json.load(file)
    except FileNotFoundError:
        raise Exception('The file {0} was not found! Check the path and try again.').format(json_path)
    except OSError:
        raise Exception('OS error occurred trying to open {0}').format(json_path)


def to_json(data, folder, name):
    """
    :param data: the dictionary to save as JSON
    :param folder: the folder where we save the JSON file
    :param name: the name of the JSON file
    :return:
    """
    if not os.path.exists(folder):
        os.makedirs(folder)

    filename = os.path.join(folder, name)
    with open(filename, 'w') as f:
        json.dump(data, f)


def find_value_by_key(list_of_dicts, find, default):
    """
    :param list_of_dicts: A list of dictionaries with fields [Country, Value]
    :param find: The value to find in Country field
    :param default: The default value to return if there is no match
    :return: Returns the value found in Value field (if any). Otherwise, returns default
    """
    i = 0
    while i < len(list_of_dicts):
        # loop through the list
        if list_of_dicts[i]['Country'] == find:
            print('{0} found! Assigning value of: {1}'.format(find, list_of_dicts[i]['Value']))
            return list_of_dicts[i]['Value']
        i += 1

    # if we are here, it means we could not find a country!
    print('{0} not found :( Assigning default: {1}'.format(find, default))
    return default
