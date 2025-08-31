<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Farmer Voice Assistant</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(120deg, #d0f0c0, #f0e68c, #a0d8ef);
            margin: 0;
            padding: 0;
            color: #333;
        }
        header {
            background-color: #4caf50;
            color: white;
            padding: 20px;
            text-align: center;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }
        h1 {
            margin: 0;
            font-size: 2.5rem;
        }
        h2 {
            color: #2f4f4f;
        }
        section {
            padding: 20px 40px;
        }
        code {
            background-color: #f5f5f5;
            padding: 2px 6px;
            border-radius: 4px;
        }
        pre {
            background-color: #f5f5f5;
            padding: 10px;
            border-radius: 6px;
            overflow-x: auto;
        }
        table {
            border-collapse: collapse;
            width: 100%;
            margin-bottom: 20px;
        }
        table, th, td {
            border: 1px solid #888;
        }
        th, td {
            padding: 10px;
            text-align: left;
        }
        .emoji {
            font-size: 1.2rem;
        }
        a {
            color: #1e90ff;
            text-decoration: none;
        }
        a:hover {
            text-decoration: underline;
        }
    </style>
</head>
<body>

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
