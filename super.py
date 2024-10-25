import pandas as pd
import numpy as np
import pickle as pickle
import streamlit as st


file1 = open('Super.pkl', 'rb')
rf = pickle.load(file1)
file1.close()

data = pd.read_csv("Super.csv")

st.title("Laptop Price Predictor")

Company = st.selectbox('Brand', data['Company'].unique())

TypeName=st.selectbox('Type',data['TypeName'].unique())

C_name=st.selectbox('Processor',data['C_name'].unique())

Brand=st.selectbox('GPU',data['Brand'].unique())

OS=st.selectbox('Operating System',data['OS'].unique())

RAM=st.selectbox('RAM (in GB)',[2, 4, 6, 8, 12, 16, 24, 32, 64])

SSD=st.selectbox('SSD(in GB)', [0, 8, 128, 256, 512, 1024])

Weight =st.number_input('Weight of the laptop(in Kg)')

ScreenSize=st.number_input('Screen size(in inches)')

Resolution = st.selectbox('Screen Resolution', [
                          '1920x1080', '1366x768', '1600x900', '3840x2160', '3200x1800', '2880x1800', '2560x1600', '2560x1440', '2304x1440'])

TouchScreen=st.selectbox('Touch Screen',['Yes','No'])
                      
IPSPanel=st.selectbox('IPS',['Yes','No'])

if st.button('Predict Price'):
    PPI=None
    if TouchScreen=='Yes':
        TouchScreen=1
    else:
        TouchSreen=0
        
    if IPSPanel=='Yes':
        IPSPanel=1
    else:
        IPSPanel=0
        
    X_resolution = int(Resolution.split('x')[0])
    Y_resolution = int(Resolution.split('x')[1])

    PPI = ((X_resolution**2)+(Y_resolution**2))**0.5/(ScreenSize)
    
    query = np.array([Company,TypeName,RAM,Weight,TouchScreen,IPSPanel,
       PPI,C_name,SSD,Brand,OS])
    
    query = query.reshape(1, 11)
    
    prediction = int(np.exp(rf.predict(query)[0]))
    
    st.title("Predicted price for this laptop could be between " +
             str(prediction-1000)+"₹" + " to " + str(prediction+1000)+"₹")


