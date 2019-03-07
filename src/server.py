from flask import Flask, render_template
from tickets import get_ticket_data


app = Flask(__name__)


@app.route('/')
def download_file(name=None):
    return render_template('index.html', name=name)


@app.route('/')
def download_file1(name=None):
    return render_template('map.js', name=name)


@app.route('/tickets')
def server_static():
    f = 'https://data.buffalony.gov/resource/d6g9-xbgu.json'
    return get_ticket_data(f)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
