import requests
from pywebio import start_server
from pywebio.output import (
    put_html, put_text, style, put_buttons,
    clear, put_markdown, put_table, put_image
)
from pywebio.session import hold


def get_fun_fact(_):
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

    # Add a fun table with emojis
    put_table([
        ['😀', 'Learn something new today!'],
        ['🔥', 'Keep your curiosity alive!'],
        ['🚀', 'One fact at a time, sky is the limit!']
    ]).style("margin:auto; width:60%; text-align:center; border:2px solid #ff6600; border-radius:10px;")

    put_buttons(
        [dict(label='🔄 Another Fun Fact', value='refresh', color='success')],
        onclick=get_fun_fact
    )


def main():
    put_html(
        "<h1 style='text-align:center; color:#4CAF50;'>🎉 Welcome to the Fun Fact Zone 🎉</h1>"
    )
    put_image("https://img.icons8.com/fluency/96/000000/smiling-face.png").style("display:block; margin:auto;")

    put_markdown(
        "<p style='text-align:center; font-size:18px; color:#555;'>"
        "Click the button below and discover random fun facts 🤩"
        "</p>"
    )

    put_buttons(
        [dict(label='✨ Show me a fact ✨', value='start', color='info')],
        onclick=get_fun_fact
    )

    hold()


if __name__ == '__main__':
    start_server(main, port=8080, debug=True)
