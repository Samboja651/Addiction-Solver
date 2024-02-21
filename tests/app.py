from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('nav.html')


if __name__ == '__main__':
    app.run(debug=True, port=5000)