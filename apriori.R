# Apriori

# Data Preprocessing
dataset = read.csv('Market_Basket_Optimisation.csv', header = FALSE)
#install.packages('arules')
library(arules)
dataset = read.transactions('Market_Basket_Optimisation.csv', sep = ',', rm.duplicates = TRUE)
summary(dataset)
itemFrequencyPlot(dataset, topN = 10)

# Training Apriori on the dataset
rules = apriori(dataset, parameter = list(support =3*7/7500, confidence =0.2))

# Visualising the results
inspect(sort(rules, by ='lift')[1:10])