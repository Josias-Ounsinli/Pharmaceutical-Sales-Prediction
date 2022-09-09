import sys
import os
import logging
import pandas as pd
import seaborn as sns

import mlflow

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
import io

logging.basicConfig(level=logging.WARN)
logger = logging.getLogger(__name__)


path = 'data/train_data.csv'
repo = './'
version='v1.1'

content =dvc.api.read(path=path, repo=repo, rev=version)

data_url = dvc.api.get_url(
    path=path,
	repo=repo,
	rev=version
	)
    
mlflow.set_experiment('mlops-work')

warnings.filterwarnings("ignore")

data = pd.read_csv(data_url, sep=",")
# data = pd.read_csv(io.StringIO(content), sep=",")

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

with mlflow.start_run():
    # Log data params
    mlflow.log_param("data_url", data_url)
    mlflow.log_param("data_version", version)
    mlflow.log_param("data_rows", data.shape[0])
    mlflow.log_param("data_cols", data.shape[1])
    


