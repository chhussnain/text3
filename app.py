import streamlit as st
from transformers import pipeline

# Load pre-trained text classification model from Hugging Face
classifier = pipeline("sentiment-analysis")

def predict_sentiment(text):
    result = classifier(text)
    return result[0]

def main():
    st.title("Text Classification App")

    # User input
    text_input = st.text_area("Enter text for classification:")

    if st.button("Predict"):
        if text_input:
            prediction = predict_sentiment(text_input)
            st.write(f"Prediction: {prediction['label']} with confidence: {prediction['score']:.4f}")
        else:
            st.warning("Please enter some text.")

if __name__ == "__main__":
    main()
