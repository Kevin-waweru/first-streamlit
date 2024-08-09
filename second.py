import streamlit as st
import requests
import pandas as pd
import io

st.title("data visualization")
csvfile=st.file_uploader("Upload csv file",'csv')

if csvfile is not None:
    st.write("file uploaded...")
    

    st.subheader("data preview")
    st.write(df.head())
    st.header("data summary")
    st.write(df.describe())

    st.subheader("filter data")
    columns=df.columns.tolist()
    selectedcolumn=st.selectbox("select column to filter by",columns)

    selectedfilter=df[selectedcolumn].unique()
    selectedvalue=st.selectbox("select value to filter",selectedfilter)
    filt=df[df[selectedcolumn]==selectedvalue]
    
    st.write(filt)
else:
    st.write("waiting for file upload...")
