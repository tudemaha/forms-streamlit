# **Google Form Data Visualization**
This project built using Streamlit -- a web-based front-end for Python. In this project, you can display your public Google Forms's responds data, and the best one is you can fully control which data you want to display in your Streamlit app.

## **Requirements**
1. Programming Language
   - [Python](https://www.python.org)
2. Python Libraries
   - [Streamlit](https://streamlit.io) [The main library]
   - [gsheetsdb](https://github.com/betodealmeida/gsheets-db-api) [It's now replaced by shillelagh, but you still can use it]
   - [Matplotlib](https://matplotlib.org) [For chart plotting]
   - [NumPy](https://numpy.org) [**Optional.** In my case, just `fig3` used this library]
   - [Pillow](https://pillow.readthedocs.io) [**Optional.** I used this just for import the website favicon]
3. A little practice about
   - Some [Streamlit API](https://docs.streamlit.io/library/api-reference)
   - Some [Matplotlib Examples](https://matplotlib.org/stable/gallery/index.html) [Especially in pie, donut, and bar chart]

## **How to Start?**
### 1. Create Your Google Forms
There are two choices to create the forms:
- Create the form only with 1 word per each question (e.g. city, pet, etc.) and give a full questions in the description, or
- Create a normal form's questions (e.g. How old are you?, etc.)

In this project, I prefer to use the second one to make a pretty interface of the form and speed up form creation.
