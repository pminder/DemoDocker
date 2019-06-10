import socket

from flask import Flask, request
from textblob import TextBlob


VERSION = "2.0"
app = Flask(__name__)


def get_polarity(text):
    return TextBlob(text).sentiment.polarity


def compute_feedback_answer(polarity):
    if polarity == 0:
        return "Thank you for this interesting feedback\n"
    elif polarity > 0:
        return 'Thank you for your positive feedback!\n'
    return "Sorry to hear that... What can I do to improve myself ?\n"


@app.route("/")
def hello():
    return "Welcome to this demo :D"


@app.route("/analyze")
def analyze_sentiment():
    text = request.args.get("sentence")
    polarity = get_polarity(text)
    html = "<h1>Feedback analyzer</h1>" \
           "<h3>{answer}</h3>" \
           "<b>Polarity:</b> {polarity}<br/>" \
           "<b>Hostname:</b> {hostname}<br/>" \
           "<b>Version:</b> {version}<br/>"
    html = html.format(
        answer=compute_feedback_answer(polarity),
        polarity=polarity,
        hostname=socket.gethostname(),
        version=VERSION
    )
    return html


if __name__ == '__main__':
    app.run(host="0.0.0.0")
