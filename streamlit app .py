import streamlit as st
import random

# Page Header
st.set_page_config(page_title="UNSCRIPTED LEGENDS", page_icon="🎬")
st.title("🎬 UNSCRIPTED LEGENDS")
st.subheader("YouTube Video Idea & Hook Generator")
st.write("Generate high-performing, dramatic video concepts in seconds.")

st.divider()

# Input Options
user_subject = st.text_input("Enter a celebrity or athlete (leave blank for random):").strip()

# Data Pools
subjects = [
    "Sylvester Stallone", "Michael Jordan", "Jackie Chan", 
    "Mike Tyson", "Tom Cruise", "Serena Williams", 
    "Keanu Reeves", "Arnold Schwarzenegger", "Cristiano Ronaldo"
]

scenarios = [
    "surviving a near-death experience on set.",
    "losing millions of dollars in a secret bet.",
    "playing a championship game with a hidden injury.",
    "getting blacklisted early in their career.",
    "getting into a real-life fight with their biggest rival.",
    "rejecting a $100M contract out of pure respect."
]

thumbnail_texts = [
    "HE FINALLY CONFESSED!",
    "THE SECRET THEY HID...",
    "WHAT REALLY HAPPENED",
    "CAREER OVER?",
    "THE NO-RETURN POINT"
]

formats = [
    "YouTube Short (60 Seconds)", 
    "Standard Video (8 - 10 Minutes)", 
    "Mini-Documentary (12 - 15 Minutes)"
]

# Generate Button
if st.button("🚀 Generate Video Plan", type="primary"):
    sub = user_subject if user_subject else random.choice(subjects)
    scen = random.choice(scenarios)
    thumb = random.choice(thumbnail_texts)
    fmt = random.choice(formats)

    st.success("### 📌 Your Generated Production Plan")
    st.write(f"**Recommended Format:** {fmt}")
    st.write(f"**Video Topic:** How **{sub}** ended up {scen}")
    st.write(f"**Opening Hook:** *\"You think you know the full story of {sub}? Think again...\"*")
    st.write(f"**Thumbnail Text Idea:** `[{thumb}]` ")

st.divider()
st.caption("Powered by UNSCRIPTED LEGENDS | Built with Streamlit & Python")
