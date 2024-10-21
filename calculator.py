import streamlit as st

st.title('calculator')
st.markdown('welcome to my first streamlt app')

c1, c2= st.columns(2)
fnum= c1.number_input('enter first number', value=0)
snum= c2.number_input('enter second number', value=0)
options= ['add','subtract','multiply','divide']
choice= st.radio('select operarion', options)

button = st.button("calculate")


if button:
    if choice == "Add":
         result = fnum + snum
    if choice == "Subtract":
        result = fnum - snum
    if choice == "Multiply":
         result = fnum*snum
    if choice == "Divide":
         result= fnum/snum
    st.success(f'Result is {result}') 
    

