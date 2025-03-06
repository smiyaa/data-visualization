import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st


df=pd.read_csv("C:\\Users\\smiya\\Downloads\\screentime_analysis.csv")
st.title('Screen time case study')
# print(df.isnull().sum())
# print(df['App'].unique())



st.subheader('Screen time of apps on August')
st.line_chart(data=df,x='Date',y='Usage (minutes)',color='App',use_container_width=True)


st.subheader('Usage of apps')
st.write('Most used apps are Instagram and NetFlix')
st.write('Less used app is Safari')
st.bar_chart(data=df,x='App',y='Usage (minutes)',stack=False)

st.subheader("INSTAGRAM")
insta=df[df['App'].isin(['Instagram'])]
st.bar_chart(data=insta,x='Date',y='Usage (minutes)',color='#FFB6C1')

st.subheader("NETFLIX")
netflix=df[df['App'].isin(['Netflix'])]
st.bar_chart(data=netflix,x='Date',y='Usage (minutes)',color='#90EE90')

st.subheader("WATSAPP")
wats=df[df['App'].isin(['WhatsApp'])]
st.line_chart(data=wats,x='Date',y='Usage (minutes)',color='#FFFFE0')




st.subheader('No. of times the apps opened on August')
st.bar_chart(data=df,x='App',y='Times Opened',color='App')


st.write('No. of times the apps were opened in a day')
st.bar_chart(data=df,x='Date',y='Times Opened',color='App',stack=False)

st.subheader('App Notifications')
st.bar_chart(data=df,x='App',y='Notifications',color='App')

average=df.groupby('App').agg(
    avg_usage=('Usage (minutes)', 'mean'),
    avg_notifications=('Notifications','mean'),
    avg_times_opened=('Times Opened','mean')
).reset_index()

average=average.sort_values(by='avg_usage',ascending=False)

st.dataframe(average)



