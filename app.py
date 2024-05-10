import streamlit as st
import pickle
import pandas as pd

#Defining the backend function
def get_df_and_predict():
        if Gender=="Female":
                col_1=1
        else:
                col_1=0
        
        if Geography=="Germany":
                col_2=1
        else:
                col_2=0
        
        col_3=CreditScore
        col_4=Age
        col_5=Balance
        col_6=NumOfProducts
        
        if IsActiveMember=="Yes":
                col_7=1
        else:
                col_7=0
        
        col_8=EstimatedSalary
        
        test = {'onehot__Gender_Female':[col_1],
        'onehot__Geography_Germany':[col_2],
        'remainder__CreditScore':[col_3],
        'remainder__Age':[col_4],
        'remainder__Balance':[col_5],
        'remainder__NumOfProducts':[col_6],
        'remainder__IsActiveMember':[col_7],
        'remainder__EstimatedSalary':[col_8]}
        
        df = pd.DataFrame(test)
        filename = 'random_forrest.pkl'
        with open(filename, 'rb') as file:
                model = pickle.load(file)
                pred_value = model.predict(df)
                if pred_value==1:
                        pred="Customer will leave 😥"
                else:
                        pred="Customer will not leave 😃"
                        
        return pred

pred="Calculating Churn"

#Main Frontend
st.set_page_config(
        page_title="Bank Churn Predictor",
        page_icon="🚨",
        layout='wide',
        menu_items={
                "Get Help": None,
                "Report a Bug": None,
                "About": None
        }
)

with st.form('Bank_Churn_Predictor'):
        st.title("Bank Churn Predictor")
        col1, col2 = st.columns(2)
        with col1:
                CreditScore=st.number_input("Enter the CreditScore")
                Age=st.number_input("Enter the age")
                Gender=st.selectbox("Select Gender",['Male','Female'])
                Tenure=st.slider("Select the Tenure",min_value=1,max_value=10)

        with col2:
                Balance=st.number_input("Enter the Balance")
                EstimatedSalary=st.number_input("Enter the Estimated Salary")
                Geography=st.selectbox("Select Country", ['Spain','Germany','France'])
                NumOfProducts=st.slider("Number of products the customer uses",min_value=1,max_value=4)
                
        HasCrCard=st.selectbox("Does the customer have a credit card?",["Yes","No"])
        IsActiveMember=st.selectbox("Is the customer an active member?",["Yes","No"])
        
        submitted = st.form_submit_button("Predict")
        if submitted:
                pred=get_df_and_predict()

              
st.title("Outcome")
st.title(pred)
                


