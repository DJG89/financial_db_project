import requests
import pandas as pd
import json

api_key = ''

api_key=open('my_api_key.txt', 'r').read()
company = "CPNG"

years = 2

response = requests.get(f"https://financialmodelingprep.com/api/v3/income-statement/{company}?limit={years}&apikey={api_key}")
with open('output.txt', 'w') as file:
	file.write(response.text)


data = response.json()

new_data= json.dumps(data)

df=pd.read_json(new_data)
print(df.head())

