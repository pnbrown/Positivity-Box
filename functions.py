import pandas as pd
from urllib.request import urlopen as urlo
from configparser import ConfigParser
import json


def set_initial_state():
    pd.set_option('display.max_colwidth', 1000)
    config = ConfigParser()
    config.read('config.txt')
    api_key = config.get('auth', 'api_key')
    form_id = config.get('auth', 'form_id')
    constants = [form_id, api_key]
    return constants


def fill_dictionary_from_csv():
    """Brings in our locally saved .csv from Typeform and populates a list with the data from it."""
    df = pd.read_csv("Motivate!!-report.csv",
                     names=['#',
                            "Please add something motivational in the box. And please don't be a dick. We're trying "
                            "to do something nice for someone here.",
                            "Start Date (UTC)", "Submit Date (UTC)", "Network ID"], encoding="utf-8-sig")
    useful_data = df["Please add something motivational in the box. And please don't be a dick. We're trying to do "
                     "something nice for someone here."]
    data_as_array = useful_data.as_matrix()
    return data_as_array


def fill_dictionary_from_api(form_id, api_key):
    """Brings in results from Typeform and populates a list with the data from it. Takes in two strings for the api key
    and the form id and returns http object"""
    form_url = 'https://api.typeform.com/v1/form/' + form_id + '?key=' + api_key
    data = urlo(form_url).read().decode('UTF-8')
    return data


def parse_data(raw_data):
    """Turns the data from the http object to an array just containing our quotes"""
    parsed = json.loads(raw_data)
    desired_data = parsed['responses']
    quotes_array = []
    for item in desired_data:
        matches = item.get('answers')
        quote = matches.get('textarea_65071942')
        if str(type(quote)) == "<class 'str'>":
            quotes_array.append(quote)
    return quotes_array


def print_quote(quotes, quotes_entry):
    """Returns a quote from our list."""
    quote = quotes[quotes_entry].strip('\'')
    quotes_entry += 1
    values = [quote, quotes_entry]
    return values


def yes_or_no():
    """Asks a user to choose yes or no. Mostly error handling. Returns boolean."""
    response = input("Please enter y or n. ")
    invalid_response = True
    while invalid_response:
        if response == 'y':
            invalid_response = False
        elif response == 'Y':
            invalid_response = False
        elif response == 'n':
            invalid_response = False
        elif response == 'N':
            invalid_response = False
        else:
            print("You have entered an invalid response.")
    if response == 'y':
        return True
    elif response == 'Y':
        return True
    else:
        return False

def program_run():
    # Set initial values
    constants = set_initial_state()
    # print(constants)
    quotes_entry = 0
    run_program = True
    see_quote = False

    # Bring in data
    raw_data = fill_dictionary_from_api(constants[0], constants[1])
    # print(raw_data)

    # Parse data
    quotes = parse_data(raw_data)
    return quotes


    # # Offer quotes
    # while run_program:
    #     print("Would you like to see a quote? ")
    #     see_quote = yes_or_no()
    #
    #     if see_quote:
    #         quotes_entry = print_quote(quotes, quotes_entry)
    #
    #     print("Would you like to exit the program? ")
    #     run_program = bool(not (yes_or_no()))