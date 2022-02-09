#import libraries
import streamlit as st
from gsheetsdb import connect
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

# form title for subtitle
form_title = 'Ayo Kawan! Ayo Testing2...'

# create connect object
conn = connect()

# function to run query from Google Sheets (chached for 30 sec)
@st.cache(ttl=30)
def run_query(query):
    rows = conn.execute(query, headers=1)
    return rows

# page config
image = Image.open('favicon.ico')
st.set_page_config(
    page_title='Google Forms Data Visualization',
    page_icon= image,
    menu_items={
        'About': '''
                  Google Forms data visualization app.

                  Visit the repository: https://github.com/tudemaha/forms-streamlit/
                  Created with :heart: by Tude Maha
                 '''
    }
)

# import sheet url and save query in rows
sheet_url = st.secrets["public_gsheets_url"]
rows = run_query(f'SELECT * FROM "{sheet_url}"')

# title and subtitle
st.markdown("<h1 style='text-align: center'>Google Forms Data Visualization</h1>", unsafe_allow_html=True)
st.markdown(f"<h3 style='text-align: center'>From Form: {form_title}</h3><br>", unsafe_allow_html=True)

# sidebar
total_respondens = st.sidebar.radio(
    'Tampilkan jumlah responden?',
    ('Ya', 'Tidak'),
    index=1
    )

st.sidebar.markdown("<h5>Data apa saja yang ingin ditampilkan?</h5>", unsafe_allow_html=1)
gender_checkbox = st.sidebar.checkbox("Jenis Kelamin", True)
city_checkbox = st.sidebar.checkbox("Tempat Asal", True)
language_checkbox = st.sidebar.checkbox("Bahasa Pemrograman Favorit", True)
hello_checkbox = st.sidebar.checkbox("Kreasi Hello World", True)

# function to find unique values
def unique(list):
    unique_list = []
    for string in list:
        if string not in unique_list:
            unique_list.append(string)
    return unique_list

# store data from query into list
genders, cities, languages = [], [], []
total = 0
for row in rows:
    genders.append(row.gender)
    cities.append(row.city.title())
    languages.append(row.language)
    total += 1

# default foreground color
back_color = '#0E1117'

# show total respondens
if total_respondens == 'Ya':
    st.markdown(f"<h5>Jumlah responden: {total}</h5>", unsafe_allow_html=True)

# gender chart
if gender_checkbox:
    # subsection title
    st.markdown("<h5>Jenis Kelamin:</h5>", unsafe_allow_html=True)

    # make needed object for plotting figure 1
    genders_labels = unique(genders)
    genders_sizes = [genders.count('Laki-laki'), genders.count('Perempuan')]

    # plot figure 1
    fig1, ax1 = plt.subplots(figsize=(7, 4), facecolor=back_color)
    ax1.pie(genders_sizes, labels=genders_labels, autopct='%1.1f%%', shadow=True, startangle=90, radius=3, textprops={'color': 'w'})
    ax1.axis('equal')
    st.pyplot(fig1)

# city chart
if city_checkbox:
    # subsection title
    st.markdown("<br><h5>Asal Responden:</h5>", unsafe_allow_html=True)

    # make needed object for plotting figure 2
    cities_label = unique(cities)
    cities_sizes = []

    # count the same city
    for city in cities_label:
        cities_sizes.append(cities.count(city))

    # starting to plot figure 2 with its properties
    x = np.arange(len(cities_label))
    width = 0.35

    fig2, ax2 = plt.subplots(facecolor=back_color)
    ax2.set_facecolor(color='#1A1C24')
    rects = ax2.bar(x, cities_sizes, width)
    ax2.tick_params(colors='w')
    plt.setp(ax2.spines.values(), color='w')


    # add text for labels and custom x-axis tick label, etc.
    ax2.set_ylabel('Jumlah', color='w')
    ax2.set_xticks(x, cities_label, rotation='vertical', color='w')

    ax2.bar_label(rects, padding=-14, color='w')
    fig2.tight_layout()

    st.pyplot(fig2)

# make languages_label public for language chart and hello world example
languages_label = unique(languages)

# programming language chart
if language_checkbox:
    # subsection title
    st.markdown("<br><h5>Bahasa Pemrograman Favorit:</h5>", unsafe_allow_html=True)

    # count for the same programming languages
    languages_sizes = []
    for language in languages_label:
        languages_sizes.append(languages.count(language))

    # properties for figure 3
    fig3, ax3 = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"), facecolor=back_color)
    wedges, texts = ax3.pie(languages_sizes, wedgeprops=dict(width=0.5), startangle=-40)

    bbox_props = dict(boxstyle="square,pad=0.3", fc="#1A1C24", ec="w", lw=0.72, )
    kw = dict(arrowprops=dict(arrowstyle="-", color='w'), bbox=bbox_props, zorder=0, va="center")

    # starting to plot figure 3
    for i, p in enumerate(wedges):
        ang = (p.theta2 - p.theta1)/2. + p.theta1
        y = np.sin(np.deg2rad(ang))
        x = np.cos(np.deg2rad(ang))
        horizontalalignment = {-1: "center", 1: "center"}[int(np.sign(x))]
        connectionstyle = "angle,angleA=0,angleB={}".format(ang)
        kw["arrowprops"].update({"connectionstyle": connectionstyle})
        ax3.annotate(languages_label[i] + (f"\n({languages_sizes[i]})"), xy=(x, y), xytext=(1.6*np.sign(x), 1.45*y),
                    horizontalalignment=horizontalalignment, **kw, color='w')

    st.pyplot(fig3)

# hello world example
if hello_checkbox:
    # subsection title
    st.markdown("<br><h5>Kreasi Hello World Mereka...</h5>", unsafe_allow_html=True)

    # show programming languages choosen by user
    for language in languages_label:
        st.write(language)

        # show hello world examples following the programming languages choosen
        for row in rows:
            if row.language == language:
                st.code(row.hello, language.lower())
