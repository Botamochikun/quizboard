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
    name = request.form['name']
    image = request.form['image']
    print(f"Received image data (first 100 chars): {image[:100]}")
    answers.append((name, image))
    return redirect('/player')


@app.route('/reset')
def reset():
    answers.clear()
    return redirect('/host')


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
