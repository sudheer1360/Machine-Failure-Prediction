import streamlit as st
import pickle

model=pickle.load(open('model.pkl','rb'))
st.title('Machine Failure Prediction')

Type=st.text_input('Enter the Type of Machine')
AT=st.text_input('Enter the Air Temperature: ')
PT=st.text_input('Enter the Process Temperature: ')
RPM=st.text_input('Enter the RPM: ')
Torque=st.text_input('Enter the Torque: ')
Tw=st.text_input('Enter the Tool wear:')



if st.button('Predict'):
    Type=int(Type)
    AT=float(AT)
    PT=float(PT)
    RPM=float(RPM)
    Torque=float(Torque)
    Tw=float(Tw)


    data=[[Type,AT,PT,RPM,Torque,Tw]]
    result=model.predict(data)
    st.success(result)

    if result[0]==0:
        st.write("Working")


    else :
        st.write("Failure")

