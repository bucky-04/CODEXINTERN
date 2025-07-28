from flask import Flask, request, render_template_string
from textblob import TextBlob

app = Flask(__name__)

HTML = """
<!doctype html>
<title>Sentiment Analysis</title>
<h2>Enter your text below:</h2>
<form method="post">
  <textarea name="text" rows="6" cols="40"></textarea><br>
  <input type="submit">
</form>
{% if result %}
<h3>{{ result }}</h3>
{% endif %}
"""

@app.route("/", methods=["GET", "POST"])
def home():
    result = ""
    if request.method == "POST":
        text = request.form["text"]
        blob = TextBlob(text)
        polarity = blob.sentiment.polarity
        subjectivity = blob.sentiment.subjectivity
        if polarity > 0:
            sentiment = "Positive"
        elif polarity < 0:
            sentiment = "Negative"
        else:
            sentiment = "Neutral"
        result = f"Sentiment: {sentiment}, Polarity: {polarity:.2f}, Subjectivity: {subjectivity:.2f}"
    return render_template_string(HTML, result=result)

if __name__ == "__main__":
    app.run(debug=True)
