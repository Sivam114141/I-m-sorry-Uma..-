import streamlit as st
import time

# Page configuration
st.set_page_config(
    page_title="Dil Se Sorry...",
    page_icon="❤️",
    layout="centered"
)

# Custom Styling
st.markdown("""
    <style>
    .main {
        background-color: #FAFAFA;
    }
    .title-text {
        text-align: center;
        font-size: 2.2rem;
        font-weight: 700;
        color: #B22222;
        margin-bottom: 0.5rem;
    }
    .subtitle-text {
        text-align: center;
        font-size: 1.4rem;
        font-weight: 600;
        color: #4A4A4A;
        margin-bottom: 1.5rem;
    }
    .card {
        background: #FFFFFF;
        padding: 2rem;
        border-radius: 12px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.06);
        border: 1px solid #F0E6E6;
        margin-bottom: 1.5rem;
        line-height: 1.8;
        font-size: 1.05rem;
        color: #333333;
    }
    .trust-section {
        background: #FFF8F8;
        border-left: 4px solid #B22222;
        padding: 1.2rem;
        border-radius: 4px;
        margin-top: 1rem;
        margin-bottom: 1.5rem;
        font-size: 0.98rem;
        color: #555555;
    }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown('<div class="title-text">Dil Se Sorry...</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle-text">Meri jaan... ❤️</div>', unsafe_allow_html=True)

# Main Message Card
st.markdown("""
<div class="card">
    <p>Mujhe pata hai maine tumhe hurt kiya. Ye soch ke bohot bura lagta hai.</p>
    <p>Tum mere liye kitne special ho, words mein nahi bata sakta.</p>
    <p>Jo bhi hua, uska koi excuse nahi. Maine galti ki aur main accept karta hoon.</p>
    <p>Tumhari feelings matter karti hain mujhe. Bohot zyada.</p>
    <p>Main promise karta hoon agli baar se zyada careful rahunga.</p>
    <p>Tum mujhe itna pyaar dete ho, aur maine tumhe takleef di. I'm really sorry.</p>
    <p style="font-weight: 600; color: #B22222;">Please mujhe ek aur chance do?</p>
</div>
""", unsafe_allow_html=True)

# Trust Reflection Card
st.markdown("""
<div class="trust-section">
    <strong>Why your trust means everything to me:</strong><br>
    Trust takes time to build and just a moment to shake. I understand that words alone can't fix how you feel right now, but I want to earn back your confidence step by step. No deflecting, no excuses—just genuine effort and transparency moving forward.
</div>
""", unsafe_allow_html=True)

# Interactive Response Section
col1, col2 = st.columns(2)

with col1:
    if st.button("I need time, but I hear you"):
        st.info("Take all the time you need. I'm right here whenever you're ready to talk.")

with col2:
    if st.button("I forgive you ❤️"):
        st.balloons()
        st.success("Thank you for your grace. I promise to cherish and protect our trust.")
