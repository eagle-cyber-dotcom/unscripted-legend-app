
import streamlit as st
import random

# Page Header Configuration
st.set_page_config(page_title="UNSCRIPTED LEGENDS", page_icon="🎬")

st.title("🎬 UNSCRIPTED LEGENDS")
st.subheader("YouTube Video Idea & Full Script Generator")

st.divider()

# --- MONETIZATION: PAYWALL & PASSWORD SYSTEM ---
st.markdown("### 🔒 Creator Access")
st.write("Enter your Creator Password to unlock the full script generator.")

# Your working Paystack link
paystack_link = "https://paystack.shop/pay/dfmvjam8bn" 

st.markdown(f"**Don't have a password?** [👉 Click here to buy lifetime access]({paystack_link})")

# Password input box
password = st.text_input("Enter Access Password:", type="password")

# --- APP INTERFACE (LOCKED UNTIL PASSWORD IS ENTERED) ---
if password == "PRO-CREATOR":
    st.success("✅ Access Granted! Welcome to the Creator Suite.")
    st.divider()

    # User Input
    user_subject = st.text_input("Enter a celebrity or athlete (leave blank for random):").strip()

    # Data Pools
    subjects = ["Sylvester Stallone", "Michael Jordan", "Jackie Chan", "Mike Tyson", "Tom Cruise", "Serena Williams"]
    
    scenarios = [
        "surviving a near-death experience on set.",
        "losing millions of dollars in a secret bet.",
        "getting blacklisted early in their career.",
        "rejecting a $100M contract out of pure respect."
    ]

    thumbnail_texts = ["HE FINALLY CONFESSED!", "THE SECRET THEY HID...", "WHAT REALLY HAPPENED", "CAREER OVER?"]
    formats = ["YouTube Short (60 Seconds)", "TikTok (60 Seconds)", "Reel (60 Seconds)"]

    if st.button("🚀 Generate Full Video Script", type="primary"):
        sub = user_subject if user_subject else random.choice(subjects)
        scen = random.choice(scenarios)
        thumb = random.choice(thumbnail_texts)
        fmt = random.choice(formats)

        st.info("### 📌 Production Plan")
        st.write(f"**Recommended Format:** {fmt}")
        st.write(f"**Video Topic:** How **{sub}** ended up {scen}")
        st.write(f"**Thumbnail Text Idea:** `[{thumb}]` ")

        st.divider()
        
        # Script Generator
        st.success("### 📝 Full 3-Act Video Script")
        st.write(f"**[0:00 - 0:05] THE HOOK:** \n*\"You think you know the full story of {sub}? Think again...\"*")
        
        st.write(f"**[0:05 - 0:20] ACT 1: THE SETUP:** \n*\"At the peak of their career, the world thought they had it all figured out. But behind closed doors, a massive crisis was brewing that the media never talked about.\"*")
        
        st.write(f"**[0:20 - 0:45] ACT 2: THE CONFLICT:** \n*\"It all came crashing down when {sub} found themselves {scen} Friends turned their backs, the industry panicked, and it looked like there was no way out of this disaster.\"*")
        
        st.write(f"**[0:45 - 0:60] ACT 3: THE PAYOFF & OUTRO:** \n*\"But instead of giving up, they made a move nobody saw coming, cementing their legacy forever. If you want to know the exact details of how they pulled it off, hit subscribe and check out our deep dive video!\"*")

elif password != "":
    st.error("❌ Incorrect password. Please check your Paystack receipt or purchase access above.")

# --- FOOTER / BRANDING ---
st.divider()
st.caption("⚡ Powered by Unscripted Legends | All Rights Reserved" )
