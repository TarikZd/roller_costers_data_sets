# Importing Toolkit

import numpy as np
import pandas as pd
import seaborn as sns
import streamlit as st
import plotly.express as px
import matplotlib.pylab as plt

# Loading Data

df = pd.read_csv('coaster_db.csv')

# Page Settings

plt.style.use('ggplot')

st.set_page_config( page_title = "Tips Dashbord", 
                     page_icon=None, 
                     layout="wide", 
                     initial_sidebar_state="auto" )



# Preparing data

df = df[['coaster_name', # 'Length', 'Speed', 
         'Location',     # 'Status', 'Opening date', 'Type','Manufacturer', 'Height restriction',
                         # 'Model', 'Height','Inversions', 'Lift/launch system', 'Cost', 'Trains',  'Park section',
                         # 'Duration', 'Capacity', 'G-force', 'Designer', 
         'Max vertical angle', # 'Drop', 'Soft opening date', 'Fast Lane available', 'Replaced', 'Track layout',
                         # 'Fastrack available', 'Soft opening date.1', 'Closing date', 'Opened', 'Replaced by', 'Website',
                         # 'Flash Pass Available', 'Must transfer from wheelchair', 'Theme', 'Single rider line available',
                         # 'Restraint Style', 'Flash Pass available', 
         'Acceleration', # 'Restraints', 'Name',
         'year_introduced', #'latitude', 'longitude', 
         'Type_Main', 'opening_date_clean', # 'speed1', 'speed2', 'speed1_value', 'speed1_unit',
         'speed_mph', # 'height_value', 'height_unit',
         'height_ft', 'Inversions_clean', 'Gforce_clean']].copy()

df['opening_date_clean'] = pd.to_datetime(df['opening_date_clean'])

df = df.rename(columns = {'coaster_name' : 'Coaster_Name',
                          'Max vertical angle' : 'Max_Vertical_Angle',
                          'year_introduced' : 'Year_Introduced',
                          'opening_date_clean' : 'Opening_Date',
                          'speed_mph' : 'Speed_mph',
                          'height_ft' : 'Height_ft',
                          'Inversions_clean' : 'Inversions',
                          'Gforce_clean' : 'Gforce'
                       })

df = df.loc[-df.duplicated(subset=['Coaster_Name', 'Location', 'Opening_Date'])].reset_index(drop = True).copy()

# Side Bar

st.sidebar.header("Coasters Rollers Analysis Dashboard")
st.sidebar.image('coaster_roller.jpeg')
st.sidebar.write("This dashboard is using Coasters Rollers datasets from Kaggle for educational purposes.")
st.sidebar.write("")

# ## Filters

st.sidebar.write("Filter Data")

cat_filter = st.sidebar.selectbox("Categorical Filtering",(None, 'Coaster_Name', 'Location', 'Type_Main'))
num_filter = st.sidebar.selectbox("Numerical Filtering",(None, 'Year_Introduced', 'Inversions', 'Speed_mph', 'Gforce'))
row_filter = st.sidebar.selectbox("Row Filtering",(None,))
col_filter = st.sidebar.selectbox("Column Filtering",(None,))

st.sidebar.write("")
st.sidebar.markdown("Made with :heart_eyes: by Ds. [Ziad Tarik](https://www.kaggle.com/ziadtarik)")

# # Body

# Row A
a1, a2, a3, a4, a5, a6 = st.columns(6)

a1.metric("Max, Speed (mph)", df['Speed_mph'].max())
a2.metric("Max, Gforce", df['Gforce'].max())
a3.metric("Max, Height (ft)", df['Height_ft'].max())
a4.metric("Min, Speed (mph)", df['Speed_mph'].min())
a5.metric("Min, Gforce", df['Gforce'].min())
a6.metric("Min, Height (ft)", df['Height_ft'].min())

# # Row B

# st.subheader("Year Introduced vs. Speed")
# fig = px.scatter(data_frame = df,
#                 x = 'Speed_mph',
#                 y = 'Year_Introduced',
#                 color = cat_filter,
#                 size = num_filter,
#                 facet_col = col_filter,
#                 facet_row = row_filter)
# st.plotly_chart(fig, use_container_with = True)

# # Row C
c1, c2, c3 = st.columns((4,3,3))

with c1:
     st.text("Year Introduced vs. Speed",)
     fig = px.bar(data_frame = df, 
                  x = 'Year_Introduced', 
                  y = 'Speed_mph',
                  color = cat_filter)
     st.plotly_chart(fig, use_container_with = True)

# with c2:
#      st.text("Smoker vs. Total Bill")
#      fig = px.pie(data_frame = df,
#                     names="smoker", 
#                     values="total_bill", 
#                     color = cat_filter)
#      st.plotly_chart(fig, use_container_with = True)

# with c3:
#      st.text("Day vs. Tip")
#      fig = px.pie(data_frame = df, 
#                     names="day", 
#                     values="tip", 
#                     color = cat_filter,
#                     hole = 0.3)
#      st.plotly_chart(fig, use_container_with = True)          