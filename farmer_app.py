import streamlit as st
from murf import Murf
from deep_translator import GoogleTranslator
import requests
import os
# ----------------------------
# Gradient Background CSS
# ----------------------------
st.markdown(
    """
    <style>
    /* Main app container */
    .stApp {
        background: linear-gradient(135deg, #a8e6cf, #dcedc1, #ffd3b6, #ffaaa5);
        background-size: 400% 400%;
        animation: gradientBG 15s ease infinite;
    }

    @keyframes gradientBG {
        0% {background-position:0% 50%;}
        50% {background-position:100% 50%;}
        100% {background-position:0% 50%;}
    }

    /* Buttons styling */
    .stButton>button {
        background-color: #ff8b94;
        color: white;
        font-weight: bold;
        border-radius: 12px;
        padding: 10px 20px;
    }

    /* Text input styling */
    .stTextInput>div>div>input {
        border-radius: 10px;
        border: 2px solid #ffd3b6;
        padding: 10px;
    }

    h1, h2, h3 {
        color: #333333;
        font-family: "Comic Sans MS", cursive, sans-serif;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ----------------------------
# Configuration
# ----------------------------
MURF_API_KEY = "ap2_68eee5be-e0e1-447b-86bd-99bcd677b408"
VOICE_ID = "en-US-natalie"
AUDIO_FILE = "response.mp3"

client = Murf(api_key=MURF_API_KEY)

# ----------------------------
# Streamlit UI
# ----------------------------
st.set_page_config(page_title="🌾 Farmer Voice Assistant", page_icon="🌱", layout="centered")
st.markdown("""
<style>
body { background-color: #f0f8ff; }
h1 { color: #2e8b57; text-align: center; }
.stButton>button { background-color: #32cd32; color: white; font-weight: bold; }
</style>
""", unsafe_allow_html=True)

st.title("🌾 Farmer Voice Assistant")
st.write("Ask any farming question and get a **voice response**! 🎤🌱")

language = st.selectbox("🌐 Choose your language:", ["English", "Hindi", "Spanish", "French", "Bengali", "Tamil"])
user_question = st.text_input("❓ Enter your question here:")

if st.button("Ask"):
    if user_question.strip() == "":
        st.warning("⚠️ Please enter a question first.")
    else:
        # Basic farming knowledge logic
        if "weather" in user_question.lower():
            response_text = "🌤️ The weather looks good today for planting crops."
        elif "fertilizer" in user_question.lower():
            response_text = "🧪 Use nitrogen-based fertilizer for better crop growth."
        elif "market" in user_question.lower():
            response_text = "💰 Wheat price is around 2200 rupees per quintal today."
        else:
            response_text = f"You asked: {user_question}. Always check local farming guidelines."

        # Translate if needed
        if language != "English":
            try:
                response_text = GoogleTranslator(source='auto', target=language.lower()).translate(response_text)
            except Exception as e:
                st.warning(f"⚠️ Translation failed, using English text. ({e})")

        # Generate TTS
        try:
            response = client.text_to_speech.generate(
                text=response_text,
                voice_id=VOICE_ID,
                format="MP3"
            )

            # Download audio from the Murf response URL
            audio_url = response.audio_file  # it's a URL
            audio_data = requests.get(audio_url).content
            with open(AUDIO_FILE, "wb") as f:
                f.write(audio_data)

            st.success("✅ Response generated! Listen below 👇")
            st.audio(AUDIO_FILE)
            st.markdown(f"**Response Text:** {response_text} 🎧")

        except Exception as e:
            st.error(f"❌ Failed to generate speech: {e}")
