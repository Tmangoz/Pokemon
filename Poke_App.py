#library Import
import streamlit as st
import pandas as pd
import openpyxl
#Page Setup
st.set_page_config(page_title = "Pokedex",layout="wide")
st.title("Pokemon Stat Sheet")
#read excel file and create dataframe
csv = pd.read_csv("pokemon_data.csv")
poke_data = pd.DataFrame(csv) 
poke_data.head()
#Get User input for Pokemon they want
Answer = str(st.text_input("Please enter the Pokemon you'd like to view"))
#Capitalize the first letter of input as all names in CSV start with uppercase letter
capitalized_Answer = Answer.capitalize()
#Remove Index Value so not displayed on print
blankIndex=[''] * len(poke_data)
poke_data.index=blankIndex
#User clicks search button to search the pokemon they are trying to look up
if st.button("Search"):
    st.write(poke_data.loc[poke_data.Name==capitalized_Answer])
else:
    print("Please check your spelling or enter a valid name of a pokemon")

 
