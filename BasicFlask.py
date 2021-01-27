from flask import Flask

# Instantiate the Flask app
app = Flask(__name__)

@app.route('/') # Home Directory
def hello():
    return "Hello AI-ML Batch 2 Students. Congratulations to all of you."

# Run
if __name__ == '__main__':
    app.run(debug=True)

