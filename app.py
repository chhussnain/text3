import streamlit as st
from textblob import TextBlob

def predict_sentiment(text):
    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity

    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"

def main():
    st.title("Sentiment Analysis App")

    # User input
    text_input = st.text_area("Enter text for sentiment analysis:")

    if st.button("Predict"):
        if text_input:
            prediction = predict_sentiment(text_input)
            st.write(f"Sentiment: {prediction}")
        else:
            st.warning("Please enter some text.")

if __name__ == "__main__":
    main()



