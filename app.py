import streamlit as st
from transformers import pipeline

# Load pre-trained sentiment analysis model
classifier = pipeline("sentiment-analysis")

def predict_sentiment(text):
    result = classifier(text)
    return result[0]

def main():
    st.title("Sentiment Analysis App")

    # User input
    text_input = st.text_area("Enter text for sentiment analysis:")

    if st.button("Predict"):
        if text_input:
            prediction = predict_sentiment(text_input)
            st.write(f"Sentiment: {prediction['label']} with confidence: {prediction['score']:.4f}")
        else:
            st.warning("Please enter some text.")

if __name__ == "__main__":
    main()




