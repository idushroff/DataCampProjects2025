"""Finding Exchange Rates for International Sales"""

"""
Query the VAT Comply rates API 'https://api.vatcomply.com/rates', using 
parameters to get the exchange rates for a base currency of 'USD' and the 
date of '2024-01-21'.
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

You've been running our very successful gadget webshop 'DataGadgets' for a few years and have recently expanded into new territories. While you've been focussed on the US market for the first five years of our existence, you now are shipping our cool data gadgets to the UK and Europe, too! But now our in-house built reporting has broken! Transactions don't only come in USD, but you're also receiving transactions in EUR and GPB. 

To better understand the volume of transactions being made, you should convert the non-USD transactions to USD and sum up the total. To do this, however, you'll need to use the proper exchange rates. 

In this project, you'll start with a CSV file containing all e-commerce transactions made on January 21st, but in their original currencies. Your job is to calculate the total sum in USD of all transactions so you know how much USD you sold on January 21st. To do this, you'll need to convert any non-USD transactions to USD using the exchange rate from January 21st, 2024. 

To get the exchange rates from January 21st, 2024, you'll rely on [VAT Comply rates API's](https://www.vatcomply.com/documentation#rates) public and free currency exchange API. You'll also use `pandas` to load the CSV file into a DataFrame and the `requests` package to make interacting with the API easier. 

You need to update the `orders` DataFrame so the final version has two new columns: `exchange_rate` and `amount_usd`. The final version should look as follows:

| `amount` | `currency` | `exchange_rate` | `amount_usd` |
|-|-|-|-|
| 43.75 | EUR | ... | ... |
| 385.5 | GBP | ... | ... |
| 495.5 | GBP | ... | ... |
| 117.99 | GBP | ... | ... |
| 624 | USD | ... | ... |
"""

# Import required packages/libraries
import pandas as pd
import requests

# Read the CSV file into a DataFrame
orders = pd.read_csv('data/orders-2024-01-21.csv')
orders.head()

# Start coding here...
