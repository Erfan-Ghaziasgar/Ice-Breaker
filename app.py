from dotenv import load_dotenv
from flask import Flask, request, jsonify, render_template
from main import ice_breaker_with
import os

load_dotenv()

# Set the template_folder to the correct path
app = Flask(__name__, template_folder="ice_breaker/templates")


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/process', methods=['POST'])
def process():
    name = request.form['name']
    try:
        summary, profile_pic_url = ice_breaker_with(name)
        if summary is None:
            raise ValueError("No summary generated.")
        response = {
            'summary_and_facts': summary.to_dict(),
            "picture_url": profile_pic_url if profile_pic_url else "",
        }
    except Exception as e:
        response = {
            'summary_and_facts': {
                "summary": "Sorry, no ice breaker could be generated.",
                "facts": []
            },
            "picture_url": "",
            "error": str(e)
        }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
