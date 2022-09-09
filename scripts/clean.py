import pandas as pd
import numpy as np
import logging

logging.basicConfig(filename='./general_logfile.log', filemode='a',
                    encoding='utf-8', level=logging.DEBUG)


class dataCleaning:
    ###############################################################################
    # data cleaning
    ################################################################################

    def __init__(self, df: pd.DataFrame):
        """
            Returns a dataframe Info Object with the passed DataFrame Data
            Parameters
        """
        self.df = df

    def dateformat(self, column):
        self.df[column] = pd.to_datetime(self.df[column])
        return self.df

    def removeClosedStores(self):
        """
            Closed stores and days which didn't have any sales won't be counted into the forecasts.
        """

        self.df = self.df[(self.df['Open'] == 1) & (self.df['Sales'] != 0)]
        return self.df

    def cleanStateHoliday(self):
        self.df['StateHoliday'] = self.df['StateHoliday'].replace('0', 0)
        return self.df

    def cleanStateHoliday2(self):
        self.df['StateHoliday'] = self.df['StateHoliday'].replace(0, '0')
        return self.df
