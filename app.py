from flask import Flask, render_template, request
from waitress import serve
app = Flask(__name__)

notes = []
@app.route('/', methods=["POST"])
def index():
    note = request.args.get("note")
    notes.append(note)
    return render_template("home.html", notes=notes)


if __name__ == '__main__':

    serve(app, host="0.0.0.0", port=50100,threads=1)
