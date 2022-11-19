from flask import Flask
from flask import render_template
from flask import request
import pickle
import numpy as np


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload():
    calc = request.form["calc"]
    with open("predict_population.pickle", mode="rb") as fp:
        model = pickle.load(fp)
    txt = model.predict(np.array([[int(calc)]]))
    return render_template("upload.html", txt=txt)


if __name__ == "__main__":
    app.run(debug=True)
