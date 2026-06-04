# streamlit

**CREATED**: *Thu 8th May 2025 22:36 PM GMT*  
**UPDATED**: *Thu 4th Jun 2026 20:07 PM GMT* 

-----

## Introduction

Thu 8th May 2025 22:36 PM GMT  
Today, I created this streamlit repository so that I can run 'live' code from here.  

## Explaining more about Streamlit/and, how it is used

Streamlit, is FREE...; and, it comes with its own individual code library of objects.      

The first line of code is, usually, to **import** the streamlit library by using it's alias: 'st':      

> import streamlit as st  

Then, that line might be followed by the **import** of any other code libraries your program may wish to use:   

> import streamlit as st    
> import numpy as np  
> import pandas as pd  
> import matplotlib.pyplot as plt  
> import scipy  
> from scipy import stats   
> -etc.  

### Stream lit objects...

- st.title()  
- st.header()  
- st.markdown()  
- st.write()  
- st.slider()  
- st.button()  
- etc.  

-----

### Your 1st Streamlit program  

For one's very first Streamlit program...;   
then, it's really not necessary to write any code...;   
instead, you just type into the terminal window the command...    

> streamlit hello

...and, automatically, that will load up your *web browser* software...;     
and, lead you to an explanation web page containing further links you can *click* on...;        
together with some Streamlit **example programs**.  

-----

When you are ready to write your first Streamlit 'Hello, world' program; then...   

> import streamlit as st  
> st.header("My 1st app...")  
> st.write("Hello, world!")  

...save the code as being called:     

my1st.py  

(**NOTE**: All Python3 program files are saved using: filename + extension: .py)       

...in order to run the code file called: my1st.py;    
...inside of the terminal application window type:  

python my1st.py  

...your web browser will load up, automatically; and, then, display the *output* as a web page.    

-----
   
## Links

Streamlit official web site    
- https://streamlit.io   
