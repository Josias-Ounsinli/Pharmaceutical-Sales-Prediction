import streamlit as st
import pandas as pd
import sys
import os
import dvc.api
import io
import pickle
import plotly.express as px
import seaborn as sns

sys.path.append(os.path.abspath(os.path.join("../dashbord/pages"))) 

path = 'data/train_data.csv'
repo = './'
version='v2.1'

data_url = dvc.api.get_url(
    path=path,
	repo=repo,
	rev=version
	)

test = pd.read_csv(data_url, sep=",")

test['StateHoliday'] = test['StateHoliday'].replace(0, '0')

st.set_page_config(page_title="Sales exploration", layout="wide")

st.markdown("# Sales exploration 🎉")
st.sidebar.markdown("# Sales exploration 🎉")

st.title('Exploration of Sales for stores') 
tickers = list(test['StoreType'].unique())
dropdown = st.multiselect('Pick your store type', tickers)

def factorplot(df: pd.DataFrame, x, y, col, hue, row):
    fig = sns.factorplot(data = df, x = x, y = y, col = col, palette = 'plasma', hue = hue, row = row)
    st.pyplot(fig)


if len(dropdown) == 1:

    tickerss = list(test[test['StoreType'] == dropdown[0]]['Store'].unique())
    dropdowns = st.multiselect('Pick your store', tickerss)
    
    if len(dropdowns) == 1:
        df = test[test['Store'] == int(dropdowns[0])]
        
        fig = px.line(df, x='Date', y='Sales', title='Sales general trends')
        fig.update_xaxes(rangeslider_visible=True,
         rangeselector=dict(buttons=list([
            dict(count=1, label="1y", step="year", stepmode="backward"),
            dict(count=2, label="2y", step="year", stepmode="backward"),
            dict(step="all")
        ])))
        
        st.plotly_chart(fig, use_container_width=True)

        st.markdown("<p style='padding:10px; background-color:#000000;color:#00ECB9;font-size:16px;border-radius:10px;'>Section Break</p>", unsafe_allow_html=True)
        st.title('Sales per year')
        factorplot(df, 'Month', 'Sales', 'Year', 'Year', None)
        
        st.markdown("<p style='padding:10px; background-color:#000000;color:#00ECB9;font-size:16px;border-radius:10px;'>Section Break</p>", unsafe_allow_html=True)
        st.title('Sales per year and schoolholiday')
        factorplot(df, 'Month', 'Sales', 'Year', 'Year', 'SchoolHoliday')

        st.markdown("<p style='padding:10px; background-color:#000000;color:#00ECB9;font-size:16px;border-radius:10px;'>Section Break</p>", unsafe_allow_html=True)
        st.title('Sales per day of the week')
        factorplot(df, 'Month', 'Sales', 'DayOfWeek', 'DayOfWeek', None)

        st.markdown("<p style='padding:10px; background-color:#000000;color:#00ECB9;font-size:16px;border-radius:10px;'>Section Break</p>", unsafe_allow_html=True)
        st.title('Sales per Promo')
        factorplot(df, 'Month', 'Sales', 'Promo', 'Promo', None)

        st.markdown("<p style='padding:10px; background-color:#000000;color:#00ECB9;font-size:16px;border-radius:10px;'>Section Break</p>", unsafe_allow_html=True)


    
    else:
        st.write('Choose only one store')

else:
    st.write('Choose only one store type')





