import os
from flask import Flask, render_template, request, redirect, jsonify

app = Flask(__name__)

# answersは辞書のリストに変更、scoreも持つ
answers = []  # [{'name': ..., 'image': ..., 'score': 0}, ...]

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
    name = request.form.get('name')
    image = request.form.get('image')
    # 新規提出はスコア0で追加
    answers.append({'name': name, 'image': image, 'score': 0})
    return redirect('/player')

@app.route('/score', methods=['POST'])
def score():
    data = request.get_json()
    name = data.get('name')
    is_correct = data.get('correct')
    for a in answers:
        if a['name'] == name:
            a['score'] = 1 if is_correct else 0
            break
    return jsonify(success=True)

@app.route('/score/<name>')
def get_score(name):
    for a in answers:
        if a['name'] == name:
            return jsonify(score=a['score'])
    return jsonify(score=0)

@app.route('/reset')
def reset():
    answers.clear()
    return redirect('/host')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
