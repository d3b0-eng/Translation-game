import streamlit as st
import random 
import pandas as pd
import json
from streamlit_lottie import st_lottie



st.set_page_config(layout='centered',
                   page_title='Learn French',
                   page_icon='🏫')


def load_csv():
    df = pd.read_csv('./assets/words.csv', sep=';', header=0, encoding='utf-8')
    return df 


numb_words = st.sidebar.text_input('How many words do you want to guess?')


def load_lottiefile(filepath):
    with open(filepath, "r") as f:
        return json.load(f)

def main_to_translate(main, translation, df, numb_words):
    st.session_state.main_list = []
    st.session_state.translation_list = []
    exclusion = []
    for words in range(numb_words):
        rand_index = random.choice([i for i in range(len(df)-1) if i not in exclusion])
        main_word, translation_word = df.loc[rand_index, [f'{main}', f'{translation}']]
        exclusion.append(rand_index)
        st.session_state.main_list.append(main_word)
        st.session_state.translation_list.append(translation_word)

    return st.session_state.main_list, st.session_state.translation_list 


def data_creation():
    dataframe = pd.DataFrame({df.columns[0]:st.session_state.main_list,
                        df.columns[1]:st.session_state.translation_list})
    dataframe['French'] = dataframe['French'].apply(lambda x: x.lower() if isinstance(x, str) else x)
    game_modes = [f'{df.columns[0]} to {df.columns[1]}',
            f'{df.columns[1]} to {df.columns[0]}']
    choice = st.selectbox('Select game mode', game_modes)

    main_language = choice.split(' ', 1)[0]
    translation_language = choice.split(' ')[-1]    
    selected_gamemode = [main_language, translation_language]

    if selected_gamemode != dataframe.columns.tolist():
        dataframe = dataframe.reindex(columns=selected_gamemode)

    return dataframe, main_language, translation_language

    

def game(number):
    try:
        if st.session_state.current_index <= int(number):
            with st.expander('Expand to see the words'):
                st.dataframe(dataframe)

            if 'translated' not in st.session_state:
                st.session_state.translated = []

            col1, col2 = st.columns(2)
            col3, col4 = st.columns(2)
            if col1.button('Next word', key='next'):
                st.session_state.current_index += 1

            col3.metric('Word to translate', 
                    dataframe.loc[st.session_state.current_index, main])
            st.session_state.translated = col4.text_input('Translate')

            if col2.button('Check', key='check_button'):
                if st.session_state.translated == dataframe.loc[st.session_state.current_index, translation]:
                    col4.write('**Correct!**')
                    st.session_state.score += 1
                else:
                    col4.write('**Wrong!**')
                
            col3.metric('Score:', st.session_state.score)

        else:
            st.stop()

    except Exception as e:
        # st.write(f'error: {e}')
        st.write('**You have finished your words!**')
        st.metric('Your final score is', st.session_state.score)



def progress_bar():
    counter = round(st.session_state.current_index * 100/len(dataframe))
    if counter > 100:
        counter = 100
    st.progress(counter, 'Progress')


col1, col2 = st.columns((0.5, 2))
lottie_animation = load_lottiefile('./assets/translation.json')
with col1:
    st_lottie(lottie_animation,
              speed=0.5,
              height=100,
              width=100)
col2.title('Learn French web-app')



try:
    df = load_csv()

    if 'score' not in st.session_state:
        st.session_state.score = 0

    if 'main_list' and 'translation_list' not in st.session_state:
        st.session_state.main_list, st.session_state.translation_list = main_to_translate(df.columns[0], df.columns[1], df, int(numb_words))
    
    if 'current_index' not in st.session_state:
        st.session_state.current_index = 0

    dataframe, main, translation = data_creation()
    game(numb_words)
    progress_bar()

except ValueError:
    st.write('Insert a number')
    empty_animation = load_lottiefile('./assets/empty.json')
    st_lottie(empty_animation)


if st.sidebar.checkbox('Show whole dataframe'):
    st.dataframe(df)
