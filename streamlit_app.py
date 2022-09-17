import streamlit

streamlit.title('My Parents New Healthy Diner') 

streamlit.header('Breakfast Menu')
streamlit.text('🥣Omega 3 & Blueberry Oatmeal') 
streamlit.text('🥗Kale, Spinach & Rocket Smoothie') 
streamlit.text('🐔Hard-Boiled Free-Range Egg') 
streamlit.text('🥑🍞 Avocado Toast') 

streamlit.header('🍌🍓 Build your own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')
my_fruit_list = my_fruit_list.set_index('Fruit')

streamlit.multiselect("pick some fruits:" , list(my_fruit_list.index))
streamlit.dataframe(my_fruit_list)

fruits_selected = streamlit.multiselect("pick some fruits:" , list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show) 

#create the repeatable code block (called a function) 
def get_fruityvice_data(this_fruit_choice):
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + this_fruit_choice)
    fruityvice_normalized = pandas.json_normalize(fruityvice_response.json()) 
    return fruityvice_normalized

#New section to display fruity vice API response
streamlit.header('Fruityvice Fruit Advice!') 
try:
   fruit_choice = streamlit.text_input('What fruit would you like information about?') 
   if not fruit_choice:
        streamlit.error("Please select a fruit to get information.") 
   else:
       back_from_function = get_fruityvice_data(fruit_choice) 
       streamlit.dataframe(back_from_function) 

