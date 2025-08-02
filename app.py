import os

from flask import Flask, render_template, request, redirect
app = Flask(__name__)

answers = []

@app.route('/')
def index():
    return redirect('/player')

@app.route('/player')
def player():
    return render_template('player.html')

@app.route('/host')
def host():
    return render_template('host.html', answers=answers)

@app.route('/submit', methods=['POST'])
def submit():
    print("Submit endpoint hit")
    name = request.form.get('name')
    image = request.form.get('image')
    print(f"Received name: {name}")
    print(f"Received image data (start): {image[:30] if image else 'No image data'}")
    answers.append((name, image))
    return redirect('/player')


@app.route('/reset')
def reset():
    answers.clear()
    return redirect('/host')


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
