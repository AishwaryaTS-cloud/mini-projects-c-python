import requests
from pywebio import start_server
from pywebio.output import put_html, put_markdown, put_image, style, clear, put_buttons
from pywebio.session import hold

def get_fun_fact(_=None):
    clear()

    # Fancy colorful heading
    put_markdown(
        "<h2 style='text-align:center; color:#ff6600;'>✨ Fun Fact Generator ✨</h2>",
        lstrip=True
    )
    put_image("https://img.icons8.com/emoji/96/000000/thinking-face.png").style("display:block; margin:auto;")

    url = "https://uselessfacts.jsph.pl/random.json?language=en"

    try:
        response = requests.get(url, timeout=5)
        data = response.json()
        useless_fact = data.get("text", "No fact found!")
    except Exception as e:
        useless_fact = f"⚠️ Could not fetch a fact. Error: {e}"

    # Styling fact inside a card-like view
    style(
        put_markdown(f"💡 **{useless_fact}**"),
        'color:#1e90ff; font-size:22px; text-align:center; margin:25px; background:#f0f8ff; padding:15px; border-radius:12px; box-shadow:2px 2px 10px #aaa;'
    )

    # Add a fun styled HTML section with emojis
    put_html('''
    <div style="
        margin:auto; 
        width:60%; 
        text-align:center; 
        border:2px solid #ff6600; 
        border-radius:12px; 
        padding:12px; 
        font-size:18px;
        background:#fffaf0;
        box-shadow: 2px 2px 8px #ddd;
    ">
        <p>😀 Learn something new today!</p>
        <p>🔥 Keep your curiosity alive!</p>
        <p>🚀 One fact at a time, sky is the limit!</p>
    </div>
    ''')

    # Proper PyWebIO button to refresh fact
    put_buttons(
        [dict(label='🔄 Another Fun Fact', value='refresh', color='success')],
        onclick=get_fun_fact
    )

def main():
    # Animated gradient background and styled page
    put_html('''
    <style>
        body {
            background: linear-gradient(270deg, #ff9a9e, #fad0c4, #a18cd1, #fbc2eb);
            background-size: 800% 800%;
            animation: gradientBG 15s ease infinite;
        }
        @keyframes gradientBG {
            0% {background-position:0% 50%;}
            50% {background-position:100% 50%;}
            100% {background-position:0% 50%;}
        }
        h1 {
            text-align: center;
            color: #ffffff;
            font-size: 3em;
            text-shadow: 2px 2px 8px #000000;
            animation: bounce 2s infinite;
        }
        @keyframes bounce {
            0%, 20%, 50%, 80%, 100% { transform: translateY(0); }
            40% { transform: translateY(-15px); }
            60% { transform: translateY(-7px); }
        }
        .info-text {
            text-align: center;
            font-size: 20px;
            color: #ffffff;
            margin: 20px;
        }
        .fun-button {
            display: block;
            margin: 30px auto;
            padding: 15px 30px;
            font-size: 20px;
            color: #fff;
            background: #ff6600;
            border: none;
            border-radius: 12px;
            cursor: pointer;
            box-shadow: 2px 2px 12px #444;
            transition: all 0.3s ease;
        }
        .fun-button:hover {
            transform: scale(1.1);
            background: #ff8533;
        }
        @keyframes emojiBounce {
            0%, 100% { transform: translateY(0); }
            50% { transform: translateY(-10px); }
        }
        .emoji-div {
            text-align:center; 
            font-size:50px; 
            animation: emojiBounce 1.5s infinite;
        }
    </style>
    <h1>🎉 Welcome to the Fun Fact Zone 🎉</h1>
    <p class="info-text">Click the button below and discover random fun facts 🤩</p>
    <div class="emoji-div">😎 🚀 🌟</div>
    ''')

    # Use PyWebIO button instead of raw HTML
    put_buttons(
        [dict(label='✨ Show me a fact ✨', value='start', color='primary')],
        onclick=get_fun_fact
    )

    hold()

if __name__ == '__main__':
    start_server(main, port=8080, debug=True, cdn=False, auto_open_webbrowser=True)
