import streamlit as st
import pandas as pd
import cbsodata
from streamlit_echarts import st_echarts
import json


# Retrieve data from CBS
@st.cache
def retreive_data_cbs():
    df = pd.DataFrame(cbsodata.get_data('83625ENG'))
    return df


df = retreive_data_cbs()

# print(df.info())

# Create Dimensions
regions = df['Regions'].unique().tolist()
periods = df['Periods'].unique().tolist()


# Create app layout
sidebar_title = st.sidebar.subheader("Compare house prices in the Netherlands")

sidebar_text = st.sidebar.write(('''
Compare Dutch house prices per country region (LD), province (PV) or municipality/city over the year 1995 until 2020.
 
[Sourcecode](https://github.com/mvs12/cbs-houseprices-streamlit)
 '''))

region_1 = st.sidebar.selectbox("Select first region", (regions))
region_2 = st.sidebar.selectbox("Select second region", (regions))

sidebar_text = st.sidebar.write(('''
[Sourcecode](https://github.com/mvs12/cbs-houseprices-streamlit)
 '''))

# Create callbacks/filter data on selection
periods_filter = periods
values_region_1 = df['AveragePurchasePrice_1'][df['Regions'] == region_1].tolist()
values_region_2 = df['AveragePurchasePrice_1'][df['Regions'] == region_2].tolist()


# Create line chart with theme
st.title(region_1 + " and " + region_2)

# Open theme
with open('theme.json') as file:
    theme = json.load(file)

options = {
    "xAxis": {
        "type": "category",
        "data": periods_filter,
        "name": "Year",
    },
    "yAxis": {"type": "value", "name": "House Prices in EUR"},
    "series": [
        {"data": values_region_1, "type": "line", "name": region_1, "areaStyle": {}},
        {"data": values_region_2, "type": "line", "name": region_2, "areaStyle": {}}
    ],
    "legend": {"display": "true"}
}

st_echarts(options=options, height="400px", theme=theme,)

st.write("Source: [CBS Open data StatLine 'Existing own homes; prices, region 1995-2020'](https://opendata.cbs.nl/statline/portal.html?_la=en&_catalog=CBS&tableId=83625ENG&_theme=1102)")
