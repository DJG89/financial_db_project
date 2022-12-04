import requests
import pandas as pd
import json
import time
import sqlite3

from IPython.display import display
from tabulate import tabulate


def get_company_profile():
	# need the key to access the api
	api_key = ''
	api_key=open('my_api_key.txt', 'r').read()

	company = input('input company in all caps:\n')
	print("getting data from web..please wait")
	time.sleep(3)

	# link to company profile api
	response = requests.get(f"https://financialmodelingprep.com/api/v3/profile/{company}?apikey={api_key}")
	data = response.json()
	new_data= json.dumps(data)

	df=pd.read_json(new_data)
	desired_columns = ['symbol', 'companyName', 'sector', 'industry', 'country']

	final_df = df[desired_columns]

	print("finishing..")
	time.sleep(3)

	print(tabulate(final_df, headers='keys', tablefmt = 'pretty'))
	print("done. data collected for you to view\n\n")