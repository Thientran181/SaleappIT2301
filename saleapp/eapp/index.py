from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html', msg="chao mung ban thao den voi binh nguyen vo tan")

if __name__ == '__main__':
    with app.app_context():
        app.run(debug=True)
