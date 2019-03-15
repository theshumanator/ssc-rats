import os

from flask import Flask, render_template
app = Flask(__name__, template_folder='testflask/templates')

@app.route("/")
def home():
    return render_template("/home.html")
@app.route("/salvador")
def salvador():
    return "Hello, Salvador"
@app.route("/about")
def about():
    return render_template("about.html")
if __name__ == "__main__":
    #app.run(debug=True)
    port = int(os.environ.get('PORT', 5000))
    #port = os.getenv('PORT', default=8000)
    #updater.start_webhook(port=port)
    app.run(host='0.0.0.0', port=port)