import numpy as np
import pickle
import streamlit as st








#loading the saved model
loaded_model = pickle.load(open('trained_model.sav', 'rb'))


#create a function for prediction

def bmi_pred(input_data):
    #changing the input data to numpy array

    input_array=np.asarray(input_data)

    #reshape

    input_array_reshape = input_array.reshape(1,-1)
    prediction= loaded_model.predict(input_array_reshape)
    print(prediction)

    if (prediction == 0):
             print('The person is normal')
    elif (prediction == 1):
                print('The person is Obese')
    elif (prediction == 2):
                print('The person is Overweight')
    else:
                print('The person is Underweight')       
                

def main():

    #giving a title
    st.title("BMI web app")

    #getting input data from users

    Age = st.text_input('ENTER YOUR AGE')
    Gender = st.text_input('ENTER THE GENDER')
    Height = st.text_input('ENTER THE HEIGHT')
    Weight = st.text_input('ENTER YOUR WEIGHT')
    BMI = st.text_input('YOUR BMI')
  


    #code for prediction
    diagnosis = ' '
    
    #creating a button for prediction

    if st.button('Check result'):
        diagnosis = bmi_pred([Age, Gender, Height, Weight, BMI ])
        # diagnosis = bmi_pred([18, 1, 180, 60, 25])


    st.success(diagnosis)







if __name__ == "__main__":
    main()



















