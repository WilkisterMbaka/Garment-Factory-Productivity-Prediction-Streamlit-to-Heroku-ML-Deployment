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
 

# load saved model
with open('classifier.pkl' , 'rb') as f:
    classifier = pickle.load(f)

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
    

if st.button("Predict Productivity"): 
    result = prediction(quarter, department, team, targeted_productivity, std_minute_value, work_in_progress, over_time, incentive, idle_men, no_of_workers) 
    if result >= 0.75:
      st.success('Your predicted productivity is: {}'.format((result).round(2))) 
      st.success('High productivity')    
   
    elif result >= 0.5:
      st.success('Your predicted productivity is {}'.format((result).round(2)))
      st.success('Moderate productivity')
    else:
      st.success('Your predicted productivity is {}'.format((result).round(2)))
      st.success('Below Average productivity')
