import streamlit as st
from transformers import pipeline

# Optional: Load models once
transformer = pipeline("sentiment-analysis")

# Sentiment functions
def rule_based_sentiment(text):
    lexicon = {
        "good": 1, "great": 2, "excellent": 3,
        "bad": -2, "poor": -3, "terrible": -5
    }
    score = sum([lexicon.get(word, 0) for word in text.lower().split()])
    return "positive" if score > 0 else "negative"

def transformer_sentiment(text):
    result = transformer(text)[0]["label"]
    return "positive" if result == "POSITIVE" else "negative"

# Streamlit interface
st.title("🎯 Sentiment Analyzer")
text = st.text_area("Enter your review:")

method = st.selectbox("Choose Sentiment Method", ["Rule-Based", "Transformer"])

if st.button("Analyze"):
    if method == "Rule-Based":
        result = rule_based_sentiment(text)
    elif method == "Transformer":
        result = transformer_sentiment(text)
    else:
        print("This button is broken!")

    st.write(f"🧠 Sentiment: **{result.upper()}**")