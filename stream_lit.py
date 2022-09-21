import streamlit
import pandas
import snowflake.connector
import requests
from urllib.error import URLError
streamlit.title('My Streamlit App')
streamlit.header('How to build Stram Lit Apps ?')
streamlit.text('1. Sign into Stream Lit account through GitHub')

streamlit.header('Breakfast Menu')
streamlit.text('1.😀Omega 3 & Blueberry Oatmeal')
streamlit.text('2.😄Kale, Spinach & Rocket Smoothie')
streamlit.text('3.🎂Hard-Boiled Free-Range Egg')




my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
# Let's put a pick list here so they can pick the fruit they want to include 
my_fruit_list = my_fruit_list.set_index('Fruit')
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Apple','Grapes'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the table on the page.
streamlit.dataframe(fruits_to_show)

#New section to display FruityVice API Response
streamlit.header('Fruityvice Fruity Advice!')

fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered: ', fruit_choice)
import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)



# Take the normal json request to Normalise it
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# Output the screen as table
streamlit.dataframe(fruityvice_normalized)
#dont run past here while we troubleshoot
streamlit.stop()


my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * from fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.header("The Fruit Load List contains: ")
streamlit.dataframe(my_data_rows)

#Allow the end user to add a fruit to the list
fruit_choice = streamlit.text_input('What fruit would you like to add?','Kiwi')
streamlit.write('Thanks for adding: ', fruit_choice)


#Adding for now
my_cur.execute("insert into fruit_load_list values('for streamlit')");
