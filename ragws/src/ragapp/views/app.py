#create ui page using streamlit for food delivery policy
import streamlit as st
from ragapp.utils.rag_engine import receive_prompt
#to run 
# streamlit run src/ragapp/views/app.py

#design the ui page layout
st.set_page_config(
    page_title="Food Delivery Policy Assistant",    
    page_icon="🍔",
    layout="wide",
    
)

#set css style for the page
#title color should be radial gradient from red to orange
#background color for the page multicolor radial gradient from light blue to dark blue
#apply main page css class to the whole page
st.markdown(
    """
    <style>
    /* Remove Streamlit top white header */
    [data-testid="stHeader"] {
        background: transparent;
        height: 0rem;
    }

    /* Hide toolbar/deploy/menu */
    [data-testid="stToolbar"] {
        display: none;
    }

    /* Full page background */
    .stApp {
        background: linear-gradient(
            120deg,
            #ff9a9e 0%,
            #fad0c4 25%,
            #a8e6a1 60%,
            #dcedc1 100%
        );
        min-height: 100vh;
    }

    /* Remove top spacing */
    .block-container {
        padding-top: 1rem;
    }
    
    .stTitle{
        background: radial-gradient(circle, blue, red, orange, yellow, green);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 48px;
        font-weight: bold;
        text-align: center;
    }
    .stWelcome{
       color: blue;
       background: radial-gradient(circle, lightblue, darkblue);
       -webkit-background-clip: text;
       -webkit-text-fill-color: transparent;
       font-size: 48px;
       font-weight: bold;
       text-align: center;
    }
     .stAnswer{
        background: radial-gradient(circle, lightgreen, darkgreen);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 20px;
        font-weight: bold;
        text-align: center;
    }
     .stQuestion{
        background: radial-gradient(circle, lightcoral, darkred);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 20px;
        font-weight: bold;
        text-align: center;
    }
    .stTextBox{
         display: flex; 
         justify-content: center; 
         margin-top: 20px;
         border-radius: 20px;
         background: rgba(255, 255, 255, 0.8); /*
    }
    </style>
    """,
    unsafe_allow_html=True
)
#apply main page css class to the whole page

#add title and description
st.markdown('<h1 class="stTitle">Food Delivery Policy Assistant</h1>', unsafe_allow_html=True)
#Welcome message with h2 tag and center aligned
st.markdown(
    """
    <h2 class="stWelcome">Welcome to the Food Delivery Policy Assistant!</h2>
    """,
    unsafe_allow_html=True
)


#create input text box for user question
st.markdown(
    """
    <div class="stTextBox">
        <input type="text" id="question_input" placeholder="Ask a question about the Food Delivery Policy..." style="width: 50%; padding: 10px; font-size: 16px; border-radius: 5px; border: 1px solid #ccc;">
    </div>
    """,
    unsafe_allow_html=True
)

