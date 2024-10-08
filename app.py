import streamlit as st
import pickle
import sklearn
import pandas as pd
import numpy as np
from PIL import Image


model = pickle.load(open('model.sav','rb'))

st.title("NBA Player's Salary Prediction")
st.sidebar.header('Player Data')
image = Image.open('BB.png')
st.image(image,'')

#Function

def user_report():
    rating = st.sidebar.slider('Rating', 0,100,60)
    jersey = st.sidebar.slider('Jersey', 0,100,1)
    team = st.sidebar.slider('Team', 0,30,1)
    position = st.sidebar.slider('Position', 0,10,1)
    country = st.sidebar.slider('Country', 0,3,1)
    draft_year = st.sidebar.selectbox('Draft Year', [2000] + [i for i in range(2000, 2021)])
    draft_round = st.sidebar.selectbox('Draft Round', [1] + [i for i in range(1, 11)])
    draft_peak = st.sidebar.selectbox('Draft Peak', [1] + [i for i in range(1, 31)])

    user_report_data = {
        'rating': rating,
        'jersey': jersey,
        'team': team, 
        'position': position, 
        'country': country,
        'draft_year': draft_year, 
        'draft_round': draft_round,
        'draft_peak': draft_peak,
    }

    report_data = pd.DataFrame(user_report_data, index=[0])
    return report_data

user_data = user_report()
st.header('Player Data')
st.write(user_data)

salary = model.predict(user_data)
st.subheader("Player's Salary")
st.subheader('$'+str(np.round(salary[0],2)))

