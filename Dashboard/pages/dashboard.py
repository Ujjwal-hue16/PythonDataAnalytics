import pandas as pd
import seaborn as sns
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go

st.title("Titanic dashboard")
#load the dataset
df = sns.load_dataset("titanic")

st.dataframe(df)

st.sidebar.header("Filter option")

#gender filter
gender = st.sidebar.multiselect('Gender',
                                     options= df['sex'].unique(),
                                     default=df['sex'].unique())

#class filter
pclass = st.sidebar.multiselect('Passenger Class',
                                       options=sorted (df['pclass'].unique()),
                                                       default = df['pclass'].unique())

#Age filters
min_age, max_age = st.sidebar.slider("Age",
                                      min_value= int(df['age'].min()),
                                      max_value = int(df['age'].max()),
                                      value = (int(df['age'].min()),int(df['age'].max())))

#filter the data based on the user selection
filtered_df = df[
        (df['sex'].isin(gender))&
        (df['pclass'].isin(pclass))&
        (df['age']>=min_age)&
        (df['age']<=max_age)
]
st.dataframe(filtered_df)

#Create a pie chart for gender distribution

st.subheader("Gender Distribution ")
gender_count = filtered_df['sex'].value_counts()
fig = px.pie(names=gender_count.index,values=gender_count.values,title='Gender Distribution')
st.plotly_chart(fig)

#Create a histogram for age distribution 
st.subheader("Age Distribution")
fig = px.histogram(filtered_df, x='age',nbins=20, title='Age Distribution',
                   labels={'age':'Age','count':'Number of passengers'})
st.plotly_chart(fig)

#violin plot of age distribution by survival class
#scatter plot of age vs fare
#box plot of age distribution by class
#bar chart of survival class
