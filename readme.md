# **Google Form Data Visualization**
This project built using Streamlit -- a web-based front-end for Python. In this project, you can display your public Google Forms's responds with many types of chart, and the best one is you can fully control which data you want to display in your Streamlit app.

## **My App**
- Google Forms: https://docs.google.com/forms/d/e/1FAIpQLSdz4jIkzSr6-adQfuZhkh86gHMyk72wUDWSVJiR_sRsZ_53BA/viewform
- Visualization: https://share.streamlit.io/tudemaha/forms-streamlit/main/forms-streamlit.py

Feel free to fill the anonymous form and visit the visualization website.

## **Requirements**
1. Programming Language
   - [Python](https://www.python.org)
2. Python Libraries
   - [Streamlit](https://streamlit.io) [The main library]
   - [gsheetsdb](https://github.com/betodealmeida/gsheets-db-api) [Used to connecting Google Sheets with Streamlit. (It's now replaced by shillelagh, but you still can use it.)]
   - [Matplotlib](https://matplotlib.org) [For chart plotting]
   - [NumPy](https://numpy.org) [**Optional.** In my case, just `fig3` used this library]
   - [Pillow](https://pillow.readthedocs.io) [**Optional.** I used this just for import the website's favicon]
3. A little practice about
   - Some [Streamlit API](https://docs.streamlit.io/library/api-reference) [take a look on my [source code](/forms-streamlit.py) for the APIs I used]
   - Some [Matplotlib Examples](https://matplotlib.org/stable/gallery/index.html) [In this project: pie, donut, and bar chart]
4. Google's services
   - [Google Forms](https://forms.google.com)
   - [Google Sheets](https://sheets.google.com)

## **How to Start?**
### **1. Create Your Google Forms**
Create a Google Forms in a folder. There are two options to create the form:
- Create the form with only one word per question (e.g. city, age, etc.) and give a full questions in the description, or
- Create a normal form's questions (e.g. How old are you?, etc.)

In this project, I prefer to use the second one to make a pretty interface of the form and speed up form creation. This is my example form:

![Form Creation](/../assets/form_creation.jpg)

### **2. Creating Spreadsheets**
There are also two options to create the spreadsheets following the previous step:
- for the first option: only use the connected Google Forms's spreadsheet, or
- for the second option: use the connected Google Form's spreadsheet and make a new spreadsheet.

#### **Global Step**
- Go to `Answer` (id=Jawaban) tab in the pre-built Google Forms
- Click on the `Google Sheets` button to make a connected Spreadsheet
![Connecting Sheets](/../assets/connecting_sheets.jpg)

#### **Continue for the first option**
- Change your connected Google Sheet availability to public
  - Click on `Share` (id=Bagikan) button at the top right
  - Turn on link sharing for `Anyone with the link` (id=Siapa saja yang memiliki link) with `viewer` access (id=Pengakses lihat-saja).
![Change Availability](/../assets/change_availability.jpg)

#### **Continue for the second option**
- Go to your project folder in Drive
- Create a new blank Google Sheet (choose your own name)
- Make one word table header following on your connected Google Sheets header starting from cell `A1` (e.g. in your connected Google Sheets header is "How old are you?", just make "age" header for your new Google Sheets)
- In cell `A2`, use `=IMPORTRANGE()` formula to import the data from the connected Google Sheets
  - Import data from cell `A2` (`A1` if you want to include the timeline) until your last data
  - **Important: prepare your last data in formula and new spreadsheet up to 500 rows or more**
- Change your new Google Sheet availability to public
  - Click on `Share` (id=Bagikan) button at the top right
  - Turn on link sharing for `Anyone with the link` (id=Siapa saja yang memiliki link) with `viewer` access (id=Pengakses lihat-saja).
![Change Availability](/../assets/change_availability.jpg)

### **3. Creating Streamlit Front-End**
To create the front-end of this app, take a little research in:
- Streamlit's official docs about [Connect Streamlit to a public Google Sheet](https://docs.streamlit.io/knowledge-base/tutorials/databases/public-gsheet).
- "A little practice about" that I mentioned on [Requirements](#requirements) section above.
- [My source code](/forms-streamlit.py)

### **4. Instantly Deploy Your App**
It's a simple way to deploy your app using Streamlit's free deployment service (https://share.streamlit.io). Just sign up using your email or connect  your GitHub account to Streamlit and paste your GitHub repo link of your app.

> Remember to put your `secrets` while deploying your app!

Read Streamlit's official docs about [Deploy an app](https://docs.streamlit.io/streamlit-cloud/get-started/deploy-an-app) for more information.

## **At the End...**
Congratulation on your new Streamlit app :tada: