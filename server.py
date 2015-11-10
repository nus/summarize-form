#coding :utf-8

from flask import abort, Flask, jsonify, render_template, request
from summpy.lexrank import summarize

app = Flask(__name__)

@app.route('/')
def show_index():
    return render_template('index.html')

@app.route('/api/summarize.json')
def api_summarize_text():
    try:
        text = request.args.get('text', '')
        if len(text) == 0:
            raise ValueError('No value in text parameter.')
        sentence_limit = int(request.args.get('sent_limit', 3))
        if sentence_limit < 1:
            raise ValueError('sent_limit parameter must be a natural number.')
    except ValueError, e:
        abort(404, str(e))

    summary, debug_info = summarize(
        text, sentence_limit,
        debug=True, continuous=True)
    return jsonify({
        'summary': summary,
        'debug_info': debug_info})

if __name__ == '__main__':
    app.run(host='localhost', port=8080, debug=True)
