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

# function to find unique values
def unique(list):
    unique_list = []
    for string in list:
        if string not in unique_list:
            unique_list.append(string)
    return unique_list


# gender chart
st.markdown("<h5>Jenis Kelamin</h5>", unsafe_allow_html=True)

genders, cities, languages, hello = [], [], [], []

for row in rows:
    genders.append(row.gender)
    cities.append(row.city)
    languages.append(row.language)

genders_labels = unique(genders)
genders_sizes = [genders.count('Laki-laki'), genders.count('Perempuan')]
fig1, ax1 = plt.subplots()
ax1.pie(genders_sizes, labels=genders_labels, autopct='%1.1f%%', shadow=True, startangle=90, radius=3)
ax1.axis('equal')
st.pyplot(fig1)

# programming language chart


languages_label = unique(languages)
languages_sizes = []
for language in languages_label:
    languages_sizes.append(languages.count(language))

st.write(languages_label)
st.write(languages_sizes)
