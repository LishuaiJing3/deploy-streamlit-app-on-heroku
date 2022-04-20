

import streamlit as st
from utils.pkg1 import add_int # You can train models, data processing etc.

input1 = st.sidebar.number_input(
    'Input 1', min_value=0, max_value=100, value=25)

input2 = st.sidebar.number_input(
    'Input 2', min_value=0, max_value=100, value=25)

tax_schema = st.sidebar.selectbox(
    'Tax schema', ['Business', 'Personal'])



st.title('A simple calculation tool')


html_temp = """
	<div style="background-color:#85929E;"><p style="color:white;font-size:16px;padding:10px">A simple template to get streamlit deployed on Heroku. You can add data applications, models etc. here.  </p></div>
	"""
st.markdown(html_temp, unsafe_allow_html=True)


# Create a button, that when clicked, shows a text
if(st.button("Calculate")):

    st.write(add_int(input1,input2))
	
   
    
