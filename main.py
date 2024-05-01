
from flask import Flask, request, redirect, url_for, render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit_query', methods=['POST'])
def submit_query():
    query = request.form['query']
    response = requests.get(f'https://vertexai.googleapis.com/v1/projects/{project_id}/locations/{location}/models/{model_id}:generateText?key={api_key}', json={"prompt": {"text": query}})
    response_text = response.json()['candidates'][0]['output']
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
