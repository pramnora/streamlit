import streamlit as st
import pandas as pd

# read external file
data_frame=pd.read_csv("data.csv")

# display file contents
st.write(data_frame)
