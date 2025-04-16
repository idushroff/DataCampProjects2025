""" Will this customer purchase your product? """

"""
The marketing team asked you to analyze the behavior of online customers 
during November and December, the busiest months for shoppers.

1. What are the purchase rates for online shopping sessions by customer type
for November and December? Store the result in a dictionary called purchase_rates
in the format below using the exact names for keys. 

purchase_rates = {"Returning_Customer": 0.254, "New_Customer": 0.276}

2. What is the strongest correlation in total time spent among page types 
by returning customers in November and December? Store the result in a 
dictionary called top_correlation in the format below using the exact names 
for keys.

top_correlation = {"pair": (x_duration, y_duration), "correlation": 0.345}

3. A new campaign for the returning customers will boost the purchase rate 
by 15%. What is the likelihood of achieving at least 100 sales out of 500 
online shopping sessions for the returning customers? Store the result in 
a variable called prob_at_least_100_sales. Optional: plot a binomial 
probability distribution chart to visualize your chances.
"""

"""
Online shopping decisions rely on how consumers engage with online store content. You work for a new startup company that has just launched a new online shopping website. The marketing team asks you, a new data scientist, to review a dataset of online shoppers' purchasing intentions gathered over the last year. Specifically, the team wants you to generate some insights into customer browsing behaviors in November and December, the busiest months for shoppers. You have decided to identify two groups of customers: those with a low purchase rate and returning customers. After identifying these groups, you want to determine the probability that any of these customers will make a purchase in a new marketing campaign to help gauge potential success for next year's sales.

### Data description:

You are given an `online_shopping_session_data.csv` that contains several columns about each shopping session. Each shopping session corresponded to a single user. 

|Column|Description|
|--------|-----------|
|`SessionID`|unique session ID|
|`Administrative`|number of pages visited related to the customer account|
|`Administrative_Duration`|total amount of time spent (in seconds) on administrative pages|
|`Informational`|number of pages visited related to the website and the company|
|`Informational_Duration`|total amount of time spent (in seconds) on informational pages|
|`ProductRelated`|number of pages visited related to available products|
|`ProductRelated_Duration`|total amount of time spent (in seconds) on product-related pages|
|`BounceRates`|average bounce rate of pages visited by the customer|
|`ExitRates`|average exit rate of pages visited by the customer|
|`PageValues`|average page value of pages visited by the customer|
|`SpecialDay`|closeness of the site visiting time to a specific special day|
|`Weekend`|indicator whether the session is on a weekend|
|`Month`|month of the session date|
|`CustomerType`|customer type|
|`Purchase`|class label whether the customer make a purchase|
"""

"""
# Import required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Load and view your data
shopping_data = pd.read_csv("online_shopping_session_data.csv")
shopping_data.head()
"""

# Start your code here!
# Use as many cells as you like