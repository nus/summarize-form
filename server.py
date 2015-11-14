#coding :utf-8

from flask import abort, Flask, jsonify, render_template, request
import extractcontent
import requests
from requests.exceptions import ConnectionError
from summpy.lexrank import summarize

app = Flask(__name__)

@app.route('/')
def show_index():
    return render_template('index.html')

@app.route('/api/summarize.json')
def api_summarize_text():
    try:
        text = request.args.get('text', None)
        url = request.args.get('url', None)
        if text is None and url is None:
            raise ValueError('No value in text or url parameters.')
        sentence_limit = int(request.args.get('sent_limit', 3))
        if sentence_limit < 1:
            raise ValueError('sent_limit parameter must be a natural number.')
        if url:
            r = requests.get(url)
            if not (200 <= r.status_code < 300):
                raise ValueError('url is bad.')
            text = r.text

            extractor = extractcontent.ExtractContent()
            extractor.analyse(text)
            text, _ = extractor.as_text()
    except ValueError, e:
        abort(404, str(e))
    except ConnectionError, e:
        abort(404, str(e))

    summary, debug_info = summarize(
        text, sentence_limit,
        debug=True, continuous=True)
    return jsonify({
        'summary': summary,
        'debug_info': debug_info})

if __name__ == '__main__':
    app.run(host='localhost', port=8080, debug=True)
