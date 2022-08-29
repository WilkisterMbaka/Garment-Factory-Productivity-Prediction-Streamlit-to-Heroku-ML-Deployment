import streamlit as st


st.title('Garment Factory Productivity Prediction ML App')
st.markdown('A model that can predict the level of productivity of employee teams in the garment industry.')
st.header('Productivity Variables')
col1, col2 = st.columns(2)


# display the front end aspect
# st.markdown(html_temp, unsafe_allow_html = True) 
  
# following lines create boxes in which user can enter data required to make prediction 
with col1:
    department = st.selectbox('Department',('sewing','finishing'))
    quarter = st.number_input('Month Quarter', min_value = 1, step = 1, max_value = 4)
    team = st.number_input('Team Number', min_value = 1, step = 1, max_value = 12)
    targeted_productivity = st.number_input('Targeted Productivity', min_value = 0.00,  max_value = 10.00, step = 0.01)
    std_minute_value = st.number_input('Standard Minute Value', min_value = 0.00, step = 0.01)

with col2:
    work_in_progress = st.number_input('Work In Progress', min_value = 0.00, step = 0.01)
    over_time = st.number_input('Over Time', min_value = 0, step = 1)
    incentive = st.number_input('Incentive', min_value = 0.00, step = 0.01)
    idle_men = st.number_input('Idle Men', min_value = 0, step = 1)
    no_of_workers = st.number_input('Number of Workers', min_value = 0, step = 1)

result =""

import pickle
import streamlit as st
 
# loading the trained model
pickle_in = open('classifier.pkl', 'rb') 
classifier = pickle.load(pickle_in)

import joblib
def prediction(quarter, department, team, targeted_productivity, std_minute_value, work_in_progress, over_time, incentive, idle_men, no_of_workers):
    # Pre-processing user input    
    if department == 'sewing':
        department = 0
    else:
        department = 1
    
    # Making predictions 
    prediction = classifier.predict( 
        [[quarter, department, team, targeted_productivity, std_minute_value, work_in_progress, over_time, incentive, idle_men, no_of_workers]])
     
    return prediction
    
    # clf = joblib.load('model.sav')
    # return clf.predict(quarter, department, team, targeted_productivity, std_minute_value, work_in_progress, over_time, incentive, idle_men, no_of_workers)

if st.button("Predict Productivity"): 
    result = prediction(quarter, department, team, targeted_productivity, std_minute_value, work_in_progress, over_time, incentive, idle_men, no_of_workers) 
    st.success('Your predicted productivity is {}'.format(result))
