import streamlit as st
import pandas as pd
import sys
import os
import dvc.api
import io
import pickle
import plotly.express as px

sys.path.append(os.path.abspath(os.path.join("../dashbord/pages"))) 

path = 'data/test_data.csv'
repo = './'
version='vt.2.1'

data_url = dvc.api.get_url(
    path=path,
	repo=repo,
	rev=version
	)

test = pd.read_csv(data_url, sep=",")

test['StateHoliday'] = test['StateHoliday'].replace(0, '0')

def newfeatures(df): 
    df.set_index('Date', inplace=True)
    df['Year'] = df.index.year
    df['Month'] = df.index.month
    df['Day'] = df.index.day
    df['WeekOfYear'] = df.index.weekofyear

    df.reset_index(inplace=True)

    df['BeginMonth'] = (((df['Day'])//7) == 0)*1
    df['MidMonth'] = (((df['Day'])//10) == 1)*1
    df['EndMonth'] = (((df['Day'])//7) >= 3)*1

    
    df.drop(['Date', 'Store'], axis=1)

    return df

XGBModel = pickle.load(open('09-09-2022-17-58-55-00-XGB.pkl', 'rb'))
CatBoostModel = pickle.load(open('09-09-2022-18-03-50-00-CatBoost.pkl', 'rb'))
RandomForest = pickle.load(open('09-09-2022-14-44-50-00-RandomForest.pkl', 'rb'))

st.set_page_config(page_title="Sales Predictions", layout="wide")

st.markdown("# Sales Predictions ❄️")
st.sidebar.markdown("# Sales Predictions ❄️")

st.title('Predictions of Sales for stores') 
tickers = list(test['StoreType'].unique())
dropdown = st.multiselect('Pick your store type', tickers)

if len(dropdown) == 1:

    tickerss = list(test[test['StoreType'] == dropdown[0]]['Store'].unique())
    dropdowns = st.multiselect('Pick your store', tickerss)
    
    if len(dropdowns) == 1:
        df = test[test['Store'] == int(dropdowns[0])]
        df['Date'] = list(pd.date_range(start="2015-08-01", periods=len(df)))
        
        df_pred = newfeatures(df)
        
        df['XGBpred'] = XGBModel.predict(df_pred)
        df['CBpred'] = CatBoostModel.predict(df_pred)
        df['RFpred'] = RandomForest.predict(df_pred)
        
        fig = px.line(df, x='Date', y=df.columns[27:30])
        
        st.plotly_chart(fig, use_container_width=True)
    
    else:
        st.write('Choose only one store')

else:
    st.write('Choose only one store type')





