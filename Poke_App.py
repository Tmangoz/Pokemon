#library Import
import streamlit as st
import pandas as pd
#Page Setup
st.set_page_config(page_title = "Pokedex",layout="wide")
st.title("Pokemon Stat Sheet")

#read excel file and create dataframe
xlsx = pd.read_excel("pokemon_data.xlsx")
poke_data = pd.DataFrame(xlsx) 

#Show the dataframe(Delete Later)
st.write    
