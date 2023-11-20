from flask import Flask, render_template, request
import openai

openai.api_key = "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"

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        color = request.form['color']
        occasion = request.form['occasion']
        receiver = request.form['receiver']
        fragrance = request.form['fragrance']
        msg = request.form['msg']

        prompt = "Please suggest me what flowers should I gift as per the following conditions: Receiver of flowers: " + receiver + ", Occasion: " + occasion + ", Colors/Tones: " + color + ", Fragrance: " + fragrance +  ", Message you want to convey: " + msg + ". I don't want a list of flowers. I want your answer to be very specific in about 40-50 words."
        conversation = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": prompt}
    ]

        response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=conversation
    )
        
        assistant_response = response.choices[0].message['content'].strip()


        return render_template('index.html', assistant_response=assistant_response)

if __name__ == '__main__':
    app.run(debug=True)
