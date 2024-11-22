#library Import
import streamlit as st
import pandas as pd
import requests
#Page Setup
st.set_page_config(page_title = "Pokedex",layout="wide")
st.title("Pokemon Stat Sheet")

#read excel file and create dataframe
url= 'https://github.com/Tmangoz/Pokemon/blob/main/pokemon_data.xlsx'
myfile = requests.get(url)
xlsx = pd.read_excel(myfile.content)
poke_data = pd.DataFrame(xlsx) 

#Show the dataframe(Delete Later)
st.write    
