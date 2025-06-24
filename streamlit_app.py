# Import python packages
import streamlit as st
from snowflake.snowpark.functions import col

# Write directly to the app
st.title(f":cup_with_straw: Customize Your Smoothie! :cup_with_straw:")
st.write(
  """Replace this example with your own code!
  **And if you're new to Streamlit,** check
  out our easy-to-follow guides at
  [docs.streamlit.io](https://docs.streamlit.io).
  """
)


name_on_order = st.text_input("Name of smoothie", 'enter name')
st.write(f"The name of your smoothie will be {name_on_order}")

cnx = st.connection("snowflake")
session = cnx.session()

df = session.table("SMOOTHIES.PUBLIC.fruit_options").select(col("FRUIT_NAME"))
#st.dataframe(df)

ingredients_list = st.multiselect(
    "multyselect name",
    df,
    max_selections = 5
)

result = ''
if ingredients_list:
    #st.text(ingredients_list)
    #st.write(ingredients_list)

    result = ' '.join(ingredients_list)

    my_insert_stmt = f"insert into smoothies.public.orders(ingredients, name_on_order) values ('{result}','{name_on_order}')"


    insert = st.button('ready')
    if insert:
        session.sql(my_insert_stmt).collect()
        st.success('Your Smoothie is ordered!', icon="✅")

st.write(result)
        


