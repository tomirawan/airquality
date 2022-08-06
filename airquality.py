import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import datetime
import calendar
import streamlit as st

st.write("""

# Simple Air Quality Dashboard
###### Air quality report in Yogyakarta region monthly on 2021.

""")
for x in range(1,13):
    m = calendar.month_name[x]

st.sidebar.header('Select Month')
st.sidebar.columns((1,2))
selected_month = st.sidebar.selectbox(
                '',
                ('January','February','March','April','May','June','July',
                'August','September','October','November','December'))

#@st.cache(suppress_st_warning=True)

#Prepare the data
def load_data(dataset):
    df = pd.read_csv(dataset)

    df.iloc[:,1] = pd.to_datetime(df.iloc[:,1], format='%H:%M:%S')
    df.iloc[:,1] = df.iloc[:,1].dt.hour
    df.index = df.iloc[:,1]

    df = df.drop(df.columns[[1,-3]], axis=1)

    st.write("""

    This graph shows you the particle contained in air.

    """)

    #Show the graph in each particle
    fig1 = plt.figure(figsize=(12,8))
    sns.lineplot(data=df,
                markers=True)
    plt.xticks(range(0,24))
    plt.xlabel('Hour')
    plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    st.pyplot(fig1)

    st.write("""

    This chart shows you the air quality indicator in Yogyakarta.

    """)

    #Show the air quality indicator
    fig2 = plt.figure(figsize=(6,4))
    sns.countplot(df.iloc[:,-1])
    st.pyplot(fig2)
    return

if selected_month == 'January':
    src = 'jan.csv'
elif selected_month == 'February':
    src = 'feb.csv'
elif selected_month == 'March':
    src = 'mar.csv'
elif selected_month == 'April':
    src = 'apr.csv'
elif selected_month == 'May':
    src = 'may.csv'
elif selected_month == 'June':
    src = 'jun.csv'
elif selected_month == 'July':
    src = 'jul.csv'
elif selected_month == 'August':
    src = 'aug.csv'
elif selected_month == 'September':
    src = 'sep.csv'
elif selected_month == 'October':
    src = 'oct.csv'
elif selected_month == 'November':
    src = 'nov.csv'
elif selected_month == 'December':
    src = 'dec.csv'

load_data(src)
