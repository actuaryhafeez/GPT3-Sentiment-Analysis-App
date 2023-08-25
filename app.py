import streamlit as st
import openai

# Set your OpenAI API key here
openai.api_key = st.secrets["OPENAI_API_KEY"]  # Use st.secrets to access environment variables

# Streamlit app title
st.title("Sentiment Analysis App")

# Input text from user
user_input = st.text_area("Enter text for sentiment analysis")

# Perform sentiment analysis when user submits input
if st.button("Analyze Sentiment"):
    if user_input:
        # Call OpenAI API for sentiment analysis
        prompt = f"Given the text '{user_input}', provide a response from the following sentiment options: positive, negative, neutral."
        response = openai.Completion.create(
            engine="text-davinci-003",  # You can experiment with different engines
            prompt=prompt,
            max_tokens=50,
        )
        
        # Get the sentiment response
        sentiment_response = response.choices[0].text.strip()
        
        # Display sentiment response
        st.write(f"Generated Sentiment: {sentiment_response}")
        

    else:
        st.write("Please enter some text to analyze sentiment.")
