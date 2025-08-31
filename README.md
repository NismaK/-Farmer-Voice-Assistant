<!DOCTYPE html>
<html lang="en">

<header>
    <h1>🌾 Farmer Voice Assistant</h1>
    <p>Voice-enabled interactive assistant for farmers</p>
</header>

<section>
    <h2>🎯 Features</h2>
    <ul>
        <li>Voice Responses using Murf TTS 🎤</li>
        <li>Interactive, emoji-filled UI 🌟</li>
        <li>Multilingual support via Deep Translator 🌐</li>
        <li>Smart farming tips for weather, fertilizers, and market prices 🧪💰</li>
        <li>Simple text input and Ask button for easy queries ✍️</li>
    </ul>
</section>

<section>
    <h2>💻 Tech Stack</h2>
    <table>
        <tr><th>Component</th><th>Technology</th></tr>
        <tr><td>Frontend</td><td>Streamlit</td></tr>
        <tr><td>Backend</td><td>Python</td></tr>
        <tr><td>Text-to-Speech</td><td>Murf API</td></tr>
        <tr><td>Translation</td><td>Deep Translator</td></tr>
        <tr><td>Audio Playback</td><td>Streamlit <code>st.audio()</code></td></tr>
    </table>
</section>

<section>
    <h2>🚀 Installation & Setup</h2>
    <ol>
        <li>Clone the repository:<br>
            <code>git clone https://github.com/yourusername/farmer-voice-assistant.git</code>
        </li>
        <li>Create a virtual environment (optional):<br>
            <code>python -m venv venv</code><br>
            <code>source venv/bin/activate  # Linux/Mac</code><br>
            <code>venv\Scripts\activate   # Windows</code>
        </li>
        <li>Install dependencies:<br>
            <code>pip install streamlit murf deep-translator requests</code>
        </li>
        <li>Set your Murf API Key in <code>farmer_app.py</code></li>
    </ol>
</section>

<section>
    <h2>🖥️ Run the App</h2>
    <pre>
streamlit run farmer_app.py
    </pre>
    <p>Open the URL displayed in the terminal (usually <code>http://localhost:8501</code>), type your question, and click <strong>Ask</strong>.</p>
</section>

<section>
    <h2>📸 Sample Questions</h2>
    <ul>
        <li>“What is the weather today?” 🌤️</li>
        <li>“Which fertilizer should I use for wheat?” 🧪</li>
        <li>“Current wheat market price?” 💰</li>
        <li>Any other general farming question 🤔</li>
    </ul>
</section>

<section>
    <h2>📂 Project Structure</h2>
    <pre>
farmer-voice-assistant/
│
├─ farmer_app.py          # Main Streamlit app
├─ response.mp3           # Generated audio responses
├─ README.html
└─ requirements.txt       # Dependencies
    </pre>
</section>

<section>
    <h2>⚡ Future Enhancements</h2>
    <ul>
        <li>Voice input for questions 🎙️</li>
        <li>Full multilingual support 🌍</li>
        <li>AI-powered dynamic answers using GPT models 🤖</li>
        <li>Mobile-friendly interface 📱</li>
    </ul>
</section>

<section>
    <h2>🔗 References</h2>
    <ul>
        <li><a href="https://murf.ai/api/docs/" target="_blank">Murf API Docs</a></li>
        <li><a href="https://github.com/nidhaloff/deep-translator" target="_blank">Deep Translator</a></li>
        <li><a href="https://streamlit.io/" target="_blank">Streamlit</a></li>
    </ul>
</section>

</body>
</html>
