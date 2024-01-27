from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def test_stories():
    return render_template('f_stories.html')

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        required_fields = ['addiction-type', 'duration', 'cause', 'severity', 'age', 'gender']
        form_data = {field: request.form.get(field) for field in required_fields}

        if not all(form_data.values()):
            return "Please fill in all fields."

        return "Form submitted successfully!"

    return render_template('f_stories.html')
if __name__ == '__main__':
    app.run(debug=True)