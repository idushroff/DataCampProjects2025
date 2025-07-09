"""Finding Exchange Rates for International Sales"""

"""
Query the VAT Comply rates API 'https://api.vatcomply.com/rates', using 
parameters to get the exchange rates for a base currency of 'USD' and the 
date of '2023-01-21'.
Using the orders DataFrame and the exchange rate from the API, calculate the 
total amount sold in USD, saving as a variable called total_usd_sales.
Ensure the final version of the orders DataFrame matches the requirements 
detailed in the Workbook.
*The VAT Comply rates API is free to use and doesn't require registration/
authentication.
"""

"""
![Header image](resources/image.jpg)

Exciting times! 

You've been running our very successful gadget webshop 'DataGadgets' for a few years and have recently expanded into 
new territories. While you've been focussed on the US market for the first five years of our existence, you now are 
shipping our cool data gadgets to the UK and Europe, too! But now our in-house built reporting has broken! 
Transactions don't only come in USD, but you're also receiving transactions in EUR and GPB. 

To better understand the volume of transactions being made, you should convert the non-USD transactions to USD and sum 
up the total. To do this, however, you'll need to use the proper exchange rates. 

In this project, you'll start with a CSV file containing all e-commerce transactions made on January 21st, but in their 
original currencies. Your job is to calculate the total sum in USD of all transactions so you know how much USD you 
sold on January 21st. To do this, you'll need to convert any non-USD transactions to USD using the exchange rate 
from January 21st, 2023. 

To get the exchange rates from January 21st, 2023, you'll rely on [VAT Comply rates API's]
(https://www.vatcomply.com/documentation#rates) public and free currency exchange API. You'll also use `pandas` to 
load the CSV file into a DataFrame and the `requests` package to make interacting with the API easier. 

You need to update the `orders` DataFrame so the final version has two new columns: `exchange_rate` and `amount_usd`. 
The final version should look as follows:

| `amount` | `currency` | `exchange_rate` | `amount_usd` |
|-|-|-|-|
| 43.75 | EUR | ... | ... |
| 385.5 | GBP | ... | ... |
| 495.5 | GBP | ... | ... |
| 117.99 | GBP | ... | ... |
| 624 | USD | ... | ... |
"""
'''
https://www.kaggle.com/code/abdelazizsami/project-finding-exchange-rates-for-international-s
https://www.kaggle.com/datasets/abdelazizsami/finding-exchange-rates-for-international-sales/data
'''

'''
Dataset Overview:
amount: This column contains the monetary values of the orders, ranging from 10.05 to 999.
currency: This column shows the currency in which the order was made, including GBP (British Pound), EUR (Euro), and USD (US Dollar).
'''


# Import required packages/libraries
import pandas as pd
import requests

# Read the CSV file into a DataFrame
orders = pd.read_csv('orders-2024-01-21.csv')
print(orders.head())

# Start coding here...

# Convert orders to a DataFrame (not strictly necessary here since it's already a DataFrame)
orders_df = pd.DataFrame(orders)

# Add placeholder columns for 'exchange_rate' and 'amount_usd'
# These will be populated after fetching the exchange rates from the API
orders_df['amount_usd'] = ''
orders_df['exchange_rate'] = ''

# Use the requests package to get the currency exchange rates and populate the exchange_rate column
# Define the URL and parameters for the VAT Comply API request
request_url = 'https://api.vatcomply.com/rates'
params = {
    'date' : '2023-01-21',
    'base': 'USD'
}

# Make a GET request to the API to retrieve exchange rates
response = requests.get(request_url, params=params)
rates = response.json()['rates']


# Use map() to match the currency in each row to its exchange rate from the 'rates' dict
# Since the base is USD, the rates represent how much 1 USD is in each foreign currency.
# We need the inverse to convert foreign currencies to USD.
orders_df['exchange_rate'] = orders_df['currency'].map(rates)

# Calculate sales in US dollars
orders_df['amount_usd'] = orders_df['amount'] * orders_df['exchange_rate']

# Find and print the total amount of sales in US dollars
total_usd_sales = orders_df['amount_usd'].sum()
print('total_usd_sales = ', total_usd_sales)

# Print the updated DataFrame to check the added columns and calculations
print(orders_df.head())

