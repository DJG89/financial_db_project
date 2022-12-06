import requests
import pandas as pd
import json
import time
import sqlite3
from balance_sheet_func import *
from income_statement_func import *
from get_company_profile_func import *


while True:
	# initial input from user
	initial_message = '''which data are you trying to retrieve? \n
	b/i/c - balance sheet, income statement, or company profile?\n
	or..enter 'q' to quit\n'''

	initial_input = input(initial_message)

	if initial_input == 'b':
		get_balance_sheet()
		continue

	elif initial_input == 'i':
		get_income_statement()
		continue

	elif initial_input == 'c':
		get_company_profile()
		continue

	elif initial_input == 'q':
		break

	else:
		print('incorrect input. try again')
		continue
