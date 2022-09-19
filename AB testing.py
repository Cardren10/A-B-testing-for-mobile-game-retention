#Packages
import numpy as np
import pandas as pd
import seaborn as sns
from statsmodels.stats.proportion import proportions_ztest
import os

#Importing data
Cookie = pd.read_csv('cookie_cats.csv')

#Summary statistics for the cookies dataframe
Cookie.describe()

#count of players in the two groups
sns.catplot(data = Cookie, x= 'version', kind = 'count')

#Splitting our data into two groups
A = Cookie['version'] == 'gate_30'
Cookie_A = Cookie[A]
B = Cookie['version'] == 'gate_40'
Cookie_B = Cookie[B]

#bootstraped kde for 1-day and 7-day retention
bootstrap_7_A = []
bootstrap_7_B = []

for i in range(1000):   
    sample_A = Cookie_A.sample(n = 1000, replace = True)['retention_7'].mean()
    bootstrap_7_A.append(sample_A)
    sample_B = Cookie_B.sample(n = 1000, replace = True)['retention_7'].mean()
    bootstrap_7_B.append(sample_B)
    
sns.kdeplot(data = bootstrap_7_A)
sns.kdeplot(data = bootstrap_7_B)

#calculating the 1-day and 7-day retention rate for both groups
retention_A_1 = Cookie_A['retention_1'].sum() / Cookie_A['retention_1'].count()
retention_B_1 = Cookie_B['retention_1'].sum() / Cookie_B['retention_1'].count()

retention_A_7 = Cookie_A['retention_7'].sum() / Cookie_A['retention_7'].count()
retention_B_7 = Cookie_B['retention_7'].sum() / Cookie_B['retention_7'].count()


#Z-test for 1 day retention
count_1 = np.array([Cookie_A['retention_1'].sum(), Cookie_B['retention_1'].sum()])
nobs_1 = np.array([Cookie_A['retention_1'].count(), Cookie_B['retention_1'].count()])

proportions_ztest(count_1, nobs_1)

#Z-test for 7 day retention
count_7 = np.array([Cookie_A['retention_7'].sum(), Cookie_B['retention_7'].sum()])
nobs_7 = np.array([Cookie_A['retention_7'].count(), Cookie_B['retention_7'].count()])

proportions_ztest(count_7, nobs_7)
