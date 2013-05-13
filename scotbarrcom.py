from datetime import datetime
from flask import Flask, render_template
import config


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html', **get_page_data())


def get_page_data():
    now = datetime.now()
    return {
        'YEAR': now.year
    }

if __name__ == '__main__':
    app.run(host=config.HOST, port=config.PORT, debug=config.DEBUG)
