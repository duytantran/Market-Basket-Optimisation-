# Apriori

# Importing the libraries
import numpy as np
import matplotlib as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Market_Basket_Optimisation.csv', header = None)

# The dataset is given as dataframe, Apriori requires a list in a list
transactions = []
for i in range(0, 7501):
    transactions.append([str(dataset.values[i, j]) for j in range(0,20)])

# Training Apriori on the dataset
from apyori import apriori
rules = apriori(transactions,min_support = 3*7/7500 
                , min_confidence = 0.2
                , min_lift = 3
                , min_length = 2)

# Visualising the results
results = list(rules)
clean_results = []
for i in range (0, len(results)):
    clean_results.append('RULLE:\t' + str(results[i][0]) + 
                         '\nSUPPORT:\t' + str(results[i][1])
                         + '\nCONFIDENCE:\t' + str(results[i][2][0][2])
                         + '\nLIFT:\t'+ str(results[i][2][0][3]))
    
    