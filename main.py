import os

# from rats pkg, open amazons3 package and file connectWithS3, import function connectWithS3
from rats.AmazonS3.connectWithS3 import connectWithS3


from flask import Flask, render_template
app = Flask(__name__, template_folder='testflask/templates')

@app.route("/")
def home():
    #return render_template("/home.html")
    return connectWithS3()
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
    app.run(port=port);
    #app.run(host='0.0.0.0', port=port)