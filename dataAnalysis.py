# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 14:59:28 2020

@author: akashweb
"""

#importing required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
 
 
#getting along with datasets
covidDatasets = pd.read_csv('covid19_Confirmed_dataset.csv')


#getting covid datasets head
covidDatasets.head(10)


#getting the shape i.e. no of rows and coloumns
covidDatasets.shape


#cleaning dataset inplace
covidDatasets.drop(['Lat','Long'], axis=1, inplace = True)
covidDatasets.head()
aggregatedDf = covidDatasets.groupby('Country/Region').sum()
aggregatedDf.head()


#various ways of plotting data
aggregatedDf.loc['China'].plot()
aggregatedDf.loc['India'].plot()
plt.legend()
plt.title('sample data from china and india')

#first 3day data
aggregatedDf.loc['China'][:3].plot()
aggregatedDf.loc['India'][:3].plot()
plt.title('first 3 days data')
plt.lengend()

#plotting the first derivative i.e. new cases each day
aggregatedDf.loc['China'].diff().plot()
aggregatedDf.loc['India'].diff().plot()
plt.title('sample differential plot - showing new cases each day')
plt.legend()


#finding ma infection rate
print('Sample data on new infection rates!')
print('Max infection rate in China:',aggregatedDf.loc['China'].diff().max())
print('Max infection rate in India:',aggregatedDf.loc['India'].diff().max())


#getting all infection rates
countries = list(aggregatedDf.index)
maxInfectionRates = []
for c in countries:
    maxInfectionRates.append(aggregatedDf.loc[c].diff().max())
aggregatedDf['Max Infection Rates'] = maxInfectionRates
aggregatedDf.head()


#getting cleaned Data
cleanedCovidData = pd.DataFrame(aggregatedDf['Max Infection Rates'])


#getting world happiness report
worldHappinessReport = pd.read_csv('worldwide_happiness_report.csv')
worldHappinessReport.head()

#cleaning the second data
worldHappinessReport.drop(['Overall rank','Score','Generosity','Perceptions of corruption'], axis = 1, inplace = True)
worldHappinessReport.head()
worldHappinessReport.set_index('Country or region', inplace = True)


#joining datasets
cleanedFinalData = cleanedCovidData.join(worldHappinessReport, how = "inner")


#getting the correlation matrix
corrMatrix = cleanedFinalData.corr()

#visualising data
x = cleanedFinalData['GDP per capita']
y = cleanedFinalData['Max Infection Rates']
sns.scatterplot(x,y)
plt.title('GDP vs Infection Rates')


#log scale
sns.scatterplot(x, np.log(y))
plt.title('GDP vs Infection Rates(Log Scale)')


#Reg plot
sns.regplot(x, np.log(y))
plt.title('GDP vs Infection Rates(Reg plot)')


#visualising another data
x = cleanedFinalData['Healthy life expectancy']
y = cleanedFinalData['Max Infection Rates']
sns.scatterplot(x,y)
plt.title('Healthy Life Expectancy vs Infection Rates')


#log scale
sns.scatterplot(x, np.log(y))
plt.title('Healthy Life Expectancy vs Infection Rates(Log Scale)')


#Reg plot
sns.regplot(x, np.log(y))
plt.title('Healthy Life Expectancy vs Infection Rates(Reg plot)')






