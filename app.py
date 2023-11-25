import streamlit as st

positive_words = ["happy", "good", "excellent", "positive", "awesome"]
negative_words = ["sad", "bad", "terrible", "negative", "awful"]

def predict_sentiment(text):
    words = text.lower().split()
    positive_count = sum(word in positive_words for word in words)
    negative_count = sum(word in negative_words for word in words)

    if positive_count > negative_count:
        return "Positive"
    elif negative_count > positive_count:
        return "Negative"
    else:
        return "Neutral"

def main():
    st.title("Simple Sentiment Analysis App")

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


