import requests
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os
import json

app = Flask(__name__, static_folder=os.path.dirname(os.path.abspath(__file__)))
CORS(app)

# Route to serve your elite index.html
@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')

# The AI Engine using your local Llama 3.2:1b model
@app.route('/grade', methods=['POST'])
def grade_answer():
    try:
        data = request.json
        
        # Professional Senior Professor Prompt for structural HTML output
        prompt = f"""
        Act as a Senior Academic Professor. 
        Question: {data.get('question')}
        Student's Answer: {data.get('answer')}
        
        Evaluate accurately. Provide professional feedback in HTML format.
        Use <h3> for titles and <ul> for bullet points.
        Return ONLY this JSON structure:
        {{"score": 8, "report": "HTML_CONTENT_HERE"}}
        """

        # Talking to your Local Ollama (Llama 3.2:1b)
        # Optimized with temperature and num_predict for speed on your 8GB RAM
        response = requests.post('http://localhost:11434/api/generate', 
            json={
                "model": "llama3.2:1b",
                "prompt": prompt,
                "stream": False,
                "format": "json",
                "options": {
                    "num_predict": 300,
                    "temperature": 0.3
                }
            }, timeout=45)
        
        local_result = response.json()
        # Parse the JSON string sent back by Ollama
        return jsonify(json.loads(local_result['response']))
    
    except Exception as e:
        # Professional error handling if the local brain is not responding
        return jsonify({
            "score": 0, 
            "report": f"<p style='color:red'>The Professor is currently offline. (Error: {str(e)})</p>"
        })

if __name__ == '__main__':
    # Professional Terminal Output to ensure you use the correct link for Firebase
    print("\n" + "═"*50)
    print(" 🚀  GRADEWISE ELITE EDITION: ONLINE")
    print(" 🎓  STATUS: Local Brain (Llama 3.2:1b) Connected")
    print(" 🔗  SEAMLESS LINK: http://localhost:5000")
    print(" ⚠️  USE THE LINK ABOVE FOR SIGN-IN TO WORK!")
    print("═"*50 + "\n")
    
    # Run the server on port 5000
    app.run(debug=True, port=5000)
