import streamlit as st
st.header("PROGRAM: 12 Time tables:-")
x=st.slider("Choose a x value:",1,12)
y=st.slider("Choose a y value:",1,12)
st.write("Output values: ( :red[***x***] : ",x,") ( :blue[***y***] : ",y,") ( :red[x] * :blue[y] : ",x*y,")")
