import streamlit as st
from streamlit.elements.image import image_to_url
from streamlit.proto.Button_pb2 import Button
from config import *
from model_helper import load
from textblob import TextBlob
from db import prediction
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


st.sidebar.write(DEVELOPER)

def opendb():
    engine = create_engine('sqlite:///db.sqlite3') # connect
    Session =  sessionmaker(bind=engine)
    return Session()
def save_results(data,sentiment):
    sess = opendb()
    obj = prediction(comment=data,result=sentiment)
    sess.add(obj)
    sess.commit()
    sess.close()
choice = st.sidebar.radio("Select Options",MENU_OPTIONS)

if choice=='About Project':
    st.title(PROJECT_NAME)
    st.image("s.png")
    st.header("About project")
    st.success('''Sentiment Analysis is Natural Language Processing task which deals with automated extraction of subjective content from digital text and predicting their subjectivity such as Positive , Negative and Neutral.
''')
    
if choice=='Instruction':
    st.title("How to use Application")
    st.success("1️⃣Select Sentiment Analysis option.")
    st.success("2️⃣Fill the Hindi content in the text box.")
    st.success("3️⃣Click on Get Sentiment Analysis for sentiment result")
    st.success("4️⃣You can check your records from View Record.")






if choice=='Sentiment Analysis':
    st.subheader("Please fill content in box below👇")
    data = st.text_area("Your content here")
    btn = st.button('Get Sentiment analysis')
    if btn and data:
        cl = load()

        blob = TextBlob(data,classifier=cl)
        st.write([np for np in blob.noun_phrases])
        st.write(blob.classify())
        save_results(data,blob.classify())
        st.success("sentiment saved")
if choice=='View Records':
    st.header("View Records")
    db = opendb()
    results = db.query(prediction).all()
    db.close()
    record = st.selectbox("select a sentiment Record",results)
    if record:
        st.write(record.comment)
        st.write(record.result)
        st.write(record.created_on)
    