import streamlit as st

# print title + underline divider
st.header("Streamlit: Picture image app",divider=True)

# select image type
file_type=st.radio("Choose a picture image type",[".jpg",".jpeg",".gif",".png"],horizontal=True)

# upload image
file=st.file_uploader("Choose new picture image",type=file_type)

# show image
st.image(file)

