import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


df = pd.read_csv('RESULTS ADIT.csv')
st.title('DATA ANALYSIS')

col1, col2 = st.columns(2)
col1.metric('NAME',17)
col2.metric('TOTAL MARKS',400)

if st.button('load dataset'):
    st.write(df)

if st.sidebar.button('load description'):
    st.write(df.describe())

if st.sidebar.button('load bar chart'):
    df1=df.head(5)
    fig = plt.figure(figsize=(10,8))
    plt.bar(df1['NAME'],df1['TOTAL MARKS'])
    st.pyplot(fig) 

if st.sidebar.button('load pie chart'):
    a = np.array([69,76,83,81])
    b = ['M1','M2','M3','M4']
    fig = plt.figure(figsize=(4,4))
    plt.pie(a,labels =b)
    plt.legend(title = "Anjali:")
    st.pyplot(fig)

if st.sidebar.button('load grid chart'):
    x = np.array([69,76,83,81])
    y = np.array([85,85,90,88])
    fig = plt.figure(figsize=(4,4))
    plt.title("Data")
    plt.xlabel("marks")
    plt.ylabel("module")
    plt.plot(x,y)
    plt.grid()
    st.pyplot(fig)

if st.sidebar.button('load boxplot'):
    fig = plt.figure(figsize=(4,4))
    sns.boxplot(x='FIRST MODULE',data=df)
    st.pyplot(fig)


if st.sidebar.button('load stripplot'):
    fig = plt.figure(figsize=(10,8))
    sns.stripplot(df)
    st.pyplot(fig)
