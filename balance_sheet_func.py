import requests
import pandas as pd
import json
import time
import sqlite3

from IPython.display import display
from tabulate import tabulate

def get_balance_sheet():
	# need the key to access the api
	api_key = ''
	api_key=open('my_api_key.txt', 'r').read()
	
	years = 30
	company = input('input company in all caps:\n')
	
	print("getting data from web..please wait")
	time.sleep(3)

	# link to balance sheet api
	response = requests.get(f"https://financialmodelingprep.com/api/v3/balance-sheet-statement/{company}?apikey={api_key}&limit=120")
	data = response.json()

	new_data= json.dumps(data)
	df=pd.read_json(new_data)

	print("displaying data momentarily..")
	time.sleep(3)
	
	print(tabulate(df, headers='keys', tablefmt = 'pretty'))
	print("done. data collected for you to view\n\n")