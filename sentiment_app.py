
import streamlit as st
from transformers import pipeline

# Title
st.title("🧠 Sentiment Analysis Web App")
st.write("Analyze the sentiment of any text using NLP and Hugging Face Transformers.")

st.divider()

# Input box
user_input = st.text_area("Enter text to analyze:", placeholder="Type something here...")

if st.button("Analyze Sentiment"):
    if user_input.strip() == "":
        st.warning("Please enter some text!")
    else:
        # Load pre-trained sentiment analysis model
        sentiment_pipeline = pipeline("sentiment-analysis")

        # Run sentiment prediction
        result = sentiment_pipeline(user_input)[0]

        # Display results
        st.success(f"**Label:** {result['label']}")
        st.info(f"**Confidence Score:** {result['score']:.2f}")

        # Add emojis for better UX
        if result['label'].lower() == "positive":
            st.markdown("😄 The sentiment is **Positive!**")
        elif result['label'].lower() == "negative":
            st.markdown("😞 The sentiment is **Negative.**")
        else:
            st.markdown("😐 The sentiment is **Neutral.**")

st.divider()
st.caption("Made with ❤️ using Streamlit & Hugging Face Transformers")
