# CREATED: Date/Time: Thu 4th June 2026 19:30 PM GMT
# UPDATED: Date/Time: Thu 4th June 2026 19:30 PM GMT
# ------
# Streamlit program: 12 x Tables
# ------
# This code shows how to use the 'slider' control
# to select a number from: 1 up to 12;

# in fact, it uses 2 such similar 'slider' controls...
# the slider control number values are stored in variables: x,y;

# which, then, produces the output sum of: x * y;
# or, in other words, produces the 12 x Tables.
# ------
import streamlit as st
st.header("PROGRAM: 12 Time tables:-")
x=st.slider("Choose a x value:",1,12)
y=st.slider("Choose a y value:",1,12)
st.write("Output values: ( :red[***x***] : ",x,") ( :blue[***y***] : ",y,") ( :red[x] * :blue[y] : ",x*y,")")
