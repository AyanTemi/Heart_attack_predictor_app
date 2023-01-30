#import packages
import streamlit as st
import pandas as pd
import pickle


 
#loading the model
model = pickle.load(open('log_model.pkl','rb'))



def prediction(Age, Sex, Exang, CAA, CP, FBS, RESTECG, THALACH, SLP, THALL):   
 
    # Pre-processing user input    
    if Sex == "Male":
        Sex = 0
    else:
        Sex = 1
 
    if Exang == "No":
        Exang = 0
    else:
        Exang = 1
 
    if CP == "typical anginal":
        CP = 1
    elif CP == "atypical anginal":
        CP = 2
    elif CP == "non-anginal pain":
        CP = 3
    else:
        CP = 4
 
    if FBS == "False":
        FBS = 0
    else:
        FBS = 1

    if RESTECG == "normal":
        RESTECG = 0
    elif  RESTECG == "abnormal":
        RESTECG = 1
    else:
        RESTECG = 2

     #predictions
    prediction = model.predict([[Age, Sex, Exang, CAA, CP, FBS, RESTECG, THALACH, SLP, THALL]])
     
    if prediction == 0:
        pred = 'Low Risk'
    else:
        pred = 'High Risk'
    return pred

#main
def main():       
    # front end 
    st.markdown("<h1 style='text-align: center; color: White;background-color:Blue'>Heart Attack Predictor</h1>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: side; color: Black;'>About this App.</h2>", unsafe_allow_html=True)
    st.markdown("#### This is a web app that helps the user, especially medical personnel, determine whether a patient is at risk of a heart attack.")
    st.markdown("## Tools Used?")
    st.markdown("#### The model was made using a dataset from Kaggle, and Kaggle notebooks were used to train the model. I made use of Sci-Kit Learn in order to make the logistic linear regression model.")
      
    # create boxes and sliders for users to enter data required to make prediction 
    Sex = st.selectbox('Sex',("Male","Female"))
    Age = st.number_input("Patient's Age") 
    Exang = st.selectbox('Exercise induced Anginal',("Yes","No"))
    CP = st.selectbox('chest pain',("typical anginal","atypical anginal", "non-anginal pain", "asymptomatic"))
    THALACH = st.number_input("Max heart rate achieved")
    FBS = st.selectbox('Fasting Blood Sugar > 120mg/dl',("True","False"))
    RESTECG = st.selectbox('resting electrocardiographic results',("normal", "abnormal", "hypertrophy"))
    CAA = st.slider("number of major vessels",0,3) 
    SLP = st.slider("number of slope", 0, 2)   
    THALL = st.slider("thall rate", 0, 3)
    output = ""
      
    # when 'Predict' is clicked, make the prediction and store it 
    if st.button("Predict"): 
        output = prediction(Age, Sex, Exang, CAA, CP, FBS, RESTECG, THALACH, SLP, THALL)
        st.success(f'You have a {output} of heart attack')

if __name__=='__main__': 
    main()




    
   
