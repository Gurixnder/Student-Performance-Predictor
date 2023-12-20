import numpy as np
import streamlit as st
from code import getPrediction

result = 0

def predict():
    result = getPrediction(numOfHoursStudied,prev_marks,numberOfPracticePaperQuestions)

    if result > 100:
        result = 100
    st.text("The predicted Marks are: {}".format(result))
    return


st.title("Student Performance Predictor")

numOfHoursStudied = st.number_input('Number of hours studied', value=None, placeholder="Enter a number....")
#st.write('The current number is ', numOfHoursStudied)

prev_marks = st.number_input('Previous exam marks',value=None, placeholder="Enter a number....")
#st.write('The current number is ', prev_marks)

numberOfPracticePaperQuestions = st.number_input('Number of practice question papers solved',value=None, placeholder="Enter a number....")
#st.write('The current number is ', numberOfPracticePaperQuestions)

st.button("Predict Score", type="primary", on_click=predict())




