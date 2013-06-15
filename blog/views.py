from datetime import datetime
from flask import render_template
from blog import app


@app.route('/')
def home():
    return render_template('index.html', **get_page_data())


def get_page_data():
    now = datetime.now()
    return {
        'YEAR': now.year
    }
