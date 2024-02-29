from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
    {
        "id": 1,
        "title": "AI/Machine Learning Engineer",
        'location': "Enugu, Nigeria",
        "salary": "#400,000"
    },
    {
        "id": 2,
        "title": "Prompt Engineer",
        'location': "Awka, Nigeria",
        # "salary": "#250,000"
    },
    {
        "id": 3,
        "title": "AI Engineer",
        'location': "Remote",
        "salary": "#700,000"
    }
]


@app.route('/')
def home():
    return render_template('home.html', jobs=JOBS, company_name="Jovian")


@app.route('/api/jobs')
def list_jobs():
    return jsonify(JOBS)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)