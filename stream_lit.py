import streamlit
streamlit.title('My Streamlit App')
streamlit.header('How to build Stram Lit Apps ?')
streamlit.text('1. Sign into Stream Lit account through GitHub')

streamlit.header('Breakfast Menu')
streamlit.text('1.😀Omega 3 & Blueberry Oatmeal')
streamlit.text('2.😄Kale, Spinach & Rocket Smoothie')
streamlit.text('3.🎂Hard-Boiled Free-Range Egg')



import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
