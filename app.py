from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def test_stories():
    return render_template('f_stories.html')

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        addiction_type = request.form.get('addiction-type')
        duration = request.form.get('duration')
        cause = request.form.get('cause')
        severity = request.form.get('severity')
        age = request.form.get('age')
        gender = request.form.get('gender')

        if not (addiction_type and duration and cause and severity and age and gender):
            return "Please fill in all fields."

        return "Form submitted successfully!"

    return render_template('f_stories.html')

if __name__ == '__main__':
    app.run(debug=True)