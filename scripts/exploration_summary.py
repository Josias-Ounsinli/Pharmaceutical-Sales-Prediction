import sys
import os
import logging
import pandas as pd
import seaborn as sns

sns.set_style("darkgrid")

import warnings
warnings.filterwarnings("ignore")

sys.path.append(os.path.abspath(os.path.join("../scripts"))) 

from clean import dataCleaning

# Get url from DVC
import warnings

# import csv
import os
import sys
# from random import random, randint
import dvc.api
# import io

logging.basicConfig(level=logging.WARN)
logger = logging.getLogger(__name__)

warnings.filterwarnings("ignore")

data = pd.read_csv('data/train_dat.csv', sep=",")

data = dataCleaning(data).cleanStateHoliday()

data.reset_index(inplace=True)

print(data.head(), '\n')
print(data.columns, '\n')

correlation = data[['Sales', 'Customers']].corr()
print('Correlation coefficient between Sales and Customers: %s' % round(correlation['Sales']['Customers'], 2), '\n')


correlation2 = round(data[['Sales', 'CompetitionDistance', 'CompetitionOpenSinceMonth', 'CompetitionOpenSinceYear']].corr(), 3)

print('Correlation coefficient between Sales and CompetitionDistance: %s' % round(correlation2['Sales']['CompetitionDistance'], 2))
print('Correlation coefficient between Sales and CompetitionOpenSinceMonth: %s' % round(correlation2['Sales']['CompetitionOpenSinceMonth'], 2))
print('Correlation coefficient between Sales and CompetitionOpenSinceYear: %s' % round(correlation2['Sales']['CompetitionOpenSinceYear'], 2), '\n')


with open("./reports/explore.txt", "w") as file1:
    # Writing data to a file
    file1.write('Correlation coefficient between Sales and Customers: %s \n' % round(correlation['Sales']['Customers'], 2))
    file1.write('Correlation coefficient between Sales and CompetitionDistance: %s \n' % round(correlation2['Sales']['CompetitionDistance'], 2))
    file1.write("Correlation coefficient between Sales and CompetitionOpenSinceMonth: %s \n" % round(correlation2['Sales']['CompetitionOpenSinceMonth'], 2))
    file1.write("Correlation coefficient between Sales and CompetitionOpenSinceMonth: %s \n" % round(correlation2['Sales']['CompetitionOpenSinceYear'], 2))
