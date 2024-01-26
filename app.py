from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def test_stories():
    return render_template('f_stories.html')

if __name__ == '__main__':
    app.run(debug=True)