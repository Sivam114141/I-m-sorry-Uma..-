import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="For My Favorite Person ❤️",
    page_icon="🌹",
    layout="centered"
)

# Custom Styling
st.markdown("""
    <style>
    .stApp {
        background-color: #FAF6F6;
    }
    .main-header {
        text-align: center;
        font-size: 2.3rem;
        font-weight: 700;
        color: #A31D1D;
        margin-bottom: 0.2rem;
    }
    .sub-header {
        text-align: center;
        font-size: 1.2rem;
        font-weight: 500;
        color: #555555;
        margin-bottom: 1.5rem;
    }
    .card {
        background: #FFFFFF;
        padding: 2rem;
        border-radius: 16px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05);
        border: 1px solid #F0DCDC;
        margin-bottom: 1.5rem;
        line-height: 1.8;
        font-size: 1.05rem;
        color: #333333;
    }
    .highlight-box {
        background: #FFF0F0;
        border-left: 4px solid #A31D1D;
        padding: 1.2rem;
        border-radius: 8px;
        margin-top: 1rem;
        margin-bottom: 1.5rem;
        font-size: 1rem;
        color: #4A4A4A;
        line-height: 1.7;
    }
    .quote-style {
        font-style: italic;
        font-size: 1.15rem;
        color: #8B0000;
        text-align: center;
        padding: 1rem 0;
    }
    </style>
""", unsafe_allow_html=True)

# Header Section
st.markdown('<div class="main-header">For My Favorite Person ❤️</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">Please take a moment to read this...</div>', unsafe_allow_html=True)

# Tabs Navigation
tab1, tab2, tab3 = st.tabs(["💔 Dil Se Sorry", "✨ You Complete Me", "🎵 A Song For You"])

# TAB 1: Dil Se Sorry
with tab1:
    st.markdown("""
    <div class="card">
        <h3 style="color: #A31D1D; margin-top: 0;">Meri jaan...</h3>
        <p>Mujhe pata hai maine tumhe hurt kiya. Ye soch ke bohot bura lagta hai.</p>
        <p>Tum mere liye kitne special ho, words mein nahi bata sakta.</p>
        <p>Jo bhi hua, uska koi excuse nahi. Maine galti ki aur main accept karta hoon.</p>
        <p>Tumhari feelings matter karti hain mujhe. Bohot zyada.</p>
        <p>Main promise karta hoon agli baar se zyada careful rahunga.</p>
        <p>Tum mujhe itna pyaar dete ho, aur maine tumhe takleef di. I'm really sorry.</p>
        <p style="font-weight: 700; color: #A31D1D; font-size: 1.1rem;">Please mujhe ek aur chance do?</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="highlight-box">
        <strong>Why your trust means everything to me:</strong><br>
        Trust is the foundation of us. Breaking it, even for a moment, made me realize how delicate and valuable it is. I am not asking for instant forgiveness, but I am asking for the opportunity to prove to you through my actions, every single day, that you can count on me.
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        if st.button("I need some time ⏳"):
            st.info("I completely understand. Take all the time you need, I am right here waiting for you.")
    with col2:
        if st.button("I forgive you ❤️"):
            st.balloons()
            st.success("Thank you so much. I promise to cherish you and protect your trust forever.")

# TAB 2: You Complete Me
with tab2:
    st.markdown("""
    <div class="card">
        <h3 style="color: #A31D1D; margin-top: 0;">Why You Mean The World To Me</h3>
        <p>Before you came into my life, I never realized how much was missing. You brought warmth, peace, and genuine happiness into my world.</p>
        <p><strong>You complete me in ways I can't put into words:</strong></p>
        <ul>
            <li><strong>Your Kindness:</strong> The way you care and love unconditionally is something I treasure every single day.</li>
            <li><strong>Your Presence:</strong> Even on my hardest days, just talking to you makes everything feel alright.</li>
            <li><strong>My Safe Space:</strong> With you, I can be 100% myself without any fear or hesitation.</li>
        </ul>
        <div class="quote-style">
            "Without you, everything feels quiet and incomplete. You are my home."
        </div>
        <p>Seeing you hurt because of me breaks my heart, because my goal in life is to protect your smile, not take it away. I love you more than words can express.</p>
    </div>
    """, unsafe_allow_html=True)

# TAB 3: A Song For You
with tab3:
    st.markdown("""
    <div class="card" style="text-align: center;">
        <h3 style="color: #A31D1D; margin-top: 0;">A Melody Dedicated To You 🎶</h3>
        <p>Music expresses what words sometimes fail to say. Press play below and listen to this while reading...</p>
    </div>
    """, unsafe_allow_html=True)

    # Romantic Background Acoustic Track
    st.audio("https://cdn.pixabay.com/download/audio/2022/05/27/audio_1808fbf07a.mp3?filename=soft-piano-112677.mp3")

    st.markdown("""
    <div class="highlight-box" style="text-align: center;">
        <p style="font-size: 1.1rem; margin-bottom: 0.5rem;"><em>"Every beat of my heart reminds me of how much you mean to me."</em></p>
        <p style="margin-bottom: 0;">Thank you for being in my life. I hope we can move past this together, stronger than before.</p>
    </div>
    """, unsafe_allow_html=True)
