import streamlit

streamlit.title('My Parents New Healthy Diner') 

streamlit.header('Breakfast Menu')
streamlit.text('๐ฅฃOmega 3 & Blueberry Oatmeal') 
streamlit.text('๐ฅKale, Spinach & Rocket Smoothie') 
streamlit.text('๐Hard-Boiled Free-Range Egg') 
streamlit.text('๐ฅ๐ Avocado Toast') 

streamlit.header('๐๐ Build your own Fruit Smoothie ๐ฅ๐')

import pandas
my_fruit_list = pandas.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')
my_fruit_list = my_fruit_list.set_index('Fruit')

streamlit.multiselect("pick some fruits:" , list(my_fruit_list.index))
streamlit.dataframe(my_fruit_list)

fruits_selected = streamlit.multiselect("pick some fruits:" , list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)
