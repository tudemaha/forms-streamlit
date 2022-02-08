import streamlit as st
from gsheetsdb import connect
import matplotlib.pyplot as plt
import numpy as np

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

# store data from query into list
genders, cities, languages = [], [], []
for row in rows:
    genders.append(row.gender)
    cities.append(row.city.title())
    languages.append(row.language)

# gender chart
st.markdown("<h5>1. Jenis Kelamin</h5>", unsafe_allow_html=True)

genders_labels = unique(genders)
genders_sizes = [genders.count('Laki-laki'), genders.count('Perempuan')]

fig1, ax1 = plt.subplots(figsize=(7, 4))
ax1.pie(genders_sizes, labels=genders_labels, autopct='%1.1f%%', shadow=True, startangle=90, radius=3)
ax1.axis('equal')
st.pyplot(fig1)

# city chart
st.markdown("<br><h5>2. Asal Responden</h5>", unsafe_allow_html=True)
cities_label = unique(cities)
cities_sizes = []

for city in cities_label:
    cities_sizes.append(cities.count(city))

x = np.arange(len(cities_label))
width = 0.35

fig2, ax2 = plt.subplots()
rects = ax2.bar(x, cities_sizes, width)

# add text for labels and custom x-axis tick label, etc.
ax2.set_ylabel('Jumlah')
ax2.set_xticks(x, cities_label)
ax2.legend()

ax2.bar_label(rects, padding=3)
fig2.tight_layout()

st.pyplot(fig2)

# programming language chart
st.markdown("<br><h5>3. Bahasa Pemrograman Favorit</h5>", unsafe_allow_html=True)

languages_label = unique(languages)
languages_sizes = []
for language in languages_label:
    languages_sizes.append(languages.count(language))

fig3, ax3 = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))
wedges, texts = ax3.pie(languages_sizes, wedgeprops=dict(width=0.5), startangle=-40)

bbox_props = dict(boxstyle="square,pad=0.3", fc="w", ec="k", lw=0.72)
kw = dict(arrowprops=dict(arrowstyle="-"), bbox=bbox_props, zorder=0, va="center")

for i, p in enumerate(wedges):
    ang = (p.theta2 - p.theta1)/2. + p.theta1
    y = np.sin(np.deg2rad(ang))
    x = np.cos(np.deg2rad(ang))
    horizontalalignment = {-1: "center", 1: "center"}[int(np.sign(x))]
    connectionstyle = "angle,angleA=0,angleB={}".format(ang)
    kw["arrowprops"].update({"connectionstyle": connectionstyle})
    ax3.annotate(languages_label[i] + (f"\n({languages_sizes[i]})"), xy=(x, y), xytext=(1.45*np.sign(x), 1.45*y),
                horizontalalignment=horizontalalignment, **kw)

st.pyplot(fig3)

# hello world example
st.markdown("<br><h5>4. Kreasi Hello World Mereka...</h5>", unsafe_allow_html=True)


for language in languages_label:
    st.write(language)
    for row in rows:
        if row.language == language:
            st.code(row.hello, language.lower())