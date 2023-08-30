from google_trans_new import google_translator
import streamlit as st
from googletrans import Translator
from io import StringIO
translator = google_translator()
translator_2 = Translator()
st.title("Language Translator")

dict={'english':'en','marathi':'mr','gujarati':'gu','punjabi':'pa','swedish':'sv','odia':'or','bengali':'bn','hindi':'hi'}

def changed_to():
    p=st.session_state.To
    ft = "Translate To.txt"
    with open(ft, "a", encoding="utf-8") as f:
         f.write(p)
         f.write("\n")

@st.cache
def saveData():
    fo = "history.txt"
    with open(fo, "a", encoding="utf-8") as f:
        f.write('{} | {} | {}'.format(Text, to,translate))
        f.write("\n")


to = st.selectbox(
     'Translate to:',
     ('english','marathi','gujarati','punjabi','swedish','odia','bengali','hindi'),key="To",on_change=changed_to)

for i in dict:
     if(i==to):
          str = dict[i]

Text = st.text_input("Enter a text")
translate = translator.translate(Text, lang_tgt=str)
st.write("Result of google_trans_new API ",translate)

translate_2=translator_2.translate(Text,dest=str)
st.write("Result of googletrans API ",translate_2.text)
saveData()

@st.cache
def translate_file():
    if uploaded_file is not None:
        stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
        for string in stringio:
            translate = translator.translate(string, lang_tgt=str)
            translate_2 = translator_2.translate(string, dest=str)
            string=string.strip()
            with open("translated_file.txt","a",encoding="utf-8") as f:
                f.write('{} | {} | {}'.format(translate, string, translate_2.text))
                f.write("\n")



uploaded_file = st.file_uploader("Choose a file")

translate_file()

if uploaded_file is not None:
    st.write("GOOGLE_TRANS_NEW | original | GOOGLETRANS")
    with open("translated_file.txt", "r", encoding='utf-8') as file1:
        for x in file1:
            st.write(x)




def Res_new():
    p=st.session_state.R_1
    ft = "record_new.txt"
    with open(ft, "a", encoding="utf-8") as f:
         f.write(p)
         f.write("\n")

def Res_trans():
    q=st.session_state.R_2
    ft = "record_trans.txt"
    with open(ft, "a", encoding="utf-8") as f:
         f.write(q)
         f.write("\n")

    open("translated_file.txt", 'w').close()


res_1 = st.radio(
     "Give accuracy for google_trans_new API result",
     ('0-40','40-60', '60-80', '80-100'),key="R_1",on_change=Res_new)

res_2 = st.radio(
     "Give accuracy for googletrans API result",
     ('0-40','40-60','60-80','80-100'),key="R_2",on_change=Res_trans)

