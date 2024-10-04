import openai
from flask import Flask, request, jsonify

app = Flask(__name__)

openai.api_key = "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"

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('input')
    response = openai.Completion.create(
      engine="text-davinci-003",
      prompt=user_input,
      max_tokens=150
    )
    reply = response.choices[0].text.strip()
    return jsonify({'response': reply})

if __name__ == '__main__':
    app.run(debug=True)
