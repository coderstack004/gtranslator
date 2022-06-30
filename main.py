# pip install pywebio googletrans==3.1.0a0

from pywebio import start_server
from pywebio.input import *
from pywebio.output import *
from googletrans import Translator

t = Translator()


def app():
    text = input("text: ")
    lang = input("language: ")

    result = t.translate(f"{text}", dest=f"{lang}").text

    put_html(f"<h1 style='color: red'>{result}</h1>")
if __name__ == "__main__":
    start_server(app, debug=True)
    