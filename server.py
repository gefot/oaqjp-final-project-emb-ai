"""
Flask web application for emotion detection using the EmotionDetection package.
This app provides a web interface and an API endpoint to analyze emotions in text.
"""

from flask import Flask, request, render_template
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector")
def emotion_detector_route():
    """
    Flask route to handle emotion detection requests.
    Accepts a query parameter 'textToAnalyze' and returns
    either the formatted emotion response or an error message
    if the input is invalid or empty.
    """
    text_to_analyze = request.args.get("textToAnalyze", "")

    result = emotion_detector(text_to_analyze)

    if result['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    response_text = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, 'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, 'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )

    return response_text


@app.route("/")
def index():
    """
    Renders the index.html file that contains the web interface
    for user input and emotion analysis display.
    """
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
