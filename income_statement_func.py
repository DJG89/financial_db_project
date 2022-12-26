import requests
import pandas as pd
import json
import time
import sqlite3

from IPython.display import display
from tabulate import tabulate

def get_income_statement():
	# need the key to access the api
	api_key = ''
	api_key=open('my_api_key.txt', 'r').read()
	years = 30

	print("..getting data from web..")
	time.sleep(3)

	company = input("which company would you like data for: \n")

	response = requests.get(f"https://financialmodelingprep.com/api/v3/income-statement/{company}?limit={years}&apikey={api_key}")
	data = response.json()

	new_data= json.dumps(data)
	df=pd.read_json(new_data)
	print('..gathered data. printing to console..')
	time.sleep(3)

	my_list = ['symbol', 'calendarYear',
	'revenue', 'grossProfit', 'grossProfitRatio',
	'sellingGeneralAndAdministrativeExpenses', 'grossProfit',
	'operatingExpenses',
	'researchAndDevelopmentExpenses',
	'interestExpense', 'operatingIncome',
	'netIncome', 'eps'
	]

	income_statement_df = df[my_list]
	print(tabulate(income_statement_df, headers='keys', tablefmt = 'pretty'))
	print("done. data collected for you to view\n\n")

	message = '''
	do you want to commit this info
	to the database? y/n \n
	'''

	answer = input(message)

	if answer == 'y':
		# commit data to db
		conn = sqlite3.connect('finance_data.db')
		c = conn.cursor()
		income_statement_df.to_sql('Income_Statement', conn, if_exists='append', index = False)
