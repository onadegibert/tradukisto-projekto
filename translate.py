import streamlit as st
import sentencepiece as spm
import ctranslate2
from nltk import sent_tokenize
from nltk import word_tokenize

def load_models(option):
    if option == "Hispana-al-Esperanto":
        ct_model_path = "eseo_ctranslate2"
    elif option == "Esperanto-al-Hispana":
        ct_model_path = "eoes_ctranslate2"
    
    translator = ctranslate2.Translator(ct_model_path, "cpu")
    
    return translator

def translate(source, translator):
    """Use CTranslate model to translate a sentence

    Args:
        source (str): Source sentences to translate
        translator (object): Object of Translator, with the CTranslate2 model
        sp_source_model (object): Object of SentencePieceProcessor, with the SentencePiece source model
        sp_target_model (object): Object of SentencePieceProcessor, with the SentencePiece target model
    Returns:
        Translation of the source text
    """

    source_sentences = sent_tokenize(source)
    source_tokenized = [word_tokenize(sentence) for sentence in source_sentences]
    translations = translator.translate_batch(source_tokenized, replace_unknowns=True)
    translations = [translation[0]["tokens"] for translation in translations]
    translations_detokenized = [" ".join(translation) for translation in translations]
    translation = " ".join(translations_detokenized)

    return translation

# Title for the page and nice icon
st.set_page_config(page_title="Saluton!", page_icon="img/esperanto.png")
# Header
st.title("Tradukisto")

# Form to add your items
with st.form("my_form"):

    # Dropdown menu to select a language pair
    option = st.selectbox(
    "Elektu la adreson",
    ("Hispana-al-Esperanto", "Esperanto-al-Hispana"))
    #st.write('You selected:', option)

    # Textarea to type the source text.
    user_input = st.text_area("Teksto", max_chars=200)

    # Load models
    translator = load_models(option)
    
    # Translate with CTranslate2 model
    translation = translate(user_input, translator)

    # Create a button
    submitted = st.form_submit_button("Traduku")
    # If the button pressed, print the translation
    # Here, we use "st.info", but you can try "st.write", "st.code", or "st.success".
    if submitted:
        st.write("Traduko")
        st.info(translation)