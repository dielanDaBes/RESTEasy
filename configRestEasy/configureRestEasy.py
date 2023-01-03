from flask import request, render_template, Flask
import json
import os

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/submit")
def submit():
	with open('static/restEasy.conf', 'w') as outfile:
		json.dump(request.args, outfile)
	return render_template("success.html")

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
