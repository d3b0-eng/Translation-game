import pandas as pd
import streamlit as st
from nav import navbar


st.set_page_config(page_title='Add words', 
                   page_icon='➕')
st.title('Add a new word')


# load the data
df = pd.read_csv('./assets/words.csv', header=0, sep=";", encoding='utf-8')
df['French'] = df['French'].apply(lambda x: x.lower() if isinstance(x, str) else x)
df['Italian'] = df['Italian'].apply(lambda x: x.lower() if isinstance(x, str) else x)
df = df.dropna()
df = df.reset_index(drop=True)

# add a new word with its translation to the dataframe
add_new_word = st.checkbox('Add new word', value=False)

french_list = []
if add_new_word:
    french = st.text_input('Enter the French word: ').lower()
    if df['French'].str.contains(french).any():
            st.write(f'**{french}** already present in the dataset')
    else:
        italian = st.text_input(f'Enter the Italian translation of **{french}**: ')
        new_word = [french, italian]
        new_word = pd.DataFrame({'French': [new_word[0]], 'Italian': [new_word[1]]})
        df = pd.concat([df, new_word], ignore_index=True, axis=0)


# save the new dataframe in csv file
if st.button('Save changes'):
    df.to_csv('./assets/words.csv', sep=";", index=False, encoding='utf-8')
    st.success('Data addedd successfully')
    st.cache_data.clear()

st.write('These are the words available for now')
st.dataframe(df, width=800, height=500)

