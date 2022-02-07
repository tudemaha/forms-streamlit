import streamlit as st
from gsheetsdb import connect
import matplotlib.pyplot as plt

form_title = 'Ayo Kawan! Ayo Testing2...'

conn = connect()

@st.cache(ttl=30)
def run_query(query):
    rows = conn.execute(query, headers=1)
    return rows

sheet_url = st.secrets["public_gsheets_url"]
rows = run_query(f'SELECT * FROM "{sheet_url}"')

st.markdown("<h1 style='text-align: center'>Google Forms Data Visualization</h1>", unsafe_allow_html=True)
st.markdown(f"<h3 style='text-align: center'>From Form: {form_title}</h3><br>", unsafe_allow_html=True)

# gender chart
st.markdown("<h5>Jenis Kelamin</h5>", unsafe_allow_html=True)

gender = []
city = []
for row in rows:
    gender.append(row.gender)
    city.append(row.city)

gender_labels = 'Laki-laki', 'Perempuan'
gender_sizes = [gender.count('Laki-laki'), gender.count('Perempuan')]
fig1, ax1 = plt.subplots()
ax1.pie(gender_sizes, labels=gender_labels, autopct='%1.1f%%', shadow=True, startangle=90, radius=3)
ax1.axis('equal')
st.pyplot(fig1)
