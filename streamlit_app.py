import streamlit

streamlit.title('My Parents New Healthy Diner')
streamlit.header('Breakfast Names')
streamlit.text('dosa')
streamlit.text('puri')
streamlit.text('bonda')



import pandas
my_fruit_list = pandas.read_csv(" https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
