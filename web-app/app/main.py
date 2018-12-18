from flask import Flask, request, session, flash, make_response, render_template, send_file, redirect, url_for, abort, send_file
from database import init_db
from database import db
from flask_sqlalchemy import SQLAlchemy

import os
import models

app = Flask(__name__)
app.config.from_object('config.Config')
init_db(app)

app.secret_key = '\x81\\j\xa2\xd4\x1d\x01^\xc0y\x0el\xec|1S\xe6\x1b\x0f\xe53\x85?\xd7'

@app.teardown_request
def teardown_request(exception):
    if exception:
        db.session.rollback()
    db.session.remove()

@app.route('/')
def hello():
    return render_template('index.html')

# healthcheck
@app.route('/healthy')
def index():
    return 'healthy'

@app.errorhandler(404)
def error_handler(error):
    return 'Not Found.', 404

@app.errorhandler(500)
def error_handler(error):
    return 'Internal ServerError.', 500
    
if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=False, port=80)
