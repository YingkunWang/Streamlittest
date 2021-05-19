import streamlit as st
import pandas as pd

st.title("Vehicle Speed")

@st.cache
def get_data():
    df = pd.read_excel("testdataset.csv", index_col=0)
    return df

df = get_data()

types = df['vehicleType'].drop_duplicates()
make_choice = st.sidebar.selectbox('Select your vehicle:', types)
selectedspeed = df.loc[df["vehicleType"] == make_choice]

col1, col2 = st.beta_columns([3,1])
with col1:
    st.write('Results:', selectedspeed)

with col2:
   st.write('Mean:', selectedspeed['speeding'].mean())

# st.write('Results:', selectedspeed)
# st.write('Mean:', selectedspeed['speeding'].mean())
st.write('Bar Chart:')
st.bar_chart(selectedspeed.groupby("speeding").count())
