# Market-Basket-Optimisation-
Given a dataset of different market baskets from different customers, optimise the market basket using the association rule learning: apriori. 
The support is defined as a product bought at least 3 times in a week over 7500 transactions.
Coded in both Python and R.

# Using Eclat
Of course, we can use a simpler association rule learning such as Eclat. In R file:
* Change the apriori function with eclat, remove confidence parameter, add minlen
* In the inspect function, change 'lift' with 'support'
