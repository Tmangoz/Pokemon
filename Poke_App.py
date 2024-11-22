#library Import
import streamlit as st
import pandas as pd
import requests
from io import BytesIO #Import Bytes IO to handle binary file content

#Page Setup
st.set_page_config(page_title = "Pokedex",layout="wide")
st.title("Pokemon Stat Sheet")

#read excel file and create dataframe
url= 'https://github.com/Tmangoz/Pokemon/blob/main/pokemon_data.xlsx'
response = requests.get(url)

if response.status_code == 200: #check if the request was successful
  data = BytesIO(response.content)
  poke_data = pd.read_excel(data)
  st.dataframe(poke_data) #Display Dataframe in the Streamlit app
else:
  st.error("Failed to retrieve data from the provided URL.")

 
